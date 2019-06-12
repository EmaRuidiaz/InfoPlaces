import sys
# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class IniciarSesionView(object):


    def __init__(self,Ventana_1):
        #self.controlador = Controller()
        Ventana_1.setObjectName("Iniciar Sesion")
        Ventana_1.resize(314, 287)
        self.centralwidget = QtWidgets.QWidget(Ventana_1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Ventana_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        Ventana_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_1)
        self.statusbar.setObjectName("statusbar")
        Ventana_1.setStatusBar(self.statusbar)
        Ventana_1.show()
        print("Holaaaaaa desde UI")
        

        self.retranslateUi(Ventana_1)
        #self.pushButton.clicked.connect(self.adelante)
        self.valor=0
        #self.pushButton_2.clicked.connect(lambda: self.adelante2())
        #self.pushButton_2.clicked.connect(lambda: self.mostrar(self.valor))
        QtCore.QMetaObject.connectSlotsByName(Ventana_1)

    def adelante2(self):
        print ("testeo1 entre")
        self.valor = "33423432"
        return self.valor



    def adelante(self):
        self.op = "2"
        return self.op


    def atras(self):
        return "3"

    def retranslateUi(self, Ventana_1):
        _translate = QtCore.QCoreApplication.translate
        Ventana_1.setWindowTitle(_translate("Ventana_Principal", "MainWindow"))
        self.pushButton.setText(_translate("Ventana_Principal", ">"))
        self.pushButton_2.setText(_translate("Ventana_Principal", "<"))
        self.label.setText(_translate("Ventana_Principal", "1"))




class Ui_Ventana_2(object):
    def setupUi(self, Ventana_2):
        Ventana_2.setObjectName("Ventana_2")
        Ventana_2.resize(314, 287)
        self.centralwidget = QtWidgets.QWidget(Ventana_2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Ventana_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        Ventana_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_2)
        self.statusbar.setObjectName("statusbar")
        Ventana_2.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_2)
        self.pushButton.clicked.connect(self.v.imprimir)
        self.pushButton_2.clicked.connect(self.pushButton_2.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Ventana_2)

    def adelante(self):
        return "3"

    def atras(self):
        return "1"

    def retranslateUi(self, Ventana_2):
        _translate = QtCore.QCoreApplication.translate
        Ventana_2.setWindowTitle(_translate("Ventana_Principal", "MainWindow"))
        self.pushButton.setText(_translate("Ventana_Principal", ">"))
        self.pushButton_2.setText(_translate("Ventana_Principal", "<"))
        self.label.setText(_translate("Ventana_Principal", "2"))

class Ui_Ventana_3(object):
    def setupUi(self, Ventana_3):
        Ventana_3.setObjectName("Ventana_3")
        Ventana_3.resize(314, 287)
        self.centralwidget = QtWidgets.QWidget(Ventana_3)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Ventana_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        Ventana_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_3)
        self.statusbar.setObjectName("statusbar")
        Ventana_3.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_3)
        self.pushButton.clicked.connect(self.pushButton.setFocus)
        self.pushButton_2.clicked.connect(self.pushButton_2.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Ventana_3)

    def adelante(self):

        return "1"

    def atras(self):
        return "2"

    def retranslateUi(self, Ventana_3):
        _translate = QtCore.QCoreApplication.translate
        Ventana_3.setWindowTitle(_translate("Ventana_Principal", "MainWindow"))
        self.pushButton.setText(_translate("Ventana_Principal", ">"))
        self.pushButton_2.setText(_translate("Ventana_Principal", "<"))
        self.label.setText(_translate("Ventana_Principal", "3"))
