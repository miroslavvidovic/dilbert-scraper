from dilbert.scraper import Scraper
from dilbert.dilbert_comic import DilbertComic

scraper = Scraper()
titles = scraper.find_titles()
dates = scraper.find_dates()
images = scraper.find_images()
