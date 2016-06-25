"""
database.py module
15.06.2016.
Miroslav Vidovic

"""
import dataset
from dilbert.dilbert_comic import DilbertComic


class Database(object):
    """
    Database class
    Interact with the sqlite database using the python dataset library

    """

    database = dataset.connect('sqlite:///database/dilbert.sqlite')
    table = database['comics']

    @classmethod
    def save_data_to_db(cls, item):
        """
        Save the data to the database
        :param item: Item containing the title, date and image url for a comic
        :type item: dict

        """
        cls.table.upsert(item, ['date'])

    @classmethod
    def load_data_from_db(cls):
        """
        Load the date, image url and the title from the database into a
        DilbertComic object
        :return: DilbertComic

        """
        comics_data = []
        comics = cls.table.all()
        for comic in comics:
            dilbert = DilbertComic()
            dilbert.date = comic['date']
            dilbert.image = comic['image']
            dilbert.title = comic['title']
            comics_data.append(dilbert)
        return comics_data
