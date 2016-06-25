"""
scraper.py module
15.06.2016.
Miroslav Vidovic

"""
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
          :return: A list of dictionaries containing the title, date and the
          image for every comic

          """

        comics = self.bsoup.find_all('div', {'class': 'comic-item-container'})
        output = []
        for comic in comics:
            date = comic.find('span', {'class': 'comic-date-wrapper'})
            date_start = date.find('span').text
            year = date.find('span', {'itemprop': 'copyrightYear'}).text
            full_date = date_start + year

            img = comic.find('img', {'class': 'img-comic'})
            url = img.attrs['src']

            title = comic.find('span', {'class': 'comic-title-name'}).text
            output.append({
                'title': title, 'date': full_date, 'image': url
            })
        return output
