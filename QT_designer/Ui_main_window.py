# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\musab\OneDrive\Belgeler\GitHub\Atm-Project\QT_designer\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_open_window(object):
    def setupUi(self, open_window):
        open_window.setObjectName("open_window")
        open_window.resize(480, 600)
        self.centralwidget = QtWidgets.QWidget(open_window)
        self.centralwidget.setObjectName("centralwidget")
        self.openwdw_lbl_welcome = QtWidgets.QLabel(self.centralwidget)
        self.openwdw_lbl_welcome.setGeometry(QtCore.QRect(80, 60, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.openwdw_lbl_welcome.setFont(font)
        self.openwdw_lbl_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.openwdw_lbl_welcome.setObjectName("openwdw_lbl_welcome")
        self.openwdw_btn_CSLogin = QtWidgets.QPushButton(self.centralwidget)
        self.openwdw_btn_CSLogin.setGeometry(QtCore.QRect(60, 240, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openwdw_btn_CSLogin.setFont(font)
        self.openwdw_btn_CSLogin.setObjectName("openwdw_btn_CSLogin")
        self.openwdw_btn_ADLogin = QtWidgets.QPushButton(self.centralwidget)
        self.openwdw_btn_ADLogin.setGeometry(QtCore.QRect(250, 240, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openwdw_btn_ADLogin.setFont(font)
        self.openwdw_btn_ADLogin.setObjectName("openwdw_btn_ADLogin")
        self.openwdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.openwdw_btn_exit.setGeometry(QtCore.QRect(150, 360, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openwdw_btn_exit.setFont(font)
        self.openwdw_btn_exit.setObjectName("openwdw_btn_exit")
        open_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(open_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        open_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(open_window)
        self.statusbar.setObjectName("statusbar")
        open_window.setStatusBar(self.statusbar)

        self.retranslateUi(open_window)
        self.openwdw_btn_exit.clicked.connect(open_window.close)
        QtCore.QMetaObject.connectSlotsByName(open_window)

    def retranslateUi(self, open_window):
        _translate = QtCore.QCoreApplication.translate
        open_window.setWindowTitle(_translate("open_window", "MainWindow"))
        self.openwdw_lbl_welcome.setText(_translate("open_window", "Welcome to the Banking App"))
        self.openwdw_btn_CSLogin.setText(_translate("open_window", "CUSTOMER LOGIN"))
        self.openwdw_btn_ADLogin.setText(_translate("open_window", "ADMIN LOGIN"))
        self.openwdw_btn_exit.setText(_translate("open_window", "EXIT"))