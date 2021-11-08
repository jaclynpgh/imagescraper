import requests
from requests.exceptions import HTTPError
def get_imageAPI(url):
    """:param index (int) for parsing json and getting different images
    :param query (string) search term to scrape corresponding images"""

    imageAPI_url = 'https://websiteimagescraper.herokuapp.com/'
    url = url.replace(' ', '+')
    try:
        response = requests.get(imageAPI_url + url)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()
        # print(jsonResponse) - run to print all of json data
        # grabs image url from json based on index

        return jsonResponse

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

print(get_imageAPI("https://www.cookinglight.com/recipes/vegetarian-green-curry-stew"))