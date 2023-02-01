from PyQt5.QtWidgets import *
import sys
from Ui_main_window import *
from Ui_admin_window import *
# from Ui_admin_createCS_window import *

class Main_Window(QMainWindow, Ui_open_window):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.openwdw_btn_ADLogin.clicked.connect(self.adlogin)
    def adlogin(self):
        self.admin = ADPreLogin()
        widget.addWidget(self.admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.admin.show()
        
        
    
class ADPreLogin(QMainWindow, Ui_admin_window):
    def __init__(self):
        super(ADPreLogin, self).__init__()
        self.setupUi(self)
        
#         self.adminwdw_btn_login.clicked.connect(self.adafterlogin)
#     def adafterlogin(self):
#         self.after = ADAfterLogin()
#         self.after.show()

# class ADAfterLogin(QMainWindow, Ui_admin_window):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(500)
    widget.show()
    sys.exit(app.exec_())
