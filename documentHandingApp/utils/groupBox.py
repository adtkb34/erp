# class C:
#     def __init__(self, tableName, tableWidgetList, ActionsContextMenuList, initDist):
#     # def __init__(self, UI):
#         # tableWidget里的属性
#         self.height = 74
#         self.lineHeight = 40
#         self.columnWidth = 165
#         self.columnNum = 5
#         self.currentRowNum = 1
#         self.currentLockRow = 1
#         self.tableName = tableName
#         self.typeList = []
#         self.idList = []
#         self.columnNameList = []
#         self.tableWidgetList = tableWidgetList
#         self.ActionsContextMenuList = ActionsContextMenuList
#         self.initDist = initDist
#         # self.itemChangedValue = itemChangedValue
#         # self.itemChangedDist = itemChangedDist
import pandas as pd

from documentHandingApp.utils.initAllGroups import init_lineEdit_combobox, init_tableWidgets

class C:
    def __init__(self):
        # tableWidget里的属性
        self.height = 74
        self.lineHeight = 40
        self.columnWidth = 165
        self.columnNum = 5
        self.currentRowNum = 1
        self.currentLockRow = 1
        self.typeList = []
        self.idList = []
        self.columnNameList = []

    def t_shipment_11_num_type(self, orderFollowUp):
        declared_qty_container_type = orderFollowUp.allIDFDist['t_shipment']['declared_qty_container_type'].tolist()
        if declared_qty_container_type in [[], ['']]:
            Num, typeList = 0, []
        else:
            Num = sum(map(int, [x[0] for x in declared_qty_container_type[0].split('+')]))
            typeList = [x[2:] for x in declared_qty_container_type[0].split('+')]
        return {'Num': Num, 'typeSeries': pd.Series(typeList)}

    def initgroup(self, orderFollowUp, fileWindow, rowExcel):
        init_lineEdit_combobox(self)
        init_tableWidgets(orderFollowUp, fileWindow, rowExcel, self)
