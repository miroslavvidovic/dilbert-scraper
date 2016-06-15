from bs4 import BeautifulSoup
import requests
from requests import get
import time
import os

class Scraper:

    def __init__(self):
        self.dilbert_page = requests.get('http://dilbert.com/')
        self.bsoup = BeautifulSoup(self.dilbert_page.content, "lxml")

    def get_data(self):
        comics = self.bsoup.find_all('div',{'class':'comic-item-container'})
        output = []
        for comic in comics:
            date = comic.find('span',{'class':'comic-date-wrapper'})
            date_start = date.find('span').text
            year = date.find('span',{'itemprop':'copyrightYear'}).text

            img = comic.find('img',{'class':'img-comic'})
            url = img.attrs['src']
            self.download(url, self.generate_name())

            title = comic.find('span',{'class':'comic-title-name'}).text
            output.append({'title':title,'date':date_start + year, 'url':url})

        return output

    def download(self, url, file_name):
        path = "images/"
        with open(os.path.join(path, file_name), "wb") as file:
            # get request
            response = get(url)
            # write to file
            file.write(response.content)

    def generate_name(self):
        timestamp = time.asctime()
        name = timestamp + ".jpg"
        return name

