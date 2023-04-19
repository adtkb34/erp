import os
import time

import PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from accountApp.views import login
from documentHandingApp.views import fileWindow


dirname = os.path.dirname(PySide2.__file__)
# dirname = 'E:\\桌面文件\\gcst_project\\venv\\lib\\site-packages\\PySide2'

plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon('./view/图片/k.png'))
    a = time.time()
    # LoginUI = login.LoginUI()
    # LoginUI.ui.show()
    fileWindowUI = fileWindow.fileWindowUI()
    fileWindowUI.ui.show()
    b = time.time()
    print(b - a)
    app.exec_()


if __name__ == '__main__':
    main()

