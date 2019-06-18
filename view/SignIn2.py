# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class IniciarSesionView(object):
    def __init__(self, MainWindow):
        self.passwd = None
        self.user = None
        self.type = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Inicio/mapa.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(3, 48, 118,180);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Name_app = QtWidgets.QLabel(self.frame)
        self.Name_app.setGeometry(QtCore.QRect(180, 90, 471, 101))
        self.Name_app.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(83, 83, 83);\n"
"background: transparent;")
        self.Name_app.setObjectName("Name_app")

        self.Name_app2 = QtWidgets.QLabel(self.frame)
        self.Name_app2.setGeometry(QtCore.QRect(180, 90, 480, 110))
        self.Name_app2.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(230, 230, 230);;\n"
"background: transparent;")
        self.Name_app2.setObjectName("Name_app")

        self.campo_email_or_user = QtWidgets.QLineEdit(self.frame)
        self.campo_email_or_user.setGeometry(QtCore.QRect(240, 250, 321, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.campo_email_or_user.setFont(font)
        self.campo_email_or_user.setPlaceholderText("  Email or Username")
        self.campo_email_or_user.setTabletTracking(False)
        self.campo_email_or_user.setAutoFillBackground(True)
        self.campo_email_or_user.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.campo_email_or_user.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_email_or_user.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_email_or_user.setClearButtonEnabled(True)
        self.campo_email_or_user.setObjectName("campo_email_or_user")
        self.campo_password = QtWidgets.QLineEdit(self.frame)
        self.campo_password.setPlaceholderText("  Password")
        self.campo_password.setGeometry(QtCore.QRect(240, 320, 321, 41))
        self.campo_password.setAutoFillBackground(False)
        self.campo_password.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.campo_password.setStyleSheet("background-color: rgb(254, 252, 224,70);\n"

"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_password.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_password.setClearButtonEnabled(True)
        self.campo_password.setObjectName("campo_password")
        self.campo_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_Create_Account = QtWidgets.QPushButton(self.frame)
        self.pushButton_Create_Account.setGeometry(QtCore.QRect(240, 400, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Create_Account.sizePolicy().hasHeightForWidth())
        self.pushButton_Create_Account.setSizePolicy(sizePolicy)
        self.pushButton_Create_Account.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_Create_Account.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_Create_Account.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_Create_Account.setObjectName("pushButton_Create_Acount")
        self.pushButton_Sign_In = QtWidgets.QPushButton(self.frame)
        self.pushButton_Sign_In.setGeometry(QtCore.QRect(450, 400, 111, 51))
        self.pushButton_Sign_In.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_Sign_In.setObjectName("pushButton_Sign_In")
        self.pushButton_Anonymous_access = QtWidgets.QPushButton(self.frame)
        self.pushButton_Anonymous_access.setGeometry(QtCore.QRect(290, 470, 211, 51))
        self.pushButton_Anonymous_access.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(570, 253, 171, 41))
        self.groupBox.setStyleSheet("background: transparent;\n"
"border: transparent;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_User = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_User.setGeometry(QtCore.QRect(0, 10, 82, 17))
        self.radioButton_User.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_User.setChecked(True)
        self.radioButton_User.setObjectName("radioButton_User")
        self.radioButton_Owner = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Owner.setGeometry(QtCore.QRect(60, 10, 82, 17))
        self.radioButton_Owner.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Owner.setObjectName("radioButton_Owner")
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.radioButton_User.setText("User")
        self.radioButton_Owner.setText("Owner")

        self.pushButton_Sign_In
        self.pushButton_Anonymous_access.setObjectName("pushButton_Anonymous_access")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def actualizar(self):
        #if self.lineEdit.is
        self.user = self.campo_email_or_user.text()
        self.passwd = self.campo_password.text()
        if self.radioButton_User.isChecked():
            self.type = 1
            print("Hola")
        else:
            self.type = 2
            print("Hola")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_app.setText(_translate("MainWindow", "InfoPlaces"))
        self.Name_app2.setText(_translate("MainWindow", "InfoPlaces"))
        self.pushButton_Create_Account.setText(_translate("MainWindow", "Create Acount"))
        self.pushButton_Sign_In.setText(_translate("MainWindow", "Sign In"))
        self.pushButton_Anonymous_access.setText(_translate("MainWindow", "Anonymous access"))
        MainWindow.show()


