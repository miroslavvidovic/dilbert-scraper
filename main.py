import sys
from PyQt5.QtWidgets import QApplication
from view.main_window import MyMainWindow

if __name__ == '__main__':
    app = QApplication([])
    main = MyMainWindow()
    main.show()
    sys.exit(app.exec_())

