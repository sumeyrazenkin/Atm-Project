from PyQt5.QtWidgets import *
from Ui_main_window import Ui_open_window
from customer_login_python import CsLogin_window

class MainwindowPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainwdwform = Ui_open_window
        self.mainwdwform.setupUi(self)
        self.openloginwdw = CsLogin_window
        self.mainwdwform.openwdw_btn_CSLogin.clicked(self.Cslogin)

    def Cslogin(self):
        pass    


app = QApplication([])
window = Login_window()
window.show()
app.exec_()
