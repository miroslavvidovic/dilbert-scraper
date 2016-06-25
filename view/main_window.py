"""
main_window.py module
15.06.2016.
Miroslav Vidovic

"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from view.main_widget import MainWidget


class MyMainWindow(QMainWindow):
    """
    MyMainWindow class
    Application main window
    """
    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle("Dilbert Scraper")
        self.setWindowIcon(QIcon("resources/icon.png"))

        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)
