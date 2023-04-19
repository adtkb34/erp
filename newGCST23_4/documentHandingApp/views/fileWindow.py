import os

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *

from dao import mysql
import qt_subassembly
from settings import STATIC_URL, DYNAMIC_URL
from documentHandingApp.views import orderFollowUp
from documentHandingApp.controller import fileWindow


class fileWindowUI:
    def __init__(self):
        self.initUDF = False
        self.OrderFollowUp = None
        self.folderPath = f"./documentHandingApp/{DYNAMIC_URL}/file/"
        qfile_module = QFile('./documentHandingApp/templates/file_window.ui')
        qfile_module.open(QFile.ReadOnly)
        qfile_module.close()
        self.ui = QUiLoader().load(qfile_module)
        self.ui.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.ui.treeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.init_treeWidget()

        self.select_all_DF()
        qt_subassembly.qAction(self.ui.treeWidget, "打开 order_follow_up",
                               lambda: fileWindow.check_orderCode(self))

    def closeTab(self, index):
        self.ui.tabWidget.removeTab(index)

    def init_treeWidget(self):
        self.find_file_recursion(self.folderPath, self.ui.treeWidget)
        pass

    def find_file_recursion(self, folderPath, parent):
        """ 去把file文件夹下的所有文件都搜寻到 方法：递归 """
        files = os.listdir(folderPath)
        if not files:
            return
        for file in files:
            child = QTreeWidgetItem(parent)
            child.setText(0, file)
            filetype = os.path.splitext(f'./{folderPath}/{file}')[-1]
            print(filetype)
            fileImgPath = None
            if not filetype:
                fileImgPath = f'./documentHandingApp/{STATIC_URL}/img/文件夹.png'
            elif filetype == '.pdf':
                fileImgPath = f'./documentHandingApp/{STATIC_URL}/img/pdf.png'
            elif filetype == '.xlsx':
                fileImgPath = f'./documentHandingApp/{STATIC_URL}/img/excel.png'
            if fileImgPath:
                child.setIcon(0, QIcon(fileImgPath))
            if not filetype:
                self.find_file_recursion(f'./{folderPath}/{file}', child)

    def select_all_DF(self):
        if not self.initUDF:
            self.allUDFDist = {
                't_all_columns': mysql.select('t_all_columns'),
                't_inspection_com': mysql.select('t_inspection_com')[1:],
                't_forwarder': mysql.select('t_forwarder')[1:],
                't_shipping_line': mysql.select('t_shipping_line')[1:],
                't_loading_port': mysql.select('t_loading_port')[1:],
                't_customer': mysql.select('t_customer')[1:],
                't_commodity': mysql.select('t_commodity')[1:],
                't_supplier': mysql.select('t_supplier')[1:]
            }
            self.initUDF = True

        self.orderDF = mysql.select('t_order')
        self.orderPContractDF = mysql.select('t_order_p_contract')
        self.orderPCCommodityDF = mysql.select('t_order_pc_commodity')
        self.shipmentDF = mysql.select('t_shipment')
        self.containerDF = mysql.select('t_container')
        self.containerCommodityDF = mysql.select('t_container_commodity')
        self.deliveryNoteDF = mysql.select('t_delivery_note')
        self.dnCommodityDF = mysql.select('t_dn_commodity')
        self.dnPCDF = mysql.select('t_dn_pc')
        self.usdPaymentDF = mysql.select('t_usd_payment')
        self.pContractPaymentDF = mysql.select('t_p_contract_payment')
        self.commissionDF = mysql.select('t_commission')

    def order_follow_up_ui_show(self, orderCode, tableWidgetIndex):
        self.OrderFollowUp = orderFollowUp.OrderFollowUpUI(self, tableWidgetIndex, orderCode)
        self.ui.tabWidget.addTab(self.OrderFollowUp.ui, orderCode)
        self.ui.tabWidget.setCurrentIndex(tableWidgetIndex)

