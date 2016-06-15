from dilbert.scraper import Scraper
from dilbert.scraper_new import Scraper
from dilbert.dilbert_comic import DilbertComic

'''
scraper = Scraper()
titles = scraper.find_titles()
dates = scraper.find_dates()
images = scraper.find_images()
'''

scraper = Scraper()
result = scraper.get_data()
print result
