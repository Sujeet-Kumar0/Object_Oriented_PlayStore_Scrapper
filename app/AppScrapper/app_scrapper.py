from google_play_scraper import app


class AppScraper:
    def __init__(self, package_name):
        self.package_name = package_name
        self.result = None

    def scrape(self):
        try:
            self.result = app(self.package_name)
            print("Result:", self.result.get("title"))
            self.result = {"title": self.result.get('title'), "appID": self.result.get('appId'),
                           "version": self.result.get(
                               'version'), "developer": self.result.get('developer'),
                           "updated_on": self.result.get('updated')}
        except Exception as e:
            print("Error:", e)
            self.result = {"title": self.package_name}

    def get_result(self):
        return self.result
