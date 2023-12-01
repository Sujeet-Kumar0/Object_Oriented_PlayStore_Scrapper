import pandas as pd
from google_play_scraper import app


class GooglePlayScraper:
    def __init__(self):
        self.df = None
        self.results = []

    def get_input(self, path):
        self.df = pd.read_csv(path)

    def start_scraping(self, package):
        result = None
        try:
            result = app(package)
            print("result: " + str(result.get("title")))
        except Exception as e:
            print("Error: " + str(e))
        self.results.append(result)

    def process_result(self):
        for idx, appName in enumerate(self.df["Package Names"]):
            self.start_scraping(appName)

            if idx >= 10:
                break


if __name__ == "__main__":
    g = GooglePlayScraper()
    g.get_input(path="C:\\Users\\ISU-2035\\Documents\\Book1.csv")
    print("Scraping Started")
    g.process_result()
