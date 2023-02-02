from PyQt5.QtWidgets import *
import sys
from Ui_main_window import *
from Ui_admin_window import *
import json
from Ui_admin_createCS_window import *

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
        self.adminwdw_btn_login.clicked.connect(self.adafterlogin)
    def adafterlogin(self):
        AdminID = self.adminwdw_linedit_ADid.text()
        ADpassword = self.adminwdw_linedit_ADpassword.text()
        if len(AdminID) == 0 or ADpassword == 0:
            self.adminwdw_lbl_warning.setText("Please fill the required fields!")
        else:
            file = r"QT_designer\AdminLogInfo\admin.json"
            with open (file, "r") as f:
                pyfile = json.load(f)
            if AdminID == pyfile[0]["adminID"] and ADpassword == pyfile[0]["adpassword"]: #buraya bir for dongusu yazilarak baska adminler icin giris yapilmasi saglanabilir.
                print("Successfully logged in")
                self.adminAfter = ADAfterLogin()
                widget.addWidget(self.adminAfter)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.adminAfter.show()
            else:
                self.adminwdw_lbl_warning.setText("Invalid ID or Password!")

class ADAfterLogin(QMainWindow, Ui_admin_CScreate_window):
    def __init__(self):
        super(ADAfterLogin, self).__init__()
        self.setupUi(self)
        self.admincswdw_btn_create.clicked.connect(self.createcustomer)
    def createcustomer(self):
        CustomerID = self.admincswdw_linedit_CSid.text()
        Name = self.admincswdw_linedit_name.text()
        Email = self.admincswdw_linedit_email.text()
        Password = self.admincswdw_linedit_CSpassword_2.text()
        CurrentBalance = self.admincswdw_spinBox_balance.text()
        if CustomerID and Name and Email and Password:
            file = "QT_designer\customer_database\customers.json"
            customers = {}
            with open (file, "r") as f:
                pyfile = json.load(f)
            customers["Customer_ID"] = int(CustomerID)
            customers["Name"] = Name
            customers["Email"] = Email
            customers["Password"] = Password
            customers["Current Balance"] = CurrentBalance
            pyfile.append(customers)
        
            with open (file, "w") as f:
                json.dump(pyfile, f, indent=2)




if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(500)
    widget.show()
    sys.exit(app.exec_())

