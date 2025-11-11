from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
from store import Store
import requests

class StoreApp(QWidget):
    def __init__(self, storename):
        super().__init__()
        self.form = QFormLayout()
        self.id = QLineEdit()
        self.name = QLineEdit()
        self.age = QLineEdit()
        self.phone = QLineEdit()
        self.button = QPushButton('Add')
        self.button.clicked.connect(self.add_customer)
        self.form.addRow('id', self.id)
        self.form.addRow('phone', self.phone)
        self.form.addRow('name', self.name)
        self.form.addRow('age', self.age)
        self.form.addWidget(self.button)
        self.setLayout(self.form)
        self.setFixedSize(400,400)

    def add_customer(self):
        cid = self.id.text()
        phone = self.phone.text()
        name = self.name.text()
        age = self.age.text()

        url = "https://ait25.pythonanywhere.com/add"

        headers = {"Content-Type": "application/json; charset=utf-8"}

        d = {'id':cid, 'name':name, 'phone':phone, 'age':age}

        response = requests.get(url, headers=headers, json=d)

        print(response.json())




if __name__ == "__main__":
    app = QApplication([])
    store = StoreApp('AIT')
    store.show()
    app.exec_()
