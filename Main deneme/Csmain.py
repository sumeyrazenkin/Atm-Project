import sys
from PyQt5.QtWidgets import *
from Ui_customer_main_window import *

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
            self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account..")
            self.update_balance_display()
        else:
            self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    csmainwindow = CSMain()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(csmainwindow)
    widget.show()
    sys.exit(app.exec_())