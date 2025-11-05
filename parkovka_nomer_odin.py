from PyQt5.QtWidgets import QTextEdit,  QApplication, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QFormLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from parking import Parking

class AitButton(QPushButton):
    def __init__(self):
        super().__init__()
        font = QFont()
        font.setPointSize(18)
        self.setFont(font)


class AitInfo(QWidget):
    def __init__(self, d, title=''):
        super().__init__()
        self.title = title
        self.setWindowTitle(title)
        self.form = QFormLayout(self)
        for key, value in d.items():
            self.form.addRow(key, QLabel(text=str(value)))
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        self.font = QFont()
        self.font.setPointSize(18)

        self.combo = QComboBox()
        self.combo.addItem('Iskender')
        self.combo.addItems(['Emil', 'AIt', 'Salam', 'Aleykum'])
        self.combo.setFont(self.font)
        self.form.addWidget(self.combo)

        self.knopka = QPushButton('Najmi knopku')
        self.knopka.setFont(self.font)
        self.knopka.clicked.connect(self.knopka_najmi)
        self.form.addRow('', self.knopka)

        self.knopka_pakaji = QPushButton('Pokaji')
        self.knopka_pakaji.setFont(self.font)
        self.knopka_pakaji.clicked.connect(self.knopka_pokaji)
        self.form.addRow('', self.knopka_pakaji)


    def knopka_najmi(self):
        #self.ui = AitInfo({'Name': 'Emil', 'University': 'AIT'}, self.title + 'Mnogo Knopok')
        #self.ui.show()
        self.knopka.setVisible(False)
    
    def knopka_pokaji(self):
        self.knopka.setVisible(True)

class ParkovkaNomerOdin(QWidget):
    def __init__(self):
        super().__init__()
        self.aitx = []
        self.parking = Parking()
        self.font = QFont()
        self.font.setPointSize(18)
        self.form = QVBoxLayout(self)
        self.id_mashini_label = QLabel('ID Mashini')
        self.id_mashini = QLineEdit('')
        self.id_mashini.setFont(self.font)
        self.id_mashini_label.setFont(self.font)
        self.form.addWidget(self.id_mashini_label)
        self.form.addWidget(self.id_mashini)

        self.add_car_button = QPushButton('Add car')
        self.add_car_button.setFont(self.font)
        self.form.addWidget(self.add_car_button)
        self.add_car_button.clicked.connect(self.ui_add_car)

        self.info = QTextEdit()
        self.info.setFont(self.font)
        self.setFixedHeight(800)
        self.setFixedWidth(600)

        self.add_balance_button = AitButton()
        self.add_balance_button.setText('Add Balance') #QPushButton('Add balance')
        self.form.addWidget(self.add_balance_button)
        self.add_balance_button.clicked.connect(self.ui_add_balance)
        #self.add_balance_button.setFont(self.font)

        self.remove_car_button = QPushButton('Remove car')
        self.form.addWidget(self.remove_car_button)
        self.remove_car_button.clicked.connect(self.ait_remove_car)
        self.remove_car_button.setFont(self.font)

        self.update_button = QPushButton('Update car')
        self.form.addWidget(self.update_button)
        self.update_button.clicked.connect(self.ait_update_car)
        self.update_button.setFont(self.font)

        self.export_button = QPushButton('Export to file')
        self.form.addWidget(self.export_button)
        self.export_button.clicked.connect(self.ait_export_to_file)
        self.export_button.setFont(self.font)

        self.history_button = QPushButton('Show history')
        self.form.addWidget(self.history_button)
        self.history_button.clicked.connect(self.ait_show_history)
        self.history_button.setFont(self.font)

        self.show_info = QPushButton('Show Info')
        self.form.addWidget(self.show_info)
        self.show_info.clicked.connect(self.ait_show_info)
        self.show_info.setFont(self.font)

        self.form.addWidget(self.info)

    def beautify(self, d):
        s = ''
        for key, value in d.items():
            s += key + '\n' + '-'*20 + '\n'
            if type(value) == list:
                s += '\n'.join(value)
            elif type(value) == dict:
                for a, b in value.items():
                    s += f'{a} : {b}\n'
            s += '*'*20 + '\n'
        
        return s + '\n'


    def ui_add_car(self):
        id = self.id_mashini.text()
        self.id_mashini.setText('')
        self.parking.add_car(id)
        self.update_info()

    def update_info(self):
        self.info.setText(self.beautify(self.parking.d))


    def ui_add_balance(self):
        id, balance = self.id_mashini.text().split(',')
        self.id_mashini.setText('')
        self.parking.add_balance(id, int(balance))
        self.update_info()

    def ait_remove_car(self):
        id = self.id_mashini.text()
        self.parking.remove_car(id)
        self.update_info()
    
    def ait_update_car(self):
        id, new_id = self.id_mashini.text().split(',')
        self.parking.update_car_info(id, new_id)
        self.update_info()
    
    def ait_export_to_file(self):
        filename = self.id_mashini.text()
        self.parking.export_csv(filename)
    
    def ait_show_history(self):
        self.info.setText(str(self.parking.history))
    
    def ait_show_info(self):
        id = self.id_mashini.text()
        d = self.parking.d[id]

        self.aitx.append(AitInfo(d, f'Info mashini = {id}'))
        self.aitx[-1].show()

if __name__ == "__main__":
    app = QApplication([])
    parkovka_app = ParkovkaNomerOdin()
    parkovka_app.show()
    app.exec_()