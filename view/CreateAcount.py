# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateAcount.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.frame.setStyleSheet("background-color: rgb(3, 48, 118,180);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Name_app = QtWidgets.QLabel(self.frame)
        self.Name_app.setGeometry(QtCore.QRect(170, 30, 471, 101))
        self.Name_app.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(230, 230, 230);\n"
"background: transparent;")
        self.Name_app.setObjectName("Name_app")
        self.campo_first_name = QtWidgets.QLineEdit(self.frame)
        self.campo_first_name.setGeometry(QtCore.QRect(50, 160, 321, 41))
        self.campo_first_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_first_name.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_first_name.setObjectName("campo_first_name")
        self.campo_last_name = QtWidgets.QLineEdit(self.frame)
        self.campo_last_name.setGeometry(QtCore.QRect(400, 160, 321, 41))
        self.campo_last_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_last_name.setObjectName("campo_last_name")
        self.campo_email = QtWidgets.QLineEdit(self.frame)
        self.campo_email.setGeometry(QtCore.QRect(400, 220, 321, 41))
        self.campo_email.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_email.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_email.setObjectName("campo_email")
        self.campo_username = QtWidgets.QLineEdit(self.frame)
        self.campo_username.setGeometry(QtCore.QRect(50, 220, 321, 41))
        self.campo_username.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_username.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_username.setObjectName("campo_username")
        self.campo_password = QtWidgets.QLineEdit(self.frame)
        self.campo_password.setGeometry(QtCore.QRect(50, 280, 321, 41))
        self.campo_password.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_password.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_password.setObjectName("campo_password")
        self.campo_confirm_password = QtWidgets.QLineEdit(self.frame)
        self.campo_confirm_password.setGeometry(QtCore.QRect(400, 280, 321, 41))
        self.campo_confirm_password.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_confirm_password.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_confirm_password.setObjectName("campo_confirm_password")
        self.campo_phone_number = QtWidgets.QLineEdit(self.frame)
        self.campo_phone_number.setGeometry(QtCore.QRect(400, 340, 321, 41))
        self.campo_phone_number.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_phone_number.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_phone_number.setObjectName("campo_phone_number")
        self.fecha_nacimiento = QtWidgets.QDateEdit(self.frame)
        self.fecha_nacimiento.setGeometry(QtCore.QRect(50, 340, 321, 41))
        self.fecha_nacimiento.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.fecha_nacimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.fecha_nacimiento.setDate(QtCore.QDate(2019, 6, 17))
        self.fecha_nacimiento.setObjectName("fecha_nacimiento")
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cancel.setGeometry(QtCore.QRect(210, 450, 121, 51))
        self.pushButton_cancel.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_Create_Acount = QtWidgets.QPushButton(self.frame)
        self.pushButton_Create_Acount.setGeometry(QtCore.QRect(360, 450, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Create_Acount.sizePolicy().hasHeightForWidth())
        self.pushButton_Create_Acount.setSizePolicy(sizePolicy)
        self.pushButton_Create_Acount.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_Create_Acount.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_Create_Acount.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_Create_Acount.setObjectName("pushButton_Create_Acount")
        self.checkBox_accept_terms = QtWidgets.QCheckBox(self.frame)
        self.checkBox_accept_terms.setGeometry(QtCore.QRect(210, 410, 311, 21))
        self.checkBox_accept_terms.setStyleSheet("background: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.checkBox_accept_terms.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_accept_terms.setObjectName("checkBox_accept_terms")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_app.setText(_translate("MainWindow", "InfoPlaces"))
        self.campo_first_name.setText(_translate("MainWindow", "First Name"))
        self.campo_last_name.setText(_translate("MainWindow", "Last Name"))
        self.campo_email.setText(_translate("MainWindow", "Email"))
        self.campo_username.setText(_translate("MainWindow", "Username"))
        self.campo_password.setText(_translate("MainWindow", "Password"))
        self.campo_confirm_password.setText(_translate("MainWindow", "Confirm Password"))
        self.campo_phone_number.setText(_translate("MainWindow", "Phone Number"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_Create_Acount.setText(_translate("MainWindow", "Create Acount"))
        self.checkBox_accept_terms.setText(_translate("MainWindow", " I accept the terms and conditions"))

import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

