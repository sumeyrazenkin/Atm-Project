import sys
from PyQt5.QtWidgets import *
from Ui_customer_main_window import *

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)
        # self.csmainwdw_lbl_balanceshow.text(f"{self.balanceshow} €")
        self.amount = int(self.csmainwdw_spinbox_money.text())
        self.balance = int(self.csmainwdw_lbl_balanceshow.text())

        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)
    
    def get_cash(self):
        pass

    def deposit(self):
        self.balance += self.amount
        print(self.balance)
        # self.balance.show()
        

        "deneme"


if __name__ == "__main__":

    app = QApplication(sys.argv)
    csmainwindow = CSMain()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(csmainwindow)
    widget.show()
    sys.exit(app.exec_())