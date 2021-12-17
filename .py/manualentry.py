import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui, QtCore
from manualentry_gui import Ui_Form


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ids = []
        self.loaddata()
        self.ui.pushButton.clicked.connect(self.processing)

    def loaddata(self):
        conn = sqlite3.connect("../db/inventory.db")
        cur = conn.cursor()
        query = 'SELECT mat_code FROM inventory;'
        self.ids = cur.execute(query)


    def incrementstock(self, prod_id):
        conn = sqlite3.connect("../db/inventory.db")
        cur = conn.cursor()
        query = f"SELECT * FROM inventory WHERE mat_code= '{prod_id}'"
        prod = cur.execute(query)
        index = []
        currstock = []
        for el in list(prod):
            index = el[0]
            currstock = el[4]
        updatequery =  f"UPDATE inventory SET stock = {currstock+1} WHERE id = {index}"
        cur.execute(updatequery)
        conn.commit()
#HW100XXXPDXFA-F
    def processing(self):

        lbl = self.ui.label_5
        lbl.setGeometry(QtCore.QRect(520, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        lbl.setFont(font)
        input = self.ui.lineEdit_2.text()
        flag = False
        if not input:
            flag = False
        for id in self.ids:
            if input == id[0]:
                flag = True
        if not flag:
            lbl.setText("Please enter a valid Product ID")
            self.loaddata()
        else:
            #Increment stock of the given prod. ID.
            self.incrementstock(input)
            lbl.setText("Stock updated successfully.")
            self.loaddata()


def main():
    app = QApplication(sys.argv)
    disp = MainWindow()
    disp.setWindowTitle("Inventory Management System")
    disp.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()