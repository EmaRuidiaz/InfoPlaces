# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterStore.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class RegisterStoreView(object):
    def __init__(self, MainWindow, user):
        self.name = ""
        self.address = ""
        self.number = ""
        self.description = ""
        self.streetname = ""
        self.streetnumber = ""
        self.schedule = []
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
        self.Name_app.setGeometry(QtCore.QRect(180, 10, 471, 101))
        self.Name_app.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(230, 230, 230);\n"
"background: transparent;")
        self.Name_app.setObjectName("Name_app")
        self.Name_app_2 = QtWidgets.QLabel(self.frame)
        self.Name_app_2.setGeometry(QtCore.QRect(180, 10, 480, 110))
        self.Name_app_2.setStyleSheet("font: 93px \"Segoe Print\";\n"
"color: rgb(83, 83, 83);\n"
"background: transparent;")
        self.Name_app_2.setObjectName("Name_app_2")
        self.Name_app_3 = QtWidgets.QLabel(self.frame)
        self.Name_app_3.setGeometry(QtCore.QRect(50, 90, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Name_app_3.setFont(font)
        self.Name_app_3.setStyleSheet("font: 40px \"Segoe Print\";\n"
"color: rgb(230, 230, 230);\n"
"background: transparent;")
        self.Name_app_3.setObjectName("Name_app_3")
        self.Name_app_4 = QtWidgets.QLabel(self.frame)
        self.Name_app_4.setGeometry(QtCore.QRect(50, 93, 301, 71))
        self.Name_app_4.setStyleSheet("font: 40px \"Segoe Print\";\n"
"color: rgb(83, 83, 83);\n"
"background: transparent;")
        self.Name_app_4.setObjectName("Name_app_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 241, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 170, 241, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(630, 170, 91, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border:1px solid black;\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(380, 210, 121, 31))
        self.label_2.setStyleSheet("background: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(225,225,225);")
        self.label_2.setObjectName("label_2")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(80, 240, 251, 321))
        self.toolBox.setStyleSheet("background-color:rgb(188, 188, 188,60);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.Monday = QtWidgets.QWidget()
        self.Monday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Monday.setObjectName("Monday")
        self.timeEdit_Open_Monday1 = QtWidgets.QTimeEdit(self.Monday)
        self.timeEdit_Open_Monday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Monday1.setStyleSheet("color: black")
        self.timeEdit_Open_Monday1.setObjectName("timeEdit_Open_Monday1")
        self.label_3 = QtWidgets.QLabel(self.Monday)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_3.setObjectName("label_3")
        self.timeEdit_Close_Monday1 = QtWidgets.QTimeEdit(self.Monday)
        self.timeEdit_Close_Monday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Monday1.setStyleSheet("color: black")
        self.timeEdit_Close_Monday1.setObjectName("timeEdit_Close_Monday1")
        self.label_4 = QtWidgets.QLabel(self.Monday)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_4.setObjectName("label_4")
        self.timeEdit_Open_Monday2 = QtWidgets.QTimeEdit(self.Monday)
        self.timeEdit_Open_Monday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Monday2.setStyleSheet("color: black")
        self.timeEdit_Open_Monday2.setObjectName("timeEdit_Open_Monday2")
        self.label_5 = QtWidgets.QLabel(self.Monday)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_5.setObjectName("label_5")
        self.timeEdit_Close_Monday2 = QtWidgets.QTimeEdit(self.Monday)
        self.timeEdit_Close_Monday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Monday2.setStyleSheet("color: black")
        self.timeEdit_Close_Monday2.setObjectName("timeEdit_Close_Monday2")
        self.label_6 = QtWidgets.QLabel(self.Monday)
        self.label_6.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_6.setObjectName("label_6")
        self.toolBox.addItem(self.Monday, "")
        self.Tuesday = QtWidgets.QWidget()
        self.Tuesday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Tuesday.setObjectName("Tuesday")
        self.timeEdit_Open_Tuesday1 = QtWidgets.QTimeEdit(self.Tuesday)
        self.timeEdit_Open_Tuesday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Tuesday1.setStyleSheet("color: black")
        self.timeEdit_Open_Tuesday1.setObjectName("timeEdit_Open_Tuesday1")
        self.label_7 = QtWidgets.QLabel(self.Tuesday)
        self.label_7.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Tuesday)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_8.setObjectName("label_8")
        self.timeEdit_Close_Tuesday2 = QtWidgets.QTimeEdit(self.Tuesday)
        self.timeEdit_Close_Tuesday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Tuesday2.setStyleSheet("color: black")
        self.timeEdit_Close_Tuesday2.setObjectName("timeEdit_Close_Tuesday2")
        self.label_9 = QtWidgets.QLabel(self.Tuesday)
        self.label_9.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_9.setObjectName("label_9")
        self.timeEdit_Close_Tuesday1 = QtWidgets.QTimeEdit(self.Tuesday)
        self.timeEdit_Close_Tuesday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Tuesday1.setStyleSheet("color: black")
        self.timeEdit_Close_Tuesday1.setObjectName("timeEdit_Close_Tuesday1")
        self.label_10 = QtWidgets.QLabel(self.Tuesday)
        self.label_10.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_10.setObjectName("label_10")
        self.timeEdit_Open_Tuesday2 = QtWidgets.QTimeEdit(self.Tuesday)
        self.timeEdit_Open_Tuesday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Tuesday2.setStyleSheet("color: black")
        self.timeEdit_Open_Tuesday2.setObjectName("timeEdit_Open_Tuesday2")
        self.toolBox.addItem(self.Tuesday, "")
        self.Wednesday = QtWidgets.QWidget()
        self.Wednesday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Wednesday.setObjectName("Wednesday")
        self.timeEdit_Open_Wednesday1 = QtWidgets.QTimeEdit(self.Wednesday)
        self.timeEdit_Open_Wednesday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Wednesday1.setStyleSheet("color: black")
        self.timeEdit_Open_Wednesday1.setObjectName("timeEdit_Open_Wednesday1")
        self.label_11 = QtWidgets.QLabel(self.Wednesday)
        self.label_11.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Wednesday)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_12.setObjectName("label_12")
        self.timeEdit_Close_Wednesday2 = QtWidgets.QTimeEdit(self.Wednesday)
        self.timeEdit_Close_Wednesday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Wednesday2.setStyleSheet("color: black")
        self.timeEdit_Close_Wednesday2.setObjectName("timeEdit_Close_Wednesday2")
        self.label_13 = QtWidgets.QLabel(self.Wednesday)
        self.label_13.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_13.setObjectName("label_13")
        self.timeEdit_Close_Wednesday1 = QtWidgets.QTimeEdit(self.Wednesday)
        self.timeEdit_Close_Wednesday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Wednesday1.setStyleSheet("color: black")
        self.timeEdit_Close_Wednesday1.setObjectName("timeEdit_Close_Wednesday1")
        self.label_14 = QtWidgets.QLabel(self.Wednesday)
        self.label_14.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_14.setObjectName("label_14")
        self.timeEdit_Open_Wednesday2 = QtWidgets.QTimeEdit(self.Wednesday)
        self.timeEdit_Open_Wednesday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Wednesday2.setStyleSheet("color: black")
        self.timeEdit_Open_Wednesday2.setObjectName("timeEdit_Open_Wednesday2")
        self.toolBox.addItem(self.Wednesday, "")
        self.Thursday = QtWidgets.QWidget()
        self.Thursday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Thursday.setObjectName("Thursday")
        self.timeEdit_Open_Thursday1 = QtWidgets.QTimeEdit(self.Thursday)
        self.timeEdit_Open_Thursday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Thursday1.setStyleSheet("color: black")
        self.timeEdit_Open_Thursday1.setObjectName("timeEdit_Open_Thursday1")
        self.label_15 = QtWidgets.QLabel(self.Thursday)
        self.label_15.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Thursday)
        self.label_16.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_16.setObjectName("label_16")
        self.timeEdit_Close_Thursday2 = QtWidgets.QTimeEdit(self.Thursday)
        self.timeEdit_Close_Thursday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Thursday2.setStyleSheet("color: black")
        self.timeEdit_Close_Thursday2.setObjectName("timeEdit_Close_Thursday2")
        self.label_17 = QtWidgets.QLabel(self.Thursday)
        self.label_17.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_17.setObjectName("label_17")
        self.timeEdit_Close_Thursday1 = QtWidgets.QTimeEdit(self.Thursday)
        self.timeEdit_Close_Thursday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Thursday1.setStyleSheet("color: black")
        self.timeEdit_Close_Thursday1.setObjectName("timeEdit_Close_Thursday1")
        self.label_18 = QtWidgets.QLabel(self.Thursday)
        self.label_18.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_18.setObjectName("label_18")
        self.timeEdit_Open_Thursday2 = QtWidgets.QTimeEdit(self.Thursday)
        self.timeEdit_Open_Thursday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Thursday2.setStyleSheet("color: black")
        self.timeEdit_Open_Thursday2.setObjectName("timeEdit_Open_Thursday2")
        self.toolBox.addItem(self.Thursday, "")
        self.Friday = QtWidgets.QWidget()
        self.Friday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Friday.setObjectName("Friday")
        self.timeEdit_Open_Frisday1 = QtWidgets.QTimeEdit(self.Friday)
        self.timeEdit_Open_Frisday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Frisday1.setStyleSheet("color: black")
        self.timeEdit_Open_Frisday1.setObjectName("timeEdit_Open_Frisday1")
        self.label_19 = QtWidgets.QLabel(self.Friday)
        self.label_19.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Friday)
        self.label_20.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_20.setObjectName("label_20")
        self.timeEdit_Close_Frisday2 = QtWidgets.QTimeEdit(self.Friday)
        self.timeEdit_Close_Frisday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Frisday2.setStyleSheet("color: black")
        self.timeEdit_Close_Frisday2.setObjectName("timeEdit_Close_Frisday2")
        self.label_21 = QtWidgets.QLabel(self.Friday)
        self.label_21.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_21.setObjectName("label_21")
        self.timeEdit_Close_Frisday1 = QtWidgets.QTimeEdit(self.Friday)
        self.timeEdit_Close_Frisday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Frisday1.setStyleSheet("color: black")
        self.timeEdit_Close_Frisday1.setObjectName("timeEdit_Close_Frisday1")
        self.label_22 = QtWidgets.QLabel(self.Friday)
        self.label_22.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_22.setObjectName("label_22")
        self.timeEdit_Open_Frisday2 = QtWidgets.QTimeEdit(self.Friday)
        self.timeEdit_Open_Frisday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Frisday2.setStyleSheet("color: black")
        self.timeEdit_Open_Frisday2.setObjectName("timeEdit_Open_Frisday2")
        self.toolBox.addItem(self.Friday, "")
        self.Saturday = QtWidgets.QWidget()
        self.Saturday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Saturday.setObjectName("Saturday")
        self.timeEdit_Open_Saturday1 = QtWidgets.QTimeEdit(self.Saturday)
        self.timeEdit_Open_Saturday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Saturday1.setStyleSheet("color: black")
        self.timeEdit_Open_Saturday1.setObjectName("timeEdit_Open_Saturday1")
        self.label_23 = QtWidgets.QLabel(self.Saturday)
        self.label_23.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Saturday)
        self.label_24.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_24.setObjectName("label_24")
        self.timeEdit_Close_Saturday2 = QtWidgets.QTimeEdit(self.Saturday)
        self.timeEdit_Close_Saturday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Saturday2.setStyleSheet("color: black")
        self.timeEdit_Close_Saturday2.setObjectName("timeEdit_Close_Saturday2")
        self.label_25 = QtWidgets.QLabel(self.Saturday)
        self.label_25.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_25.setObjectName("label_25")
        self.timeEdit_Close_Saturday1 = QtWidgets.QTimeEdit(self.Saturday)
        self.timeEdit_Close_Saturday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Saturday1.setStyleSheet("color: black")
        self.timeEdit_Close_Saturday1.setObjectName("timeEdit_Close_Saturday1")
        self.label_26 = QtWidgets.QLabel(self.Saturday)
        self.label_26.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_26.setObjectName("label_26")
        self.timeEdit_Open_Saturday1Open_Saturday2 = QtWidgets.QTimeEdit(self.Saturday)
        self.timeEdit_Open_Saturday1Open_Saturday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Saturday1Open_Saturday2.setStyleSheet("color: black")
        self.timeEdit_Open_Saturday1Open_Saturday2.setObjectName("timeEdit_Open_Saturday1Open_Saturday2")
        self.toolBox.addItem(self.Saturday, "")
        self.Sunday = QtWidgets.QWidget()
        self.Sunday.setGeometry(QtCore.QRect(0, 0, 251, 97))
        self.Sunday.setObjectName("Sunday")
        self.timeEdit_Open_Sunday1 = QtWidgets.QTimeEdit(self.Sunday)
        self.timeEdit_Open_Sunday1.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.timeEdit_Open_Sunday1.setStyleSheet("color: black")
        self.timeEdit_Open_Sunday1.setObjectName("timeEdit_Open_Sunday1")
        self.label_27 = QtWidgets.QLabel(self.Sunday)
        self.label_27.setGeometry(QtCore.QRect(20, 0, 51, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Sunday)
        self.label_28.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_28.setObjectName("label_28")
        self.timeEdit_Close_Sunday2 = QtWidgets.QTimeEdit(self.Sunday)
        self.timeEdit_Close_Sunday2.setGeometry(QtCore.QRect(150, 70, 81, 22))
        self.timeEdit_Close_Sunday2.setStyleSheet("color: black")
        self.timeEdit_Close_Sunday2.setObjectName("timeEdit_Close_Sunday2")
        self.label_29 = QtWidgets.QLabel(self.Sunday)
        self.label_29.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_29.setObjectName("label_29")
        self.timeEdit_Close_Sunday1 = QtWidgets.QTimeEdit(self.Sunday)
        self.timeEdit_Close_Sunday1.setGeometry(QtCore.QRect(150, 20, 81, 22))
        self.timeEdit_Close_Sunday1.setStyleSheet("color: black")
        self.timeEdit_Close_Sunday1.setObjectName("timeEdit_Close_Sunday1")
        self.label_30 = QtWidgets.QLabel(self.Sunday)
        self.label_30.setGeometry(QtCore.QRect(160, 0, 51, 16))
        self.label_30.setObjectName("label_30")
        self.timeEdit_Open_Sunday2 = QtWidgets.QTimeEdit(self.Sunday)
        self.timeEdit_Open_Sunday2.setGeometry(QtCore.QRect(10, 70, 81, 22))
        self.timeEdit_Open_Sunday2.setStyleSheet("color: black")
        self.timeEdit_Open_Sunday2.setObjectName("timeEdit_Open_Sunday2")
        self.toolBox.addItem(self.Sunday, "")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(80, 210, 141, 31))
        self.label_31.setStyleSheet("background: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(225,225,225);")
        self.label_31.setObjectName("label_31")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(380, 240, 341, 151))
        self.textEdit.setStyleSheet("background-color:rgb(188, 188, 188,60);\n"
"border: transparent;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_Create_Store = QtWidgets.QPushButton(self.frame)
        self.pushButton_Create_Store.setGeometry(QtCore.QRect(380, 470, 151, 51))
        self.pushButton_Create_Store.setStyleSheet("background-color: rgb(20, 100, 246);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_Create_Store.setObjectName("pushButton_Create_Store")

        self.pushButton_Cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(550, 470, 151, 51))
        self.pushButton_Cancel.setStyleSheet("background-color: rgb(164, 164, 164);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_Cancel.setObjectName("pushButton_Create_Store")


        self.Name_app_4.raise_()
        self.Name_app_2.raise_()
        self.Name_app.raise_()
        self.Name_app_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_2.raise_()
        self.toolBox.raise_()
        self.label_31.raise_()
        self.textEdit.raise_()
        self.pushButton_Create_Store.raise_()
        self.pushButton_Cancel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def actualizar(self):
        self.name = self.lineEdit.text()
        self.address = self.lineEdit2.text()
        self.number = self.lineEdit3.text()
        self.description = self.textEdit.text()
        self.schedule = []

        '''if self.checkBox_accept_terms.isChecked():
                                    self.terms = 1
                                else:
                                    self.terms = 0
                                self.phone = self.campo_phone_number.text()'''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_app.setText(_translate("MainWindow", "InfoPlaces"))
        self.Name_app_2.setText(_translate("MainWindow", "InfoPlaces"))
        self.Name_app_3.setText(_translate("MainWindow", "Register Store"))
        self.Name_app_4.setText(_translate("MainWindow", "Register Store"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Store Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Address"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Number"))
        self.label_2.setText(_translate("MainWindow", "Description:"))
        self.label_3.setText(_translate("MainWindow", "Open"))
        self.label_4.setText(_translate("MainWindow", "Close"))
        self.label_5.setText(_translate("MainWindow", "Open"))
        self.label_6.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Monday), _translate("MainWindow", "Monday"))
        self.label_7.setText(_translate("MainWindow", "Open"))
        self.label_8.setText(_translate("MainWindow", "Open"))
        self.label_9.setText(_translate("MainWindow", "Close"))
        self.label_10.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Tuesday), _translate("MainWindow", "Tuesday"))
        self.label_11.setText(_translate("MainWindow", "Open"))
        self.label_12.setText(_translate("MainWindow", "Open"))
        self.label_13.setText(_translate("MainWindow", "Close"))
        self.label_14.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Wednesday), _translate("MainWindow", "Wednesdy"))
        self.label_15.setText(_translate("MainWindow", "Open"))
        self.label_16.setText(_translate("MainWindow", "Open"))
        self.label_17.setText(_translate("MainWindow", "Close"))
        self.label_18.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Thursday), _translate("MainWindow", "Thursday"))
        self.label_19.setText(_translate("MainWindow", "Open"))
        self.label_20.setText(_translate("MainWindow", "Open"))
        self.label_21.setText(_translate("MainWindow", "Close"))
        self.label_22.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Friday), _translate("MainWindow", "Friday"))
        self.label_23.setText(_translate("MainWindow", "Open"))
        self.label_24.setText(_translate("MainWindow", "Open"))
        self.label_25.setText(_translate("MainWindow", "Close"))
        self.label_26.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Saturday), _translate("MainWindow", "Saturday"))
        self.label_27.setText(_translate("MainWindow", "Open"))
        self.label_28.setText(_translate("MainWindow", "Open"))
        self.label_29.setText(_translate("MainWindow", "Close"))
        self.label_30.setText(_translate("MainWindow", "Close"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Sunday), _translate("MainWindow", "Sunday"))
        self.label_31.setText(_translate("MainWindow", "Attention day:"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Store description"))
        self.pushButton_Create_Store.setText(_translate("MainWindow", "Create Store"))
        self.pushButton_Cancel.setText(_translate("MainWindow","Cancel"))

'''import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
