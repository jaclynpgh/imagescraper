#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

from flask import Flask
from imagescraper import image_scraper




app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "Must be a GET Request to pass url; GET https://websiteimagescraper.herokuapp.com/URlpathHERE "


@app.route("/<path:query>", methods=['GET'])
def get_image(query):
    return image_scraper(query)


if __name__ == '__main__':
    # change to your own port
    app.run(host='0.0.0.0', port=2455, debug=True)



