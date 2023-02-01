from PyQt5.QtWidgets import *
from Ui_customer_login_window import *
from  main_window_python import MainwindowPage
import sys
import json

class CsLogin_window(QMainWindow,Ui_customer_login_window):
    def __init__(self):
        super(CsLogin_window,self).__init__()
        self.setupUi(self)
        self.loginform = Ui_customer_login_window()
        self.loginform.setupUi(self)
        self.openmainwindow = MainwindowPage()#melikenin penceresi yazılacak
        self.loginform.csloginwdw_btn_login.clicked.connect(self.login)
    def login(self):
        cıd = self.loginform.csloginwdw_linedit_ADid.text()
        pas = self.loginform.csloginwdw_linedit_ADpassword.text()
        with open("customers.json") as f:
          data = json.load(f)
        #self.openmainwindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cslwd = CsLogin_window()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(cslwd)
    widget.show()
    sys.exit(app.exec_())