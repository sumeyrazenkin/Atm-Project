from PyQt5.QtWidgets import *
import sys
from Ui_main_window import *
from Ui_customer_login_window import *
import json
from Ui_customer_main_window import *


class Main_Window(QMainWindow, Ui_open_window):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.openwdw_btn_CSLogin.clicked.connect(self.cslogin)

        self.openwdw_btn_exit.clicked.connect(self.close_w)
    def cslogin(self):
        self.customer = CsLogin()
        widget.addWidget(self.customer)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.customer.show() 
    def close_w(self):
        sys.exit()    

class CsLogin(QMainWindow,Ui_customer_login_window):
    def __init__(self):
        super(CsLogin, self).__init__()
        self.setupUi(self)
        self.csloginwdw_btn_login.clicked.connect(self.csafterlogin)  

        self.csloginwdw_btn_exit.clicked.connect(self.close_l)
        #self.csloginwdw_btn_returnmain.clicked.connect(self.Main_Window)
        #self.csloginwdw_btn_returnmain.clicked.connect(Ui_customer_login_window.close)

    def csafterlogin(self):
        CsId = self.csloginwdw_linedit_ADid.text()  
        CsPs = self.csloginwdw_linedit_ADpassword.text() 
        if len(CsId) == 0 or CsPs == 0:
            self.csloginwdw_lbl_warning.setText("Please fill the required fields!")
        else:
            file = r"QT_designer/customer_database/customers.json"
            with open (file, "r") as f:
                pyfile = json.load(f)
            if CsId == pyfile[0]["Customer_ID"] and CsPs == pyfile[0]["Password"]:
                print("Successfully logged in")
                self.csAfter = CSMain()
                widget.addWidget(self.csAfter)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.csAfter.show()
            else:
                self.csloginwdw_lbl_warning.setText("Invalid ID or Password!")

    def close_l(self):
        sys.exit            

# class CSAfterLogin(QMainWindow, Ui_customer_main_window):
#     def __init__(self):
#         super(CSAfterLogin, self).__init__()
#         self.setupUi(self)

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)
        self.balance = 0

        self.update_balance_display()
        self.amount = int(self.csmainwdw_spinbox_money.value())
        
        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)
    
    def update_balance_display(self):
        self.csmainwdw_lbl_balanceshow.setText(f"{str(self.balance)} €")

    def deposit(self):
        self.balance += self.csmainwdw_spinbox_money.value()
        self.csmainwdw_lbl_resultmessage.setText("Successful deposit to the account..")
        self.update_balance_display()

    def get_cash(self):
        if self.balance >= self.csmainwdw_spinbox_money.value():
            self.balance -= self.csmainwdw_spinbox_money.value()
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
            self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account..")
            self.update_balance_display()
        else:
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")



if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(500)
    widget.show()
    sys.exit(app.exec_())
