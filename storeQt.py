from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
from store import Store

class ShowInfo(QWidget):
    def __init__(self, txt, title):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.text = QTextEdit('')
        self.text.setText(txt)
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)
        self.layout.addWidget(self.text)
        self.setFixedSize(400, 600)
        self.setWindowTitle(title)
        self.show()

class AITInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)

class AddNewClient(QWidget):
    def __init__(self, store):
        super().__init__()
        self.store = store
        self.layout = QVBoxLayout()
        self.label1 = AITLabel('Name')
        self.label2 = AITLabel('Phone number')
        self.input1 = AITInput()
        self.input2 = AITInput()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.input2)

        self.button = AITButton('Add Client', self.add_client)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def add_client(self):
        self.store.clients.append(self.input1.text())
        self.close()




class AITButton(QPushButton):
    def __init__(self, title, func):
        super().__init__(title)
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)
        self.clicked.connect(func)

class AITLabel(QLabel):
    def __init__(self, title):
        super().__init__(title)
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)

class AITCombo(QComboBox):
    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.font.setPointSize(18)
        self.setFont(self.font)


class NewItem(QWidget):
    def __init__(self):
        super().__init__()


class StoreApp(QWidget):
    def __init__(self, storename):
        super().__init__()
        self.store = Store(storename)
        self.store.clients = []
        self.store.items = []

        self.layout = QVBoxLayout()
        
        self.client_label = AITLabel('Client')
        self.clients = AITCombo()
        self.layout.addWidget(self.client_label)
        self.layout.addWidget(self.clients)


        self.item_label = AITLabel('Item')
        self.items = AITCombo()

        self.layout.addWidget(self.item_label)
        self.layout.addWidget(self.items)


        self.button0 = AITButton('Add to cart', self.ait_add_to_cart)
        self.button1 = AITButton('Add client', self.ait_add_client)
        self.button2 = AITButton('Add item', self.ait_add_item)
        self.button3 = AITButton('Show profit', self.ait_show_profit)
        self.button4 = AITButton('Show history', self.ait_show_history)
        self.button5 = AITButton('Show item', self.ait_show_item)
        self.layout.addWidget(self.button0)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)


        self.update = AITButton('Update', self.update)
        self.layout.addWidget(self.update)



        self.setLayout(self.layout)
        #self.setFixedSize(600, 800)

    def ait_add_to_cart(self):
        pass

    def ait_add_client(self):
        self.add_client_window = AddNewClient(self.store)
        self.add_client_window.show()
    
    def update(self):
        self.clients.clear()
        self.clients.addItems(self.store.clients)

    def ait_add_item(self):
        pass

    def ait_show_history(self):
        self.h = ShowInfo(self.store.show_history(), 'Isken')
        self.h.show()
    
    def ait_show_item(self):
        pass

    def ait_show_profit(self):
        self.w = ShowInfo('Profit: ' + str(self.store.show_profit()), 'Total Profit')
        self.w.show()


if __name__ == "__main__":
    app = QApplication([])
    store = StoreApp('AIT')
    store.show()
    app.exec_()
