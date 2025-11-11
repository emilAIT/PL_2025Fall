from PyQt5.QtWidgets import *
import requests

class Store(QWidget):
    def __init__(self):
        super().__init__()

        self.url = 'https://ait25.pythonanywhere.com'
        self.x = {"Content-Type": "application/json; charset=utf-8"}

        self.form = QFormLayout()
        self.id = QLineEdit()
        self.name = QLineEdit()
        self.price = QLineEdit()
        self.amount = QLineEdit()
        self.history = QTextEdit()

        self.addButton = QPushButton('add')
        self.sellButton = QPushButton('sell')     
        self.historyButton = QPushButton('history')

        self.form.addRow('id', self.id)
        self.form.addRow('name', self.name)
        self.form.addRow('price', self.price)
        self.form.addRow('amount', self.amount)

        self.form.addWidget(self.addButton)
        self.form.addWidget(self.sellButton)
        self.form.addWidget(self.historyButton)
        self.form.addWidget(self.history)

        self.addButton.clicked.connect(self.add)
        self.sellButton.clicked.connect(self.sell)
        self.historyButton.clicked.connect(self.showHistory)

        self.setLayout(self.form)
        self.setFixedSize(600, 800)


    def sell(self):
        cid = self.id.text()
        amount = int(self.amount.text())
        mergen = {'id': cid, 'amount': amount}
        r = requests.get(self.url + '/sell', headers=self.x, json = mergen)
        self.history.setText(str(r.json()))


    def add(self):
        cid = self.id.text()
        name = self.name.text()
        price = int(self.price.text())
        dilya = {'id': cid, 'name': name, 'price': price}
        r = requests.get(self.url + '/add', headers=self.x, json=dilya)
        self.history.setText(str(r.json()))

    def showHistory(self):
        r = requests.get(self.url + '/history')
        self.history.setText(str(r.json()))

if __name__ == "__main__":
    app = QApplication([])
    store = Store()
    store.show()
    app.exec_()

