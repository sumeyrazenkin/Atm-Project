import sys
from PyQt5.QtWidgets import *
from Ui_customer_main_window import *
import json

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)
        
        self.balance = 0
        self.update_balance_display()
        self.amount = int(self.csmainwdw_spinbox_money.value())

        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)
        # self.csmainwdw_btn_statement.clicked.connect(self.add_statement)
        # self.csmainwdw_lbl_CSinfo.setText(self.show_CSinfo)
        # self.show_CSinfo
    
    def update_balance_display(self):
        self.csmainwdw_lbl_balanceshow.setText(f"{str(self.balance)} €")

    def deposit(self):
        if self.csmainwdw_spinbox_money.value() > 0:
            self.balance += self.csmainwdw_spinbox_money.value()
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
            self.csmainwdw_lbl_resultmessage.setText("Successful deposit to the account")
            self.update_balance_display()
        else:
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.csmainwdw_lbl_resultmessage.setText("Please enter an amount..")

    def get_cash(self):
        if self.csmainwdw_spinbox_money.value() > 0:
            if self.balance >= self.csmainwdw_spinbox_money.value():
                self.balance -= self.csmainwdw_spinbox_money.value()
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account")
                self.update_balance_display()
            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

        elif self.csmainwdw_spinbox_money.value() == 0:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Please enter an amount to withdraw..")
        else:
            self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.csmainwdw_lbl_resultmessage.setText("Please enter a positif amount..")

    # def add_statement(self):
    #     with open ("Main deneme/1234.json","r") as file:  #daha sonra f stringle csID yazılacak.
    #         data = json.load(file)
    #     print(data["Customer_ID"])

      
    # def show_CSinfo(self):
    #     with open ("Main deneme/1234.json","r") as file:  #daha sonra f stringle csID yazılacak.
    #         data = json.load(file)
    #     name = data["Name"]
    #     csID = data["Customer_ID"]
    #     # self.csmainwdw_lbl_CSinfo.setText(name, csID)
    #     return (f"You've reached {name}'s acount. Customer ID: {csID}")
        

        
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    csmainwindow = CSMain()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(csmainwindow)
    widget.show()
    sys.exit(app.exec_())