# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(800,600)
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(798, 582)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.338983, y1:0.631, x2:1, y2:0, stop:0.361582 rgba(61, 139, 247, 255), stop:0.977401 rgba(3, 123, 179, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Potho = QtWidgets.QLabel(self.centralwidget)
        self.Potho.setGeometry(QtCore.QRect(30, 160, 271, 231))
        self.Potho.setStyleSheet("background: transparent;")
        self.Potho.setText("")
        self.Potho.setPixmap(QtGui.QPixmap(":/dfsfsd/user.PNG"))
        self.Potho.setScaledContents(True)
        self.Potho.setObjectName("Potho")
        self.First_Name = QtWidgets.QLabel(self.centralwidget)
        self.First_Name.setGeometry(QtCore.QRect(250, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.First_Name.setFont(font)
        self.First_Name.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.First_Name.setObjectName("First_Name")
        self.Last_Name = QtWidgets.QLabel(self.centralwidget)
        self.Last_Name.setGeometry(QtCore.QRect(310, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Last_Name.setFont(font)
        self.Last_Name.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Last_Name.setObjectName("Last_Name")
        self.Phone_Number = QtWidgets.QLabel(self.centralwidget)
        self.Phone_Number.setGeometry(QtCore.QRect(320, 260, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Phone_Number.setFont(font)
        self.Phone_Number.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Phone_Number.setObjectName("Phone_Number")
        self.Email = QtWidgets.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(310, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Email.setFont(font)
        self.Email.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Email.setObjectName("Email")
        self.lineEdit_First_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_First_Name.setGeometry(QtCore.QRect(370, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_First_Name.setFont(font)
        self.lineEdit_First_Name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"color: rgb(225,225,225)")
        self.lineEdit_First_Name.setObjectName("lineEdit_First_Name")
        self.lineEdit_Last_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Last_Name.setGeometry(QtCore.QRect(430, 190, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Last_Name.setFont(font)
        self.lineEdit_Last_Name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"color: rgb(225,225,225)")
        self.lineEdit_Last_Name.setObjectName("lineEdit_Last_Name")
        self.lineEdit_Phone_Number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Phone_Number.setGeometry(QtCore.QRect(480, 260, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Phone_Number.setFont(font)
        self.lineEdit_Phone_Number.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"color: rgb(225,225,225)")
        self.lineEdit_Phone_Number.setObjectName("lineEdit_Phone_Number")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(390, 330, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"color: rgb(225,225,225)")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(0, 0, 61, 23))
        self.pushButton_back.setAutoFillBackground(False)
        self.pushButton_back.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_Home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Home.setGeometry(QtCore.QRect(370, 0, 61, 23))
        self.pushButton_Home.setAutoFillBackground(False)
        self.pushButton_Home.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(90, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"color: rgb(225,225,225)")
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setObjectName("Username")
        self.pushButton_back_Change_Password = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back_Change_Password.setGeometry(QtCore.QRect(290, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back_Change_Password.setFont(font)
        self.pushButton_back_Change_Password.setAutoFillBackground(False)
        self.pushButton_back_Change_Password.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_back_Change_Password.setObjectName("pushButton_back_Change_Password")
        self.pushButton_Resgister_Store = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Resgister_Store.setGeometry(QtCore.QRect(480, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_Resgister_Store.setFont(font)
        self.pushButton_Resgister_Store.setAutoFillBackground(False)
        self.pushButton_Resgister_Store.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_Resgister_Store.setObjectName("pushButton_Resgister_Store")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Editar = QtWidgets.QLabel(self.frame)
        self.Editar.setGeometry(QtCore.QRect(760, 0, 41, 41))
        self.Editar.setStyleSheet("background: transparent;")
        self.Editar.setText("")
        self.Editar.setPixmap(QtGui.QPixmap(":/Inicio/descarga1.png"))
        self.Editar.setScaledContents(True)
        self.Editar.setObjectName("Editar")
        self.frame.raise_()
        self.Potho.raise_()
        self.First_Name.raise_()
        self.Last_Name.raise_()
        self.Phone_Number.raise_()
        self.Email.raise_()
        self.lineEdit_First_Name.raise_()
        self.lineEdit_Last_Name.raise_()
        self.lineEdit_Phone_Number.raise_()
        self.lineEdit_Email.raise_()
        self.pushButton_back.raise_()
        self.pushButton_Home.raise_()
        self.Username.raise_()
        self.pushButton_back_Change_Password.raise_()
        self.pushButton_Resgister_Store.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.First_Name.setText(_translate("MainWindow", "First Name:"))
        self.Last_Name.setText(_translate("MainWindow", "Last Name:"))
        self.Phone_Number.setText(_translate("MainWindow", "Phone Number:"))
        self.Email.setText(_translate("MainWindow", "E-mail:"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        self.Username.setText(_translate("MainWindow", "User Name"))
        self.pushButton_back_Change_Password.setText(_translate("MainWindow", "Change Password"))
        self.pushButton_Resgister_Store.setText(_translate("MainWindow", "Register Store"))

import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
