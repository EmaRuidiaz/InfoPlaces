# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton, QVBoxLayout, QFileDialog , QLabel, QTextEdit
from PyQt5.QtGui import QPixmap
import re

class UserEditView(object):
    def __init__(self, MainWindow, user):
        self.firstname = None
        self.lastname = None
        self.username = None
        self.birthdate = None
        self.email = None
        self.password = None
        self.confirmuser = None
        self.phone = None
        self.fileName = user.image
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800,600)
        #MainWindow.resize(798, 582)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.338983, y1:0.631, x2:1, y2:0, stop:0.361582 rgba(61, 139, 247, 255), stop:0.977401 rgba(3, 123, 179, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Potho = QtWidgets.QLabel(self.centralwidget)
        self.Potho.setGeometry(QtCore.QRect(25, 125, 241, 211))
        self.Potho.setStyleSheet("background: transparent;")
        self.Potho.setText("")
        self.Potho.setPixmap(QtGui.QPixmap(self.fileName))
        self.Potho.setScaledContents(True)
        self.Potho.setObjectName("Potho")
        self.First_Name = QtWidgets.QLabel(self.centralwidget)
        self.First_Name.setGeometry(QtCore.QRect(290, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.First_Name.setFont(font)
        self.First_Name.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.First_Name.setObjectName("First_Name")
        self.Last_Name = QtWidgets.QLabel(self.centralwidget)
        self.Last_Name.setGeometry(QtCore.QRect(290, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Last_Name.setFont(font)
        self.Last_Name.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Last_Name.setObjectName("Last_Name")
        self.Phone_Number = QtWidgets.QLabel(self.centralwidget)
        self.Phone_Number.setGeometry(QtCore.QRect(290, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Phone_Number.setFont(font)
        self.Phone_Number.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Phone_Number.setObjectName("Phone_Number")
        self.Email = QtWidgets.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(290, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Email.setFont(font)
        self.Email.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.Email.setObjectName("Email")
        self.lineEdit_First_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_First_Name.setGeometry(QtCore.QRect(410, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_First_Name.setFont(font)
        self.lineEdit_First_Name.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 6px;\n"
"border: transparent;\n")
        self.lineEdit_First_Name.setObjectName("lineEdit_First_Name")
        self.lineEdit_Last_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Last_Name.setGeometry(QtCore.QRect(410, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Last_Name.setFont(font)
        self.lineEdit_Last_Name.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 6px;\n"
"border: transparent;\n")
        self.lineEdit_Last_Name.setObjectName("lineEdit_Last_Name")
        self.lineEdit_Phone_Number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Phone_Number.setGeometry(QtCore.QRect(450, 280, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Phone_Number.setFont(font)
        self.lineEdit_Phone_Number.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 6px;\n"
"border: transparent;\n")
        self.lineEdit_Phone_Number.setObjectName("lineEdit_Phone_Number")
        self.lineEdit_Phone_Number.textChanged.connect(self.validar_PhoneNumber)
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(400, 230, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 6px;\n"
"border: transparent;\n")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        '''self.pushButton_Home = QtWidgets.QPushButton(self.centralwidget)
                                self.pushButton_Home.setGeometry(QtCore.QRect(370, 0, 61, 23))
                                self.pushButton_Home.setAutoFillBackground(False)
                                self.pushButton_Home.setStyleSheet("background: rgb(225,225,225,60);\n"
                        "border: 1px solid rgb(225,225,225,60);\n"
                        "border-radius: 6px;\n"
                        "color: rgb(225,225,225);\n"
                        "")
                                self.pushButton_Home.setObjectName("pushButton_Home")'''
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(80, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 6px;\n"
"border: transparent;\n")
        self.Username.setAlignment(QtCore.Qt.AlignCenter)
        self.Username.setObjectName("Username")
        self.pushButton_back_Change_Password = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_back_Change_Password.setGeometry(QtCore.QRect(240, 390, 300, 31))
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
        self.pushButton_back_Change_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_GuardarCambios = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GuardarCambios.setGeometry(QtCore.QRect(550, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_GuardarCambios.setFont(font)
        self.pushButton_GuardarCambios.setAutoFillBackground(False)
        self.pushButton_GuardarCambios.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_GuardarCambios.setObjectName("pushButton_Resgister_Store")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setStyleSheet("background: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Inicio/17266.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        
        self.Cargar_imagen = QtWidgets.QPushButton(self.label)
        self.Cargar_imagen.setGeometry(QtCore.QRect(25, 100, 120, 23))
        self.Cargar_imagen.setStyleSheet("background: rgb(225,225,225,60);\n"
                        "border: 1px solid rgb(225,225,225,60);\n"
                        "border-radius: 6px;\n"
                        "color: rgb(225,225,225);\n"
                        "")
        self.Cargar_imagen.setObjectName("Cargar_imagen")
        self.Cargar_imagen.clicked.connect(lambda: self.getImage(MainWindow, user))
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(547, 0, 61, 23))
        self.pushButton_cancel.setAutoFillBackground(False)
        self.pushButton_cancel.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_cancel.setObjectName("pushButton_back")
        self.lineEdit_First_Name.setMaxLength(20)
        self.lineEdit_Last_Name.setMaxLength(20)
        self.lineEdit_Phone_Number.setMaxLength(13)
        self.lineEdit_Email.setMaxLength(20)
        self.Username.setMaxLength(20)

        self.Cargar_imagen.raise_()
        self.label.raise_()
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
        #self.pushButton_Home.raise_()
        self.Username.raise_()
        self.pushButton_back_Change_Password.raise_()
        self.pushButton_GuardarCambios.raise_()
        self.pushButton_cancel.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.show()

        self.retranslateUi(MainWindow, user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def validar_PhoneNumber(self):
        self.lineEdit_Phone_Number.setMaxLength(13)
        phone = self.lineEdit_Phone_Number.text()
        validar = re.match('^[0-9]{10,13}$',phone)

    def openFileNameDialog(self, MainWindow, user):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        self.fileName, _= QFileDialog.getOpenFileName(MainWindow,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        if self.fileName:
            pixmap = QtGui.QPixmap(self.fileName)
            self.Potho.setPixmap(QtGui.QPixmap(self.fileName))
            return pixmap
        else:
            self.fileName = user.image
            pixmap = QtGui.QPixmap(self.fileName)
            self.Potho.setPixmap(QtGui.QPixmap(self.fileName))
            return pixmap

    def actualizar(self):
            self.firstname = self.lineEdit_First_Name.text()
            self.lastname = self.lineEdit_Last_Name.text()
            self.username = self.Username.text()
            self.password = self.lineEdit_Email.text()
            self.phone = self.lineEdit_Phone_Number.text()
        #self.fileName = 

    def getImage(self, MainWindow, user):
        self.photo = self.openFileNameDialog(MainWindow, user)
    #    import sys
    #    Appp = QApplication(sys.argv)
    #    PhotoWindow = QtWidgets.QMainWindow()
    #    WinPhoto = WindowPhoto()
    #    WinPhoto.InitWindow(PhotoWindow)
    #    sys.exit(Appp.exec())

    def retranslateUi(self, MainWindow, user):
       _translate = QtCore.QCoreApplication.translate
       MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       self.First_Name.setText(_translate("MainWindow", "First Name:"))
       self.lineEdit_First_Name.setText(_translate("MainWindow", user.firstname))
       self.Last_Name.setText(_translate("MainWindow", "Last Name:"))
       self.lineEdit_Last_Name.setText(_translate("MainWindow", user.lastname))
       self.Phone_Number.setText(_translate("MainWindow", "Phone Number:"))
       self.lineEdit_Phone_Number.setText(_translate("MainWindow", str(user.phone_number)))
       self.Email.setText(_translate("MainWindow", "Password:"))
       self.lineEdit_Email.setText(_translate("MainWindow", user.password))
       #self.pushButton_Home.setText(_translate("MainWindow", "Home"))
       self.Username.setText(_translate("MainWindow", user.username))
       self.pushButton_back_Change_Password.setText(_translate("MainWindow", user.email))
       self.pushButton_GuardarCambios.setText(_translate("MainWindow", "Save Changes"))
       self.Cargar_imagen.setText(_translate("MainWindow", "Change Profile Picture"))
       self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))

'''import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    sys.exit(app.exec_())'''

