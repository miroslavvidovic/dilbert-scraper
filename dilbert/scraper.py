from bs4 import BeautifulSoup
import requests
from requests import get
import time
import re


class Scraper:

    def __init__(self):
        self.dilbert_page = requests.get('http://dilbert.com/')
        self.bsoup = BeautifulSoup(self.dilbert_page.content, "lxml")

    def find_titles(self):
        titles = self.bsoup.find_all("span", {"class": "comic-title-name"})
        for title in titles:
            self.extract_title(str(title))

    def extract_title(self, text):
        start = '<span class="comic-title-name">'
        end = '</span>'
        result = re.search('%s(.*)%s' % (start, end), text).group(1)
        return(result)

    def find_dates(self):
        dates = self.bsoup.find_all("date", {"class": "comic-title-date"})
        for date in dates:
            self.extract_date(str(date))

    def extract_date(self, text):
        # Extract the date - Sunday June 12,
        date_start = '<span>'
        date_end = '</span>'
        date_result = re.search('%s(.*)%s' % (date_start, date_end),
                              text).group(1)

        # Extract the year - 2016
        year_start = '<span itemprop="copyrightYear">'
        year_end = '</span>'
        year_result = re.search('%s(.*)%s' % (year_start, year_end),
                              text).group(1)

        # Combine the results
        result = date_result + ' ' +year_result
        return(result)

    def find_images(self):
        images = self.bsoup.find_all("img", {"class": "img-responsive "
                                                      "img-comic"})
        for image in images:
            url = (image['src'])
            self.download(url, self.generate_name())

    def download(self, url, file_name):
        # open in binary mode
        with open(file_name, "wb") as file:
            # get request
            response = get(url)
            # write to file
            file.write(response.content)

    def generate_name(self):
        timestamp = time.asctime()
        name = timestamp + ".jpg"
        return name

