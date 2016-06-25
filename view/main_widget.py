"""
main_widget.py module
15.06.2016.
Miroslav Vidovic

"""
from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, \
    QLabel

from controller import scrape_and_save
from database.database import Database


class MainWidget(QWidget):
    """
    MainWidget class
    Main widget for the main window

    """
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.load_button = QPushButton("Load data")
        self.load_button.clicked.connect(self.scrape_data)
        self.layout.addWidget(self.load_button)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.item_clicked)
        self.layout.addWidget(self.list_widget)

        # Load the data from the database
        self.load_data()

        self.setLayout(self.layout)

    def scrape_data(self):
        """
        Scrape the data and load it into the list widget

        """
        scrape_and_save()
        self.load_data()
        self.status_label.setText("Data loaded")

    def load_data(self):
        """
        Load the data from the database into the list widget

        """
        self.list_widget.clear()
        data = Database.load_data_from_db()
        for item in data:
            self.list_widget.addItem(item.date + " : " + item.title + " - " +
                                     item.image)

    def item_clicked(self, item):
        """
        When a user clicks on the item in the list widget get the url for the
        item image and open it in the browser
        :param item: List widget item

        """
        text = item.text()
        image = text.split(' - ')
        image = image[1]
        import webbrowser
        webbrowser.open(image)
