import pandas as pd
from xlrd import open_workbook
from PySide2.QtCore import *
from PySide2.QtUiTools import *

import qt_subassembly
from settings import STATIC_URL, ORDER_HOME_PAGE
from documentHandingApp.utils import save, refurbish, groupBox, initAllGroups


class OrderFollowUpUI:
    def __init__(self, fileWindow, tableWidgetIndex, orderCode):
        self.initGroupBoxDist = None
        qfile_contract = QFile('./documentHandingApp/templates/Order_follow_up.ui')
        qfile_contract.open(QFile.ReadOnly)
        qfile_contract.close()
        self.ui = QUiLoader().load(qfile_contract)

        self.tabWidget = fileWindow.ui.tabWidget
        obj = groupBox.C()
        self.tabWidget.setMinimumSize(obj.columnWidth * obj.columnNum + 450, 0)

        self.orderCode = orderCode
        self.table = open_workbook(f'./documentHandingApp/{STATIC_URL}/file/{ORDER_HOME_PAGE}').sheet_by_index(0)

        self.ifInitTableWidget = False  # 如果为True qAction不再重复添加
        qt_subassembly.qAction(self.ui, "仅保存数据         ", lambda: save.f(self, fileWindow, '仅保存数据'))
        qt_subassembly.qAction(self.ui, "保存并生成文件         ", lambda: save.f(self, fileWindow, '保存并生成文件'))
        qt_subassembly.qAction(self.ui, "刷新         ", lambda: refurbish.f(fileWindow, tableWidgetIndex, orderCode))
        self.select_all_DF(fileWindow)
        self.GroupBoxsInfoDist = {
            'CUSTOMS DECLARANCE - SHIPMENT': CUSTOMS_DECLARANCE_SHIPMENT(fileWindow, self),
            'CD - CONTAINER - COMMODITY': CD_CONTAINER_COMMODITY(fileWindow, self),

        }
        initAllGroups.f(self, fileWindow, 'second part')

    def select_all_DF(self, fileWindow):
        self.allIDFDist = {
            't_order': fileWindow.orderDF[fileWindow.orderDF['code'] == self.orderCode],
            't_order_p_contract': fileWindow.orderPContractDF[
                fileWindow.orderPContractDF['order_code'] == self.orderCode],
            't_order_pc_commodity': fileWindow.orderPCCommodityDF[
                fileWindow.orderPCCommodityDF['order_code'] == self.orderCode],
            't_shipment': fileWindow.shipmentDF[fileWindow.shipmentDF['order_code'] == self.orderCode],
            't_container': fileWindow.containerDF[fileWindow.containerDF['order_code'] == self.orderCode],
            't_container_commodity': fileWindow.containerCommodityDF[
                fileWindow.containerCommodityDF['order_code'] == self.orderCode],
            't_delivery_note': fileWindow.deliveryNoteDF[fileWindow.deliveryNoteDF['order_code'] == self.orderCode],
            't_dn_commodity': fileWindow.dnCommodityDF[fileWindow.dnCommodityDF['order_code'] == self.orderCode],
            't_dn_pc': fileWindow.dnPCDF[fileWindow.dnPCDF['order_code'] == self.orderCode],
            't_usd_payment': fileWindow.usdPaymentDF[fileWindow.usdPaymentDF['order_code'] == self.orderCode],
            't_p_contract_payment': fileWindow.pContractPaymentDF[
                fileWindow.pContractPaymentDF['order_code'] == self.orderCode],
            't_commission': fileWindow.commissionDF
        }


class CUSTOMS_DECLARANCE_SHIPMENT(groupBox.C):
    def __init__(self, fileWindow, orderFollowUp):
        super().__init__()
        self.ui = orderFollowUp.ui
        self.tableName = 't_shipment'
        self.tableWidgetList = [self.ui.CUSTOMS_DECLARANCE_SHIPMENT,
                                self.ui.CUSTOMS_DECLARANCE_SHIPMENT2,
                                self.ui.CUSTOMS_DECLARANCE_SHIPMENT3,
                                self.ui.CUSTOMS_DECLARANCE_SHIPMENT4]
        self.ActionsContextMenuList = None
        self.initDist = {
            't_shipment_7': {
                'lineEdit': self.ui.t_order_3,
                'content': orderFollowUp.allIDFDist['t_order']['customer_code'],
                'length': 1,
                'column': None, 'ifLocked': False},
            't_shipment_29': {
                'combobox': self.ui.t_loading_port_0,
                'content': fileWindow.allUDFDist['t_loading_port']['code'],
                'length': 'unknow',
                'column': None, 'ifLocked': False},
            't_shipment_32': {
                'combobox': self.ui.t_order_p_contract_2,
                'content': orderFollowUp.allIDFDist['t_order_p_contract']['supplier_code'],
                'length': 'unknow',
                'column': None, 'ifLocked': False}
        }

    def tableWidget_itemChanged(self):
        print(11111111111)
        pass


class CD_CONTAINER_COMMODITY(groupBox.C):
    def __init__(self, fileWindow, orderFollowUp):
        super().__init__()
        self.ui = orderFollowUp.ui
        self.tableName = 't_container_commodity'
        self.tableWidgetList = [self.ui.CD_CONTAINER_COMMODITY]
        self.ActionsContextMenuList = ['锁定此行', '添加一行', '删除此行']
        self.containerNumTypeDist = super().t_shipment_11_num_type(orderFollowUp)
        self.initDist = {}

    def tableWidget_itemChanged(self):
        pass

    def initgroup(self, *args):
        print(11)
# self.initWidgetDist = {
#     'widgetTableColumnNum': 5,
#     'CUSTOMS DECLARANCE - SHIPMENT': {
#         'ifItemChanged': {'': ['CD - CONTAINER - COMMODITY', 'dist', 't_container_commodity_2']},
#         'dist': {
#             't_shipment_7': {'lineEdit': self.ui.t_order_3,
#                              'content': self.allIDFDist['t_order']['customer_code'],
#                              'length': 1,
#                              'column': None, 'ifLocked': False},
#             't_shipment_29': {'combobox': self.ui.t_loading_port_0,
#                               'content': mainWindow.allUDFDist['t_loading_port']['code'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False},
#             't_shipment_32': {'combobox': self.ui.t_order_p_contract_2,
#                               'content': self.allIDFDist['t_order_p_contract']['supplier_code'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False}
#         },
#         'tableWidgetList': [self.ui.CUSTOMS_DECLARANCE_SHIPMENT,
#                             self.ui.CUSTOMS_DECLARANCE_SHIPMENT2,
#                             self.ui.CUSTOMS_DECLARANCE_SHIPMENT3,
#                             self.ui.CUSTOMS_DECLARANCE_SHIPMENT4],
#
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': False,
#         'ActionsContextMenuList': None,
#         'tableName': 't_shipment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_shipment'],
#         'currentLockRow': 1
#     },
#
#     'CD - CONTAINER - COMMODITY': {
#         'dist': {
#             't_container_commodity_2': {'combobox': self.ui.t_container_commodity_combobox,
#                                         'content': pd.Series([chr(x + 65) for x in
#                                                               range(int(containerNumTypeDist['Num']))]),
#                                         'length': 'unknow',
#                                         'column': None, 'ifLocked': False},
#             't_container_commodity_4': {'combobox': self.ui.t_order_commodity_1,
#                                         'content': self.allIDFDist['t_order_pc_commodity']['commodity_code'],
#                                         'length': 'unknow',
#                                         'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.CD_CONTAINER_COMMODITY],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行', '添加一行', '删除此行'],
#         'tableName': 't_container_commodity',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_container_commodity'],
#         'currentLockRow': 0
#
#     },
#     'DELIVERY NOTE': {
#         'dist': {},
#         'ifItemChanged': {'code': ['DN - PC', 'dist', 't_dn_pc_0']},
#         'tableWidgetList': [self.ui.DELIVERY_NOTE,
#                             self.ui.DELIVERY_NOTE2],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行', '添加一行', '删除此行'],
#         'tableName': 't_delivery_note',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_delivery_note'],
#         'currentLockRow': 0
#
#     },
#     'DN - PC': {
#         'dist': {
#             't_dn_pc_0': {'combobox': self.ui.t_delivery_note_0,
#                           'content': self.allIDFDist['t_delivery_note']['code'],
#                           'length': 'unknow',
#                           'srcColumnName': 'delivery_note_code',
#                           'column': None, 'ifLocked': False},
#             't_dn_pc_1': {'combobox': self.ui.t_order_p_contract_0,
#                           'content': self.allIDFDist['t_order_p_contract']['code'],
#                           'length': 'unknow',
#                           'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.DN_PC],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行', '添加一行', '删除此行'],
#         'tableName': 't_dn_pc',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_dn_pc'],
#         'currentLockRow': 0
#
#     },
#     'DN - COMMODITY': {
#         'tableWidgetType': 'B',
#         'dist': {
#             # 't_dn_commodity_0': {'tableWidget': None,
#             #                      'content': DNCodeCCodeDist['DNCode'],
#             #                      'length': DNCodeCCodeDist['length'],
#             #                      'column': None, 'ifLocked': False},
#             # 't_dn_commodity_1': {'tableWidget': None,
#             #                      'content': DNCodeCCodeDist['CCode'],
#             #                      'length': DNCodeCCodeDist['length'],
#             #                      'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.DN_COMMODITY],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': [],
#         'tableName': 't_dn_commodity',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_dn_commodity'],
#         'currentLockRow': 0
#
#     },
#     'PRE-SHIPMENT INSPECTION': {
#         'dist': {
#             't_shipment_16': {'combobox': self.ui.t_inspection_com_0,
#                               'content': mainWindow.allUDFDist['t_inspection_com']['code'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.PRE_SHIPMENT_INSPECTION,
#                             self.ui.PRE_SHIPMENT_INSPECTION2,
#                             self.ui.PRE_SHIPMENT_INSPECTION3],
#
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': False,
#         'ActionsContextMenuList': None,
#         'tableName': 't_shipment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_shipment'],
#         'currentLockRow': 1
#
#     },
#     # # 'EXPORT INSURANCE': [[self.ui.EXPORT_INSURANCE]],
#     #
#     'FORWARDER FEE': {
#         'dist': {
#             't_shipment_12': {'lineEdit': self.ui.t_shipment_11num,
#                               'content': pd.Series([str(containerNumTypeDist['Num'])]),
#                               'length': 1,
#                               'column': None, 'ifLocked': False},
#             't_shipment_44': {'combobox': self.ui.t_forwarder_0,
#                               'content': mainWindow.allUDFDist['t_forwarder']['code'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.FORWARDER_FEE,
#                             self.ui.FORWARDER_FEE2],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': False,
#         'ActionsContextMenuList': None,
#         'tableName': 't_shipment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_shipment'],
#         'currentLockRow': 1
#
#     },
#     'BOOKING - SHIPMENT': {
#         'dist': {
#             't_shipment_30': {'combobox': self.ui.t_shipping_line_0,
#                               'content': mainWindow.allUDFDist['t_shipping_line']['code'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.BOOKING_SHIPMENT,
#                             self.ui.BOOKING_SHIPMENT2],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': False,
#         'ActionsContextMenuList': None,
#         'tableName': 't_shipment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_shipment'],
#         'currentLockRow': 1
#
#     },
#     'BOOKING - CONTAINER': {
#         'dist': {
#             't_container_0': {'tableWidget': None,
#                               'content': pd.Series([chr(x + 65) for x in
#                                                     range(int(containerNumTypeDist['Num']))]),
#                               'length': containerNumTypeDist['Num'],
#                               'column': None, 'ifLocked': False},
#             't_container_3': {'combobox': self.ui.t_shipment_11type,
#                               'content': containerNumTypeDist['typeSeries'],
#                               # 'content': containerNumTypeDist['typeSeries'],
#                               'length': 'unknow',
#                               'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.BOOKING_CONTAINER,
#                             self.ui.BOOKING_CONTAINER2],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行'],
#
#         'tableName': 't_container',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_container'],
#         'currentLockRow': 0
#     },
#     'CD - CONTAINERS': {
#         'dist': {
#             't_container_0': {'tableWidget': None,
#                               'content': pd.Series([chr(x + 65) for x in
#                                                     range(int(containerNumTypeDist['Num']))]),
#                               'length': containerNumTypeDist['Num'],
#                               'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.CD_CONTAINERS,
#                             self.ui.CD_CONTAINERS2],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行'],
#         'tableName': 't_container',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_container'],
#         'currentLockRow': 0
#
#     },
#     'USD PAYMENTS': {
#         'dist': {},
#         'tableWidgetList': [self.ui.USD_PAYMENTS,
#                             self.ui.USD_PAYMENTS2,
#                             self.ui.USD_PAYMENTS3,
#                             self.ui.USD_PAYMENTS4],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行', '添加一行', '删除此行'],
#         'tableName': 't_usd_payment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_usd_payment'],
#         'currentLockRow': 0
#
#     },
#     'PC PAYMENTS': {
#         'dist': {
#             't_p_contract_payment_1': {'combobox': self.ui.t_order_p_contract_0_1,
#                                        'content': self.allIDFDist['t_order_p_contract']['code'],
#                                        'length': 'unknow',
#                                        'column': None, 'ifLocked': False},
#         },
#         'tableWidgetList': [self.ui.PC_PAYMENTS],
#         'height': 74,
#         'currentRowNum': 1,
#         'ifActionsContextMenu': True,
#         'ActionsContextMenuList': ['锁定此行', '添加一行', '删除此行'],
#         'tableName': 't_p_contract_payment',
#         'columnNameList': [],
#         'typeList': [],
#         'contentDF': self.allIDFDist['t_p_contract_payment'],
#         'currentLockRow': 0
#     },
# }
