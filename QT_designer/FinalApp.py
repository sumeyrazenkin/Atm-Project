from PyQt5.QtWidgets import *
import json, csv, datetime, random, sys, os

from Ui_main_window import *
from Ui_customer_login_window import *
from Ui_customer_main_window import *
from Ui_admin_createCS_window import *
from Ui_admin_window import *
from Ui_customer_statement_window import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Main_Window(QMainWindow, Ui_open_window):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.openwdw_btn_CSLogin.clicked.connect(self.cslogin)
        self.openwdw_btn_ADLogin.clicked.connect(self.adlogin)
        self.openwdw_btn_exit.clicked.connect(self.close_w)
    def adlogin(self):
        self.admin = ADPreLogin()
        widget.addWidget(self.admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.admin.show() 
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
        self.adminwdw_btn_returnmain.clicked.connect(self.return_back)
        self.adminwdw_btn_exit.clicked.connect(self.close_w)
    def adafterlogin(self):
        AdminID = self.adminwdw_linedit_ADid.text()
        ADpassword = self.adminwdw_linedit_ADpassword.text()
        if len(AdminID) == 0 or len(ADpassword) == 0:
            self.adminwdw_lbl_warning.setText("Please fill the required fields!")
        else:
             
            file = resource_path("AdminLogInfo/admin.json")
            with open (file, "r") as f:
                pyfile = json.load(f)
            for admin in pyfile:
                if AdminID == admin["adminID"] and ADpassword == admin["adpassword"]:
                    print("Successfully logged in")
                    self.adminAfter = ADAfterLogin()
                    widget.addWidget(self.adminAfter)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    self.adminAfter.show()
                else:
                    self.adminwdw_lbl_warning.setText("Invalid ID or Password!")
    def return_back(self):
        main = Main_Window()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def close_w(self):
        sys.exit()  

class ADAfterLogin(QMainWindow, Ui_admin_CScreate_window):
    def __init__(self):
        super(ADAfterLogin, self).__init__()
        self.setupUi(self)
        self.admincswdw_btn_create.clicked.connect(self.createcustomer)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_CSpassword_2.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_name.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_email.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_spinBox_balance.clear)
        self.admincswdw_btn_returnmain.clicked.connect(self.return_back)
        self.admincswdw_btn_exit.clicked.connect(self.close_w)

    def createcustomer(self):
        CustomerID = random.randint(100000,999999)
        Name = self.admincswdw_linedit_name.text()
        Email = self.admincswdw_linedit_email.text()
        Password = self.admincswdw_linedit_CSpassword_2.text()
        CurrentBalance = self.admincswdw_spinBox_balance.text()
        if  len(Name) == 0 or len(Email) == 0 or len(Password) == 0:
            self.admincswdw_lbl_result.setText("Please fill all the fields!")
        if CustomerID and Name and Email and Password:
            file = resource_path("customer_database/customers.json")
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
                self.admincswdw_lbl_result.setText(f"NEW CUSTOMER CREATED:\n{CustomerID}")
                pyfile.append(customers)
            with open (file, "w") as f:
                json.dump(pyfile, f, indent=2)
            filepath = resource_path(f'customer_database/{CustomerID}.csv')
            with open(filepath,"w", newline="\n") as x:
                statement = csv.writer(x)
                statement.writerow(["Date", "Transaction Type", "Amount", "Current Balance"])
                statement.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"New Account", CurrentBalance, CurrentBalance])   # type: ignore
    def return_back(self):
            ADlogin = ADPreLogin()
            widget.addWidget(ADlogin)
            widget.setCurrentIndex(widget.currentIndex()+1)
    def close_w(self):
        sys.exit()  

class CsLogin(QMainWindow,Ui_customer_login_window):
    def __init__(self):
        super(CsLogin, self).__init__()
        self.setupUi(self)
        self.csloginwdw_btn_login.clicked.connect(self.csafterlogin)  
        self.csloginwdw_btn_returnmain.clicked.connect(self.return_back)
        self.csloginwdw_btn_exit.clicked.connect(self.close_w)

    def csafterlogin(self):
        self.CsId = self.csloginwdw_linedit_ADid.text()  
        self.CsPs = self.csloginwdw_linedit_ADpassword.text() 
        if len(self.CsId) == 0 or len(self.CsPs) == 0:
            self.csloginwdw_lbl_warning.setText("Please fill the required fields!")
        else:
            file = resource_path("customer_database/customers.json")
            with open (file, "r") as f:
                pyfile = json.load(f)
            for customer in pyfile:    
                if self.CsId == customer["Customer_ID"] and self.CsPs == customer["Password"]:
                    try:
                        CSMain.ID = self.CsId                        
                        print("Successfully logged in")
                        file = resource_path(f"customer_database/{self.CsId}.csv")
                        with open (file, "r") as f:
                            reader = csv.reader(f)
                            all_rows = list(reader)
                            last_row = all_rows[-1]
                            current_element = last_row[-1]
                            self.balance = current_element.split("€")[0]
                        with open (file, "a", newline="\n") as f:
                            writer = csv.writer(f)
                            writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Logged in", "N/A", str(self.balance)+"€"])
                        try:
                            self.csAfter = CSMain()
                            widget.addWidget(self.csAfter)
                            widget.setCurrentIndex(widget.currentIndex()+1)
                            self.csAfter.show()
                            self.csAfter.csmainwdw_lbl_CSname_show.setText(customer["Name"])
                            self.csAfter.csmainwdw_lbl_CSID_show.setText(customer["Customer_ID"])
                        except:
                            print("error")
                    except:
                        print("error")
                else:
                    self.csloginwdw_lbl_warning.setText("Invalid ID or Password!")
    def return_back(self):
            main = Main_Window()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def close_w(self):
        sys.exit()            

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)

        self.amount = self.csmainwdw_spinbox_money.value()
        self.ID
        
        file = resource_path(f"customer_database/{self.ID}.csv")
        with open (file, "r") as f:
            reader = csv.reader(f)
            all_rows = list(reader)
            last_row = all_rows[-1]
            current_element = last_row[-1]
            self.first_balance = current_element.split("€")[0]

        self.csmainwdw_lbl_balanceshow.setText(f"{str(self.first_balance)} €")
        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)
        self.csmainwdw_btn_returnmain.clicked.connect(self.return_back)
        self.csmainwdw_btn_statement.clicked.connect(self.show_statement)
        self.csmainwdw_btn_exit.clicked.connect(self.close_w)
        
    def take_balance(self):
        file = resource_path(f"customer_database/{self.ID}.csv")
        with open (file, "r") as f:
            reader = csv.reader(f)
            all_rows = list(reader)
            last_row = all_rows[-1]
            current_element = last_row[-1]
            self.balance = current_element.split("€")[0]
        
    def deposit(self):
        self.take_balance()
        try:
            if self.csmainwdw_spinbox_money.value() > 0:
                b = int(self.balance)
                b += self.csmainwdw_spinbox_money.value()
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                self.csmainwdw_lbl_resultmessage.setText("Successful deposit to the account")

                file = resource_path(f"customer_database/{self.ID}.csv")
                with open (file, "a", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Deposit", str(self.csmainwdw_spinbox_money.value())+"€", str(b)+"€"])
                    self.csmainwdw_lbl_balanceshow.setText(f"{str(b)} €")

            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Please enter an amount..")
        except:
            print("error")

    def get_cash(self):
        self.take_balance()
        try: 
            if self.csmainwdw_spinbox_money.value() > 0:
                c = int(self.balance)
                if c >= self.csmainwdw_spinbox_money.value():
                    c -= self.csmainwdw_spinbox_money.value()
                    self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                    self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account")
                    
                    file = resource_path(f"customer_database/{self.ID}.csv")
                    with open (file, "a", newline="\n") as f:
                        writer = csv.writer(f)
                        writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Withdraw", str(self.csmainwdw_spinbox_money.value())+"€", str(c)+"€"])
                        self.csmainwdw_lbl_balanceshow.setText(f"{str(c)} €")
                else:
                    self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                    self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Please enter an amount to withdraw..")
        except:
            pass
        
    def return_back(self):
        cslogin = CsLogin()
        widget.addWidget(cslogin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_statement(self):
        self.csstatement = CSinfo()
        widget.addWidget(self.csstatement)
        widget.setCurrentIndex(widget.currentIndex()+1)
        file = resource_path(f"customer_database/{self.ID}.csv")
        with open (file, "r") as f:
            reader = csv.reader(f)
            data = [row for row in reader]
            self.csstatement.csstatementwdw_tbl_statement.setRowCount(len(data)-1)
            self.csstatement.csstatementwdw_tbl_statement.setColumnCount(len(data[0]))
            for i, row in enumerate(data[1:]):
                for j, value in enumerate(row):
                    self.csstatement.csstatementwdw_tbl_statement.setItem(i, j, QTableWidgetItem(value))
        self.csstatement.show()
        self.take_balance()
        self.csstatement.csstatementwdw_lbl_balanceshow.setText(f"{self.balance} €")

    def close_w(self):
        sys.exit()  
        
class CSinfo(QMainWindow, Ui_customer_statement_window):
    def __init__(self):
        super(CSinfo, self).__init__()
        self.setupUi(self)
        self.csstatementwdw_btn_returnmain.clicked.connect(self.return_back)
        self.csstatementwdw_btn_exit.clicked.connect(self.close_w)

    def return_back(self):
        csmain = CSMain()
        widget.addWidget(csmain)
        widget.setCurrentIndex(widget.currentIndex()+1)
        csmain.csmainwdw_lbl_CSID_show.setText(csmain.ID)
        file = resource_path(f"customer_database/customers.json")
        f = open(file)
        data = json.load(f)
        for customer in data:
            if str(csmain.ID) in customer["Customer_ID"]:
                csmain.csmainwdw_lbl_CSname_show.setText(customer["Name"])

    def close_w(self):
        sys.exit()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    
    widget.addWidget(mainwindow)
    widget.setFixedHeight(700)
    widget.setFixedWidth(600)
    widget.show()

    try:
        sys.exit(app.exec_())

    except:
        print("Exiting")
    
