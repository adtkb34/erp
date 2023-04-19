import sys

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from qt_subassembly import qTableWidgetItem, qAction


def f(orderFollowUp, fileWindow, part):
    ifBegin = False
    for rowExcel in range(1000):
        text = orderFollowUp.table.cell_value(rowExcel, 4)
        if text == f'{part} end':
            break
        if text == f'{part} begin':
            ifBegin = True
        if not ifBegin or text not in orderFollowUp.GroupBoxsInfoDist:
            continue
        uiTableWidgetName = text
        GroupBoxsInfoObject = orderFollowUp.GroupBoxsInfoDist[uiTableWidgetName]
        GroupBoxsInfoObject.initgroup(orderFollowUp, fileWindow, rowExcel)
        # init_lineEdit_combobox(GroupBoxsInfoObject)
        # init_tableWidgets(orderFollowUp, fileWindow, rowExcel, GroupBoxsInfoObject)


def init_lineEdit_combobox(GroupBoxsInfoObject):
    initDist = GroupBoxsInfoObject.initDist
    for idText, idDist in initDist.items():
        if 'combobox' in idDist:
            idDist['combobox'].activated[str].connect(
                lambda: combbox_currentIndexChanged(GroupBoxsInfoObject))
            # if initDist[idText]['ifLocked']:
            #     return
            valueList = ['']
            [valueList.append(x) for x in idDist['content'] if x not in valueList]
            idDist['combobox'].addItems(valueList)
            # initDist[idText]['ifLocked'] = True
        if 'lineEdit' in idDist:
            text = idDist['content'].tolist()[0]
            idDist['lineEdit'].setText(text)


def combbox_currentIndexChanged(GroupBoxsInfoObject):
    OBJECT = GroupBoxsInfoObject
    columnNum = OBJECT.columnNum
    currentLockRow = OBJECT.currentLockRow
    if currentLockRow == 0:
        return
    # textDist = {'ExistNone': False}
    for idText, idDist in OBJECT.initDist.items():
        if 'combobox' not in idDist:
            continue
        column = idDist['column']
        if column is None:
            continue
        text = idDist['combobox'].currentText()
        # textDist[idText] = text
        if text == '':
            # textDist['ExistNone'] = True
            continue
        List = OBJECT.tableWidgetList
        tableWidget = List[column // columnNum]
        qTableWidgetItem(text, tableWidget, currentLockRow, column % columnNum, Flags=True, TextAlignment=True)


def init_tableWidgets(orderFollowUp, mainWindow, rowExcel, GroupBoxsInfoObject):
    obj = GroupBoxsInfoObject
    initDist = obj.initDist
    columnNum = obj.columnNum
    tableName = obj.tableName
    allcolumnsDF = mainWindow.allUDFDist['t_all_columns'][
        mainWindow.allUDFDist['t_all_columns']['table_name'] == tableName]
    contentDF = orderFollowUp.allIDFDist[tableName]
    length = len(contentDF)
    addRowNum = length if length > 1 else 1
    if length < 1:
        contentDF = None
    for index, tableWidget in enumerate(obj.tableWidgetList):
        if not orderFollowUp.ifInitTableWidget and obj.ActionsContextMenuList:
            # qTableWidget 允许添加右击菜单
            tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
            if "锁定此行" in obj.ActionsContextMenuList:
                qAction(tableWidget, "锁定此行", lambda: lock(obj))
            if "添加一行" in obj.ActionsContextMenuList:
                qAction(tableWidget, "添加一行", lambda: addRows(obj))
            if "删除此行" in obj.ActionsContextMenuList:
                qAction(tableWidget, "删除此行", lambda: delRow(obj))

        # qTableWidget行高40
        tableWidget.verticalHeader().setDefaultSectionSize(obj.lineHeight)
        # qTableWidget列宽165
        tableWidget.horizontalHeader().setDefaultSectionSize(obj.columnWidth)
        # qTableWidget 水平拉齐， 列宽相同
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # qTableWidget 行数
        tableWidget.setRowCount(1)
        # qTableWidget 列数
        tableWidget.setColumnCount(columnNum)
        columnIndexList = []
        for column in range(index * columnNum, (index + 1) * columnNum):
            uiColumnText = orderFollowUp.table.cell_value(rowExcel + 3, column + 1)
            if uiColumnText == '' or uiColumnText == 'end':
                break
            # 界面字段
            qTableWidgetItem(uiColumnText, tableWidget, 0, column % columnNum, Flags=True, TextAlignment=True)
            # 字段编号对应的实际字段名
            idText = orderFollowUp.table.cell_value(rowExcel + 2, column + 1)
            if idText in initDist:
                initDist[idText]['column'] = column
                if 'tableWidget' in initDist[idText]:
                    addRowNum = initDist[idText]['length']
            obj.idList.append(idText)
            columnName = allcolumnsDF[allcolumnsDF['id'] == idText].iloc[0, 3]
            columnType = allcolumnsDF[allcolumnsDF['id'] == idText].iloc[0, 5]
            obj.columnNameList.append(columnName)
            obj.typeList.append(columnType)
            # 界面字段编号
            columnIndex = orderFollowUp.table.cell_value(rowExcel + 4, column + 1)
            columnIndexList.append(columnIndex)
        columnIndexList += [''] * (columnNum - len(columnIndexList))
        tableWidget.setHorizontalHeaderLabels(columnIndexList)
    addRows(GroupBoxsInfoObject, addRowNum, contentDF)
    # for index, tableWidget in enumerate(tableWidgetList):
    #     tableWidget.itemChanged.connect(lambda: check_the_input_information_type(self, uiTableWidgetName))
    # if 'ifItemChanged' in Dist:
    #     for index, tableWidget in enumerate(tableWidgetList):
    #         tableWidget.itemChanged.connect(lambda: testF(self, uiTableWidgetName))
    for index, tableWidget in enumerate(obj.tableWidgetList):
        tableWidget.itemChanged.connect(obj.tableWidget_itemChanged)


def lock(GroupBoxsInfoObject):
    obj = GroupBoxsInfoObject
    for tableWidget in obj.tableWidgetList:
        currentLockRow = tableWidget.currentRow()
        if currentLockRow > 0:
            obj.currentLockRow = currentLockRow
    for ID, IDDist in obj.initDist.items():
        if 'combobox' in IDDist:
            # combobox 显示空
            IDDist['combobox'].setCurrentIndex(0)


def addRows(GroupBoxsInfoObject, addRowNum=1, contentDF=None):
    obj = GroupBoxsInfoObject
    initDist = obj.initDist
    columnNum = obj.columnNum
    tableWidgetList = obj.tableWidgetList
    for tableWidget in tableWidgetList:
        tableWidget.setRowCount(obj.currentRowNum + addRowNum)
        tableWidget.setMinimumSize(0, obj.height + 40 * addRowNum)
    allColumnsNum = len(obj.idList)
    for row in range(addRowNum):
        for index, tableWidget in enumerate(tableWidgetList):
            for column in range(columnNum):
                if column + index * columnNum > allColumnsNum - 1:
                    break
                rowTableWidet = obj.currentRowNum + row
                columnName = obj.columnNameList[column + index * columnNum]
                text = '' if contentDF is None else contentDF[columnName].tolist()[row]
                idText = obj.idList[column + index * columnNum]
                ifsetFlags = False
                if idText in obj.initDist:
                    ifsetFlags = True
                    if 'lineEdit' in initDist[idText]:
                        text = initDist[idText]['content'].tolist()[0]
                    if 'tableWidget' in initDist:
                        text = initDist[idText]['content'].tolist()[row]
                qTableWidgetItem(text, tableWidget, rowTableWidet, column, Flags=ifsetFlags, TextAlignment=True)
    obj.currentRowNum += addRowNum
    obj.height += obj.lineHeight * addRowNum


def delRow(GroupBoxsInfoObject):
    obj = GroupBoxsInfoObject
    tableWidgetList = obj.tableWidgetList
    rowIndex = -1
    for tableWidget in tableWidgetList:
        if tableWidget.currentRow() != -1:
            rowIndex = tableWidget.currentRow()
            break
    for tableWidget in tableWidgetList:
        tableWidget.removeRow(rowIndex)
        tableWidget.setMinimumSize(0, obj.height - 40)
    obj.height -= 40
    obj.currentRowNum -= 1



