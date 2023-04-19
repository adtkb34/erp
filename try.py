class C:
    def __init__(self):
        # tableWidget里的属性
        self.height = 74
        self.lineHeight = 40
        self.columnWidth = 165
        self.columnNum = 5
        self.currentRowNum = 1
        self.currentLockRow = 1
        # self.tableName = tableName
        self.typeList = []
        self.idList = []
        self.columnNameList = []
#
#
# class CUSTOMS_DECLARANCE_SHIPMENT(C):
#     def __init__(self):
#         C.__init__(self)
#         self.tableName = 't_shipment',
#         self.ActionsContextMenuList = 1,
#
#     def tableWidget_itemChanged(self):
#         pass
#
# A = CUSTOMS_DECLARANCE_SHIPMENT()
# print(A.tableName)
class Father():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dev(self):
        return self.a - self.b


# 调用父类初始化参数a,b并增加额外参数c
class CUSTOMS_DECLARANCE_SHIPMENT(C):
    def __init__(self):  # 固定值： 例如默认c=10，也可以显示地将c赋值
        C.__init__(self)
        self.tableName = 't_shipment',


son = CUSTOMS_DECLARANCE_SHIPMENT()  # 由于c在初始化过程中默认为10，所以c可以不用显示表达出来
print(son.c)  # 调用父类dev函数