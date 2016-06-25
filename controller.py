"""
controller.py module
15.06.2016.
Miroslav Vidovic

"""
import os
import datetime
from requests import get
from dilbert.scraper import Scraper
from database.database import Database


def scrape_data():
    """
    Scrape the data using the Scraper class

    """
    scraper = Scraper()
    data = scraper.get_data()
    return data


def scrape_and_save():
    """
    Scrape the data and save it into the database using the Database class

    """
    data = scrape_data()
    for item in data:
        Database.save_data_to_db(item)


def download(file_url, file_name):
    """
    Download a file
    :param file_url: Url of the targeted file
    :param file_name: Name for the saved file
    :type file_url: string
    :type file_name: string

    """
    path = "images/"
    with open(os.path.join(path, file_name), "wb") as destination:
        response = get(file_url)
        destination.write(response.content)


def generate_name():
    """
    Generate a name for an image by adding .jpg to the timestamp
    :return: name.jpg
    :rtype string
    """
    timestamp = datetime.datetime.now().strftime("%d_%b_%Y_%H:%M")
    file_name = str(timestamp) + ".jpg"
    return file_name

