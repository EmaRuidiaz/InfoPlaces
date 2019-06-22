# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateAcount.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re

class CreateAccountView(object):
    def __init__(self, MainWindow):
        self.firstname = None
        self.lastname = None
        self.username = None
        self.birthdate = None
        self.email = None
        self.password = None
        self.type = 1
        self.confirmuser = None
        self.phone = None
        self.terms = 0
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
        self.frame.setStyleSheet("background-color: rgb(3, 48, 118,180);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Name_app = QtWidgets.QLabel(self.frame)
        self.Name_app.setGeometry(QtCore.QRect(170, 30, 462, 92))
        self.Name_app.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(83, 83, 83);\n"
"background: transparent;")
        self.Name_app.setObjectName("Name_app")

        self.Name_app2 = QtWidgets.QLabel(self.frame)
        self.Name_app2.setGeometry(QtCore.QRect(170, 30, 471, 101))
        self.Name_app2.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(230, 230, 230);\n"
"background: transparent;")
        self.Name_app2.setObjectName("Name_app")

        self.campo_first_name = QtWidgets.QLineEdit(self.frame)
        self.campo_first_name.setGeometry(QtCore.QRect(50, 160, 321, 41))
        self.campo_first_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_first_name.setPlaceholderText("  First Name")
        self.campo_first_name.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_first_name.setObjectName("campo_first_name")
        self.campo_last_name = QtWidgets.QLineEdit(self.frame)
        self.campo_last_name.setPlaceholderText("  Last Name")
        self.campo_last_name.setGeometry(QtCore.QRect(400, 160, 321, 41))
        self.campo_last_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_last_name.setObjectName("campo_last_name")
        self.campo_email = QtWidgets.QLineEdit(self.frame)
        self.campo_email.setPlaceholderText("  Email")
        self.campo_email.setGeometry(QtCore.QRect(400, 220, 321, 41))
        self.campo_email.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_email.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_email.setObjectName("campo_email")
        self.campo_username = QtWidgets.QLineEdit(self.frame)
        self.campo_username.setPlaceholderText("  Username")
        self.campo_username.setGeometry(QtCore.QRect(50, 220, 321, 41))
        self.campo_username.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_username.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_username.setObjectName("campo_username")
        self.campo_password = QtWidgets.QLineEdit(self.frame)
        self.campo_password.setGeometry(QtCore.QRect(50, 280, 321, 41))
        self.campo_password.setPlaceholderText("  Password")
        self.campo_password.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_password.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_password.setObjectName("campo_password")
        self.campo_confirm_password = QtWidgets.QLineEdit(self.frame)
        self.campo_confirm_password.setGeometry(QtCore.QRect(400, 280, 321, 41))
        self.campo_confirm_password.setPlaceholderText("  Confirm Password")
        self.campo_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_confirm_password.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_confirm_password.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_confirm_password.setObjectName("campo_confirm_password")
        self.campo_phone_number = QtWidgets.QLineEdit(self.frame)
        self.campo_phone_number.setPlaceholderText("  Phone Number")
        self.campo_phone_number.setGeometry(QtCore.QRect(400, 340, 321, 41))
        self.campo_phone_number.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.campo_phone_number.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_phone_number.setObjectName("campo_phone_number")
        self.fecha_nacimiento = QtWidgets.QDateEdit(self.frame)
        #self.fecha_nacimiento.setPlaceholderText("  birthdate")
        self.fecha_nacimiento.setGeometry(QtCore.QRect(50, 340, 321, 41))
        self.fecha_nacimiento.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
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
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_Create_Account = QtWidgets.QPushButton(self.frame)
        self.pushButton_Create_Account.setGeometry(QtCore.QRect(360, 450, 191, 51))
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
        self.checkBox_accept_terms = QtWidgets.QCheckBox(self.frame)
        self.checkBox_accept_terms.setGeometry(QtCore.QRect(210, 410, 311, 21))
        self.checkBox_accept_terms.setStyleSheet("background: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 6px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.checkBox_accept_terms.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_accept_terms.setObjectName("checkBox_accept_terms")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.show()

        self.pushButton_Create_Account
        # Validaciónes de los campos
        self.campo_first_name.textChanged.connect(self.validar_Firstname)
        self.campo_last_name.textChanged.connect(self.validar_Lastname)
        self.campo_username.textChanged.connect(self.validar_Username)
        self.campo_email.textChanged.connect(self.validar_Email)
        self.campo_phone_number.textChanged.connect(self.validar_PhoneNumber)


    def actualizar(self):
        self.firstname = self.campo_first_name.text()
        self.lastname = self.campo_last_name.text()
        self.username = self.campo_username.text()
        self.birthdate = str(self.fecha_nacimiento.date().year()) + "-" + str(self.fecha_nacimiento.date().month()) + "-" + str(self.fecha_nacimiento.date().day())
        self.email = self.campo_email.text()
        self.password = self.campo_password.text()
        self.confirmuser = self.campo_confirm_password.text()
        if self.checkBox_accept_terms.isChecked():
            self.terms = 1
        else:
            self.terms = 0
        self.phone = self.campo_phone_number.text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_app.setText(_translate("MainWindow", "InfoPlaces"))
        self.Name_app2.setText(_translate("MainWindow", "InfoPlaces"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_Create_Account.setText(_translate("MainWindow", "Create Acount"))
        self.checkBox_accept_terms.setText(_translate("MainWindow", " I accept the terms and conditions"))

    def validar_Firstname(self):
        self.campo_first_name.setMaxLength(30) #Permite limitar la cantidad de caracteres en el campo
        firstname = self.campo_first_name.text()
        validar = re.match('^[a-z\ sáéíóúäëïöüñ]+$', firstname,re.I)
        # Desde aca es la validación
        # El resto es para cambiar de color el borde dependiendo de la validación
        if firstname == '':
            self.campo_first_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
            return False
        elif not validar:
            self.campo_first_name.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid red;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return False
        else:
            self.campo_first_name.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid green;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return True

    def validar_Lastname(self):
        self.campo_last_name.setMaxLength(30)
        lastname = self.campo_last_name.text()
        validar = re.match('^[a-z\ sáéíóúäëïöüñ]+$', lastname,re.I)
        if lastname == '':
            self.campo_last_name.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
            return False
        elif not validar:
            self.campo_last_name.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid red;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return False
        else:
            self.campo_last_name.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid green;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return True


    def validar_Username(self):
        self.campo_username.setMaxLength(20)
        username = self.campo_username.text()
        validar = re.match('[a-zA-Z0-9\-_.@sáéíóúäëïöüñ]+$',username)
        if username == '':
            self.campo_username.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
            return False
        elif not validar:
            self.campo_username.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid red;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return False
        else:
            self.campo_username.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid green;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return True

    def validar_Email(self):
        self.campo_email.setMaxLength(50)
        email = self.campo_email.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{3,4}$',email,re.I)
        if email == '':
            self.campo_email.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
            return False
        elif not validar:
            self.campo_email.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid red;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return False
        else:
            self.campo_email.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid green;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return True

    def validar_PhoneNumber(self):
        self.campo_phone_number.setMaxLength(13)
        phone = self.campo_phone_number.text()
        validar = re.match('^[0-9]{10,13}$',phone)
        if phone == '':
            self.campo_phone_number.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
            return False
        elif not validar:
            self.campo_phone_number.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid red;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return False
        else:
            self.campo_phone_number.setStyleSheet("Background-color: rgb(254,252,224,60);\n"
                "Border: 1px solid green;\n"
                "border-radius: 6px;\n"
                "font: 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);\n"
"")
            return True

    # Abre una ventana de mensaje de error
    def validar_formulario(self):
        if self.validar_Firstname and self.validar_Lastname and self.validar_Email and self.validar_PhoneNumber:
            QMessageBox.information(self,"Formulario correcto","Validacion correcta",QMessageBox.Discard)
        else:
            QMessageBox.warning(self,"Formulario incorrecto","Validacion incorrecta",QMessageBox.Discard)


'''

import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    sys.exit(app.exec_())'''

