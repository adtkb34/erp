def check_orderCode(self):
    """ treeWidget 点击 ‘打开 order_follow_up’ 核对该文件夹名称是否为已存在的订单号 """
    orderCode = self.ui.treeWidget.currentItem().text(0)
    if self.orderDF[self.orderDF['code'] == orderCode].empty:
        return
    tableWidgetIndex = self.ui.tabWidget.count()
    self.order_follow_up_ui_show(orderCode, tableWidgetIndex)
