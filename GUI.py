import sys
import sqlite3
import pandas as pd
from pathlib import Path
from PyQt5 import QtWidgets, QtGui
import db
import logic
import MainWindow
import AuthWindow
import AddWindow

tokens = False

file = Path('token.txt')
file.touch(exist_ok=True)

with open('token.txt', 'r') as file:
    try:
        token_list = file.readlines()
        logic.client_id = token_list[0]
        logic.client_secret = token_list[1]
        tokens = True
    except:
        pass


class GUIMain(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auth_gui = GUIAuth()
        self.add_gui = GUIAdd()
        self.model = QtGui.QStandardItemModel(self)
        self.button_update.clicked.connect(self.update)
        self.button_add.clicked.connect(self.add_char)
        self.button_delete.clicked.connect(self.delete_char)
        self.button_table.clicked.connect(self.table_create)
        self.button_refresh.clicked.connect(self.update_chars)
        self.button_exit.clicked.connect(self.close)
        self.update_chars()

    def update_chars(self):
        self.model.clear()
        self.list_chars.setModel(self.model)
        for item in db.Static.select():
            list_item = QtGui.QStandardItem(item.char_name)
            list_item.setData(item.char_name)
            self.model.appendRow(list_item)
        self.list_chars.setModel(self.model)

    def add_char(self):
        if not tokens:
            self.auth_gui.show()
        else:
            self.add_gui.show()

    def delete_char(self):
        char = self.list_chars.currentIndex().data()
        char_id = db.Static.select().where(db.Static.char_name == char).get()
        db.Static.delete_by_id(char_id)
        self.update_chars()
        pass

    def update(self):
        if not tokens:
            self.auth_gui.show()
        else:
            response = logic.full_update()
            if response == 'Ошибка':
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(f"Ошибка обновления")
                msg_box.exec()
            else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText(f"Данные обновлены")
                self.update_chars()
                msg_box.exec()

    @staticmethod
    def table_create():
        connection = sqlite3.connect(f'static.db')
        pd.read_sql_query(f"select * from 'Статик'", connection).to_excel(f'Статик.xlsx', index=False)
        logic.table_style()
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(f"Таблица создана")
        msg_box.exec()


class GUIAuth(QtWidgets.QMainWindow, AuthWindow.Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_info.clicked.connect(self.get_info)
        self.button_auth.clicked.connect(self.auth)

    def get_info(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.textFormat()
        msg_box.setText(f"Перейдите по ссылке <a href='https://develop.battle.net/access/clients'>Battle.net Develop"
                        f"</a> и создайте пару Client-Secret для доступа к Blizzard Api")
        msg_box.exec()
        pass

    def auth(self):
        logic.client_id = self.clientId.toPlainText().strip()
        logic.client_secret = self.clientSecret.toPlainText().strip()
        response = logic.ApiLauncher().get_tokens()
        if response == 'Ошибка':
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText('Токен указан неверно')
            self.clientId.setText('')
            self.clientSecret.setText('')
            msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText('Токен принят')
            msg_box.exec()
            with open('token.txt', 'w') as file:
                file.write(f'{logic.client_id}\n{logic.client_secret}')
            global tokens
            tokens = True
            self.close()


class GUIAdd(QtWidgets.QMainWindow, AddWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_add.clicked.connect(self.add_char)

    def add_char(self):
        name = self.name_text.toPlainText()
        role = self.combo_role.currentText()
        try:
            exist = db.Static.select().where(db.Static.char_name == name).get()
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText('Данный персонаж уже есть в таблице')
            msg_box.exec()
            return False
        except:
            pass
        response = logic.add_player(name, role)
        if response == 'Ошибка':
            db.Static.delete_by_id(db.Static.select().where(db.Static.char_name == name))
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText('Персонаж не найден')
            msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText('Персонаж добавлен')
            msg_box.exec()
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUIMain()
    window.show()
    app.exec()


main()
