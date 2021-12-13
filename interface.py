import sys
from PySide6 import QtCore, QtWidgets, QtGui


class HomeView(QtWidgets.QWidget):
    """
        HomeView class that returns the default view whenever the application is launched.
    """
    def __init__(self):
        """
            __init__ constructor
        """
        super().__init__()
        self.text = QtWidgets.QLabel("Hello World!",
                                     alignment = QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = HomeView()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())