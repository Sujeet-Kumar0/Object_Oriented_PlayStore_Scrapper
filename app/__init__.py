from flask import Flask, request, jsonify

from app.AppScrapper import AppScraper

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
async def main():
    if request.method == "GET":
        return "Hello"
    else:
        app_id = request.form["AppID"]

    app_scrapper = AppScraper(app_id)
    app_scrapper.scrape()
    response = app_scrapper.result
    return jsonify(response)
