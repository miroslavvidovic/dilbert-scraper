from dilbert.scraper import Scraper
from dilbert.dilbert_comic import DilbertComic

scraper = Scraper()
result = scraper.get_data()
print(result)
