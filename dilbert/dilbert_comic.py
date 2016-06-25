"""
dilbert_comic.py module
15.06.2016.
Miroslav Vidovic

"""


class DilbertComic(object):
    """
    Class for DilbertComic objects containing the title, image and the date

    """
    def __init__(self):
        self.__title = None
        self.__image = None
        self.__date = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value


