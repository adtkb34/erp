from PySide2 import QtCore
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


def qAction(ui, text,  function):
    """ 右键菜单 """
    option = QAction(ui)
    option.setText(text)
    option.triggered.connect(function)
    ui.addAction(option)


def qMessageBox(boxText, yesText='确定', noText='取消'):
    box = QMessageBox(QMessageBox.Question, '', boxText)
    yes = box.addButton(yesText, QMessageBox.YesRole)
    no = box.addButton(noText, QMessageBox.NoRole)
    box.exec_()
    return True if box.clickedButton() == yes else False


def qlistView(ui, qlist):
    slm = QStringListModel()
    slm.setStringList(qlist)
    ui.listView.setModel(slm)


class progressBar:
    def __init__(self, length):
        self.window = QMainWindow()
        self.window.resize(400, 400)

        self.progressBar = QProgressBar(self.window)
        self.progressBar.resize(300, 20)
        self.progressBar.move(80, 0)
        # 进度是 0 - 5，
        self.progressBar.setRange(0, length)


def qTableWidgetItem(text, tableWidget, row, column, Flags=False, TextAlignment=False):
    item = QTableWidgetItem(text)
    if Flags:
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    if TextAlignment:
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    tableWidget.setItem(row, column, item)
