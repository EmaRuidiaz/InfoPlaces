# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ventana_Principal(object):
    def setupUi(self, Ventana_Principal):
        Ventana_Principal.setObjectName("Ventana_Principal")
        Ventana_Principal.resize(314, 287)
        self.centralwidget = QtWidgets.QWidget(Ventana_Principal)
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
        Ventana_Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Principal)
        self.statusbar.setObjectName("statusbar")
        Ventana_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Principal)
        return self.pushButton.clicked.connect(self.adelante)
        return self.pushButton_2.clicked.connect(self.atras)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Principal)

    def adelante(self):
        self.op = "2"
    def atras(self):
        self.op = "3"

    def retranslateUi(self, Ventana_Principal):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Principal.setWindowTitle(_translate("Ventana_Principal", "MainWindow"))
        self.pushButton.setText(_translate("Ventana_Principal", ">"))
        self.pushButton_2.setText(_translate("Ventana_Principal", "<"))
        self.label.setText(_translate("Ventana_Principal", "1"))


class ventana1():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Principal()
    ui.setupUi(Ventana_Principal)
    Ventana_Principal.show()

    sys.exit(app.exec_())

