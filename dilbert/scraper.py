"""
scraper.py module
"""
import time
import os
from bs4 import BeautifulSoup
from requests import get


class Scraper(object):
    """
    Scraper class
    scrape the Dilbert comic website for useful data

    """

    def __init__(self):
        self.dilbert_page = get('http://dilbert.com/')
        self.bsoup = BeautifulSoup(self.dilbert_page.content, "lxml")

    def get_data(self):
        """
          Scrape the data from the website
          :return: data in dictionary format

          """

        def download(url, file_name):
            """
            Download a file
            :param url: url of the targeted file
            :param file_name: name for the saved file

            """
            path = "images/"
            with open(os.path.join(path, file_name), "wb") as destination:
                response = get(url)
                destination.write(response.content)

        def generate_name():
            """
            Generate an image file name with a timestamp
            :return: timestamp.jpg
            """
            timestamp = time.asctime()
            name = timestamp + ".jpg"
            return name

        comics = self.bsoup.find_all('div', {'class': 'comic-item-container'})
        output = []
        for comic in comics:
            date = comic.find('span', {'class': 'comic-date-wrapper'})
            date_start = date.find('span').text
            year = date.find('span', {'itemprop': 'copyrightYear'}).text

            img = comic.find('img', {'class': 'img-comic'})
            url = img.attrs['src']
            download(url, generate_name())

            title = comic.find('span', {'class': 'comic-title-name'}).text
            output.append({
                'title': title, 'date': date_start + year, 'url': url
            })

        return output
