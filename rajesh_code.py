# import requests
#
# r = requests.get(url="https://play.google.com/store/apps/details?id=com.netmarble.tog&hl=en&gl=US")
# print(r.status_code)
# r.body()

from google_play_scraper import app, exceptions
import csv
import pandas as pd

df = pd.read_csv("Book1.csv")
# df = df[["Package Names", "Client Status", "Application Name", "Paly Status"]]
# print(df["Package Names"].head(10))
# print(type(df["Package Names"].loc[1]))
for appName in df["Package Names"]:
    try:
        result = app(
            appName
        )
        print("result :", result.get("title"))
    except:
        # raise exceptions.NotFoundError("Not found")
        print("Error Found")
        pass
