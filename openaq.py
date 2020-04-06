import pandas as pd
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2018, 1, 1)
end_dt = date(2019, 12, 31)
dfs = []
for dt in daterange(start_dt, end_dt):
    try:
        base_url = 'https://openaq-data.s3.amazonaws.com/'
        date_url = f'{base_url}{dt}.csv'
        print(date_url)
        df = pd.read_csv(date_url)
        df_delhi = df[df.city=='Delhi']
        df_delhi_pm25 = df_delhi[df_delhi.parameter=='pm25']
        df_delhi_pm25.index = pd.to_datetime(df_delhi_pm25.local)
        dfs.append(df_delhi_pm25)
    except:
        pass
overall_df = pd.concat(dfs)
overall_df = overall_df.drop(["attribution", "local", "utc", "parameter"], 1)
overall_df.to_csv("open-aq.csv")