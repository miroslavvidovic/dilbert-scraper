"""
scraper.py module
15.06.2016.
Miroslav Vidovic

"""
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
          :rtype: list[dict]
          :return: title, date and the image for every comic

          """

        def download(file_url, file_name):
            """
            Download a file
            :param file_url: url of the targeted file
            :param file_name: name for the saved file
            :type file_url: string
            :type file_name: string

            """
            path = "images/"
            with open(os.path.join(path, file_name), "wb") as destination:
                response = get(file_url)
                destination.write(response.content)

        def generate_name(name):
            """
            Generate a name for an image by adding .jpg to the param name
            :param name: name for the file
            :type name: string
            :return: name.jpg
            :rtype string
            """
            file_name = name + ".jpg"
            return file_name

        comics = self.bsoup.find_all('div', {'class': 'comic-item-container'})
        output = []
        for comic in comics:
            date = comic.find('span', {'class': 'comic-date-wrapper'})
            date_start = date.find('span').text
            year = date.find('span', {'itemprop': 'copyrightYear'}).text
            full_date = date_start + year

            img = comic.find('img', {'class': 'img-comic'})
            url = img.attrs['src']

            img_name = generate_name(full_date)
            download(url, img_name)

            title = comic.find('span', {'class': 'comic-title-name'}).text
            output.append({
                'title': title, 'date': full_date, 'image': img_name
            })
        return output
