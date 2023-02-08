# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/Atm-Project/QT_designer/admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_window(object):
    def setupUi(self, admin_window):
        admin_window.setObjectName("admin_window")
        admin_window.resize(600, 700)
        admin_window.setMinimumSize(QtCore.QSize(600, 700))
        admin_window.setMaximumSize(QtCore.QSize(600, 700))
        admin_window.setStyleSheet("background-color: rgb(5, 130, 202);\n"
"")
        self.centralwidget = QtWidgets.QWidget(admin_window)
        self.centralwidget.setObjectName("centralwidget")
        self.adminwdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.adminwdw_lbl_heading.setGeometry(QtCore.QRect(50, 40, 491, 101))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_lbl_heading.setFont(font)
        self.adminwdw_lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.adminwdw_lbl_heading.setObjectName("adminwdw_lbl_heading")
        self.adminwdw_btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.adminwdw_btn_login.setGeometry(QtCore.QRect(200, 430, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_btn_login.setFont(font)
        self.adminwdw_btn_login.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 100, 148);\n"
"\n"
"border:2px solid rgb(0, 150, 199);\n"
"border-radius:20px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(0, 150, 199);\n"
"}")
        self.adminwdw_btn_login.setObjectName("adminwdw_btn_login")
        self.adminwdw_btn_returnmain = QtWidgets.QPushButton(self.centralwidget)
        self.adminwdw_btn_returnmain.setGeometry(QtCore.QRect(110, 540, 180, 70))
        self.adminwdw_btn_returnmain.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_btn_returnmain.setFont(font)
        self.adminwdw_btn_returnmain.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 150, 199);\n"
"   border-color: rgb(66, 167, 255);\n"
"   border-bottom-color: rgb(255, 255, 255);\n"
"   border:2px solid rgb(202, 240, 248);\n"
"   border-radius:20px;\n"
"   border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(202, 240, 248);\n"
"}\n"
"    \n"
"   ")
        self.adminwdw_btn_returnmain.setObjectName("adminwdw_btn_returnmain")
        self.adminwdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.adminwdw_btn_exit.setGeometry(QtCore.QRect(310, 540, 180, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_btn_exit.setFont(font)
        self.adminwdw_btn_exit.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 150, 199);\n"
"   border-color: rgb(66, 167, 255);\n"
"   border-bottom-color: rgb(255, 255, 255);\n"
"   border:2px solid rgb(202, 240, 248);\n"
"   border-radius:20px;\n"
"   border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(202, 240, 248);\n"
"}\n"
"    \n"
"   ")
        self.adminwdw_btn_exit.setObjectName("adminwdw_btn_exit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(171, 160, 271, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.adminwdw_lbl_ADid = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_lbl_ADid.setFont(font)
        self.adminwdw_lbl_ADid.setObjectName("adminwdw_lbl_ADid")
        self.verticalLayout.addWidget(self.adminwdw_lbl_ADid)
        self.adminwdw_linedit_ADid = QtWidgets.QLineEdit(self.layoutWidget)
        self.adminwdw_linedit_ADid.setMinimumSize(QtCore.QSize(250, 50))
        self.adminwdw_linedit_ADid.setMaximumSize(QtCore.QSize(250, 50))
        self.adminwdw_linedit_ADid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adminwdw_linedit_ADid.setObjectName("adminwdw_linedit_ADid")
        self.verticalLayout.addWidget(self.adminwdw_linedit_ADid)
        self.adminwdw_lbl_ADpassword = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.adminwdw_lbl_ADpassword.setFont(font)
        self.adminwdw_lbl_ADpassword.setObjectName("adminwdw_lbl_ADpassword")
        self.verticalLayout.addWidget(self.adminwdw_lbl_ADpassword)
        self.adminwdw_linedit_ADpassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.adminwdw_linedit_ADpassword.setMinimumSize(QtCore.QSize(250, 50))
        self.adminwdw_linedit_ADpassword.setMaximumSize(QtCore.QSize(250, 50))
        self.adminwdw_linedit_ADpassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adminwdw_linedit_ADpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminwdw_linedit_ADpassword.setObjectName("adminwdw_linedit_ADpassword")
        self.verticalLayout.addWidget(self.adminwdw_linedit_ADpassword)
        self.adminwdw_lbl_warning = QtWidgets.QLabel(self.layoutWidget)
        self.adminwdw_lbl_warning.setStyleSheet("color: rgb(255, 38, 0);")
        self.adminwdw_lbl_warning.setText("")
        self.adminwdw_lbl_warning.setObjectName("adminwdw_lbl_warning")
        self.verticalLayout.addWidget(self.adminwdw_lbl_warning)
        admin_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        admin_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin_window)
        self.statusbar.setObjectName("statusbar")
        admin_window.setStatusBar(self.statusbar)

        self.retranslateUi(admin_window)
        QtCore.QMetaObject.connectSlotsByName(admin_window)

    def retranslateUi(self, admin_window):
        _translate = QtCore.QCoreApplication.translate
        admin_window.setWindowTitle(_translate("admin_window", "Admin Window"))
        self.adminwdw_lbl_heading.setText(_translate("admin_window", "Administrative Login "))
        self.adminwdw_btn_login.setText(_translate("admin_window", "LOGIN"))
        self.adminwdw_btn_returnmain.setText(_translate("admin_window", "Back"))
        self.adminwdw_btn_exit.setText(_translate("admin_window", "Exit"))
        self.adminwdw_lbl_ADid.setText(_translate("admin_window", "ID:"))
        self.adminwdw_lbl_ADpassword.setText(_translate("admin_window", "Password:"))
