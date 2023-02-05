from PyQt5.QtWidgets import *
import sys
from Ui_main_window import *
from Ui_customer_login_window import *
import json, csv, datetime, random
from Ui_customer_main_window import *
from Ui_admin_createCS_window import *
from Ui_admin_window import *
from Ui_customer_statement_window import *


class Main_Window(QMainWindow, Ui_open_window):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.openwdw_btn_CSLogin.clicked.connect(self.cslogin)
        self.openwdw_btn_ADLogin.clicked.connect(self.adlogin)
    def adlogin(self):
        self.admin = ADPreLogin()
        widget.addWidget(self.admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.admin.show() 

        self.openwdw_btn_exit.clicked.connect(self.close_w)
    def cslogin(self):
        self.customer = CsLogin()
        widget.addWidget(self.customer)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.customer.show() 
    def close_w(self):
        sys.exit()  

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
            file = r"QT_designer/AdminLogInfo/admin.json"
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

        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_CSid.clear) # type: ignore
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_CSpassword_2.clear) # type: ignore
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_name.clear) # type: ignore
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_email.clear) # type: ignore
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_spinBox_balance.clear)
    def createcustomer(self):
        CustomerID = random.randint(100000,999999)
        Name = self.admincswdw_linedit_name.text()
        Email = self.admincswdw_linedit_email.text()
        Password = self.admincswdw_linedit_CSpassword_2.text()
        CurrentBalance = self.admincswdw_spinBox_balance.text()
        if CustomerID and Name and Email and Password:
            file = "QT_designer/customer_database/customers.json"
            customers = {}
            with open (file, "r") as f:
                pyfile = json.load(f)
            customers["Customer_ID"] = str(CustomerID)
            customers["Name"] = Name
            customers["Email"] = Email
            customers["Password"] = Password
            customers["Opening Balance"] = CurrentBalance
            customers["Current Balance"] = CurrentBalance
            try:
                for customer in pyfile:
                    if str(CustomerID) in customer["Customer_ID"]:
                        raise Exception("There is already a customer with the same ID")
            except Exception():
                pass
            else:
                pyfile.append(customers)
            with open (file, "w") as f:
                json.dump(pyfile, f, indent=2)
            with open(f'QT_designer/customer_database/{CustomerID}.csv',"w", newline="\n") as x:
                statement = csv.writer(x)
                statement.writerow(["Date", "Transaction Type", "Amount", "Current Balance"])
                statement.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Account Created", CurrentBalance, CurrentBalance])   # type: ignore

class CsLogin(QMainWindow,Ui_customer_login_window):
    def __init__(self):
        super(CsLogin, self).__init__()
        self.setupUi(self)
        self.csloginwdw_btn_login.clicked.connect(self.csafterlogin)  

        self.csloginwdw_btn_exit.clicked.connect(self.close_l)
        # self.csloginwdw_btn_returnmain.clicked.connect(self.Main_Window)
        #self.csloginwdw_btn_returnmain.clicked.connect(Ui_customer_login_window.close)

    def csafterlogin(self):
        self.CsId = self.csloginwdw_linedit_ADid.text()  
        self.CsPs = self.csloginwdw_linedit_ADpassword.text() 
        if len(self.CsId) == 0 or len(self.CsPs) == 0:
            self.csloginwdw_lbl_warning.setText("Please fill the required fields!")
        else:
            file = r"QT_designer/customer_database/customers.json"
            with open (file, "r") as f:
                pyfile = json.load(f)
            for customer in pyfile:    
                if self.CsId in customer["Customer_ID"] and self.CsPs in customer["Password"]:
                    CSMain.ID = self.CsId
                    print("Successfully logged in")
                    with open('QT_designer/customer_database/loggedincustomer.csv',"w+", newline="\n") as x:
                        statement = csv.writer(x)
                        statement.writerow(["The Customer"])
                        statement.writerow([self.CsId])
                    x.close()
                    self.csAfter = CSMain()
                    widget.addWidget(self.csAfter)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    self.csAfter.show()
                    self.csAfter.csmainwdw_lbl_CSname_show.setText(customer["Name"])
                    self.csAfter.csmainwdw_lbl_CSID_show.setText(customer["Customer_ID"])
                else:
                    self.csloginwdw_lbl_warning.setText("Invalid ID or Password!")

    def close_l(self):
        sys.exit            

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)
        self.balance = self.csmainwdw_lbl_balanceshow.text()
        self.ID
        self.take_balance()
        self.balance
        self.amount = self.csmainwdw_spinbox_money.value()

        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)

        self.csmainwdw_btn_statement.clicked.connect(self.show_statement)
        
    def take_balance(self):
        file = f"QT_designer/customer_database/{self.ID}.csv"
        with open (file, "r") as f:
            reader = csv.reader(f)
            all_rows = list(reader)
            last_row = all_rows[-1]
            current_element = last_row[-1]
            current_balance = current_element.split("€")[0]
            self.balance = current_balance
            self.csmainwdw_lbl_balanceshow.setText(f"{str(self.balance)} €")
        
    def deposit(self):
        if self.csmainwdw_spinbox_money.value() > 0:
            b = int(self.balance)
            b += self.csmainwdw_spinbox_money.value()
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
            self.csmainwdw_lbl_resultmessage.setText("Successful deposit to the account")

            file = f"QT_designer/customer_database/{self.ID}.csv"
            with open (file, "a") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Money Deposit", self.csmainwdw_spinbox_money.value(), b])
                self.take_balance()
                self.csmainwdw_lbl_balanceshow.setText(f"{str(b)} €")

        else:
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.csmainwdw_lbl_resultmessage.setText("Please enter an amount..")

    def get_cash(self):
        if self.csmainwdw_spinbox_money.value() > 0:
            b = int(self.balance)
            if b >= self.csmainwdw_spinbox_money.value():
                b -= self.csmainwdw_spinbox_money.value()
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account")
                
                file = f"QT_designer/customer_database/{self.ID}.csv"
                with open (file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Money Withdraw", self.csmainwdw_spinbox_money.value(), b])
                    self.take_balance()
                    self.csmainwdw_lbl_balanceshow.setText(f"{str(b)} €")
            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

        else:
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.csmainwdw_lbl_resultmessage.setText("Please enter an amount to withdraw..")
    
    def show_statement(self):
        self.csstatement = CSinfo()
        widget.addWidget(self.csstatement)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.csstatement.show()

class CSinfo(QMainWindow, Ui_customer_statement_window):
    def __init__(self):
        super(CSinfo, self).__init__()
        self.setupUi(self)
        
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(500)
    widget.show()
    sys.exit(app.exec_())
