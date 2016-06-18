"""
search_scraper.py module
17.06.2016.
Miroslav Vidovic

"""
from bs4 import BeautifulSoup
from requests import get


class SearchScraper(object):
    """
    SearchScraper class
    scrape the Dilbert comic website search page for data

    """

    def __init__(self, page_num, year):
        """
        :param page_num: number of pages to scrape
        :param year: number of years
        :type page_num: int
        :type year: int

        """
        self.page_num = page_num
        self.year = year
        self.dilbert_page = get(
            'http://dilbert.com/search_results?page=' +
            str(self.page_num) + '&sort=date_asc&year=' + str(self.year))
        self.bsoup = BeautifulSoup(self.dilbert_page.content, "lxml")

    def get_data(self):
        """
          Scrape the data from the website
          :rtype: list[dict]
          :return: title, date and the image for every comic

        """
        comics = self.bsoup.find_all('div', {'class': 'comic-item-container'})
        output = []
        for comic in comics:
            date = comic.find('span', {'class': 'comic-date-wrapper'})
            date_start = date.find('span').text
            year = date.find('span', {'itemprop': 'copyrightYear'}).text

            img = comic.find('img', {'class': 'img-comic'})
            url = img.attrs['src']

            title = comic.find('span', {'class': 'comic-title-name'}).text
            output.append({
                'title': title, 'date': date_start + year, 'url': url
            })
        return output
