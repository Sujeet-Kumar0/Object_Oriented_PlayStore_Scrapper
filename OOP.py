import pandas as pd
import concurrent.futures

from app.AppScrapper import AppScraper


class GooglePlayScraper:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def get_input(self):
        self.df = pd.read_csv(self.input_path, encoding='utf-8')

    def start_scraping(self, app_name):
        app_scraper = AppScraper(app_name)
        app_scraper.scrape()
        return app_scraper.get_result()

    def process_result(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self.start_scraping, self.df["Package Names"]))

        return results

    def save_results_to_csv(self, results):
        df_results = pd.DataFrame(results)
        df_results.to_csv(self.output_path, index=False)
        print(f"Results saved to {self.output_path}")


def main():
    input_path = "C:\\Users\\ISU-2035\\Documents\\Book1.csv"
    output_path = "C:\\Users\\ISU-2035\\Documents\\google_play_results.csv"

    g = GooglePlayScraper(input_path, output_path)
    g.get_input()
    print("Scraping Started")

    results = g.process_result()
    g.save_results_to_csv(results)


if __name__ == "__main__":
    main()
