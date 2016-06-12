class DilbertComic():
    """

    """
    def __init__(self):
        self._title = None
        self._image = None
        self._date = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value


