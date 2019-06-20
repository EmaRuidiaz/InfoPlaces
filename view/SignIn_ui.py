# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        MainWindow.setWindowTitle("Sign In")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 591, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(93)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(250, 230, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 290, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(244, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 440, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(540, 240, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(590, 240, 82, 17))
        self.radioButton_2.setTabletTracking(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 530, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(93)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        MainWindow.show()
        self.retranslateUi(MainWindow)
        self.lineEdit.setPlaceholderText("  Username or Email")
        self.lineEdit_2.setPlaceholderText("  Password")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit_2.setClearButtonEnabled(True)


    def actualizar(self):
        #if self.lineEdit.is
        self.user = self.lineEdit.text()
        self.passwd = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            self.type = 1
        else:
            self.type = 2

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#3f413e;\">InfoPlaces</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#5500ff;\">InfoPlaces</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Create Account"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign In"))
        self.pushButton_3.setText(_translate("MainWindow", "Anonymous Access"))
        self.radioButton.setText(_translate("MainWindow", "User"))
        self.radioButton_2.setText(_translate("MainWindow", "Owner"))



