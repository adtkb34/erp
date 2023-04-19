from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from PySide2.QtGui import *

from settings import STATIC_URL
from dao.mysql import *
from accountApp.controller.login import check_account
from documentHandingApp.views import fileWindow
# from view import enroll, main_window


class LoginUI:
    def __init__(self):
        self.fileWindowUI = None
        self.usersInfoDF = select('user')
        qfile_login = QFile('./accountApp/templates/Login.ui')
        qfile_login.open(QFile.ReadOnly)
        qfile_login.close()
        self.ui = QUiLoader().load(qfile_login)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.photo.setPixmap(QPixmap(f'./accountApp/{STATIC_URL}/img/gcst.png'))
        self.ui.login_button.clicked.connect(lambda: check_account(self))
        # self.ui.enroll_button.clicked.connect(self.enrollUIShow)
        # 创建快捷键
        # self.ui.login_button.setShortcut('Enter')

    def account_correct(self):
        self.ui.close()
        self.fileWindowUI = fileWindow.fileWindowUI()
        self.fileWindowUI.ui.show()
