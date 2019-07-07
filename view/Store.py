# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Store.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.338983, y1:0.631, x2:1, y2:0, stop:0.361582 rgba(61, 139, 247, 255), stop:0.977401 rgba(3, 123, 179, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ImagenShop = QtWidgets.QLabel(self.frame)
        self.ImagenShop.setGeometry(QtCore.QRect(20, 70, 211, 141))
        self.ImagenShop.setStyleSheet("background: transparent;")
        self.ImagenShop.setText("")
        self.ImagenShop.setPixmap(QtGui.QPixmap(":/Tienda/Adidas-Splau-650.jpg"))
        self.ImagenShop.setScaledContents(True)
        self.ImagenShop.setObjectName("ImagenShop")
        self.Photo = QtWidgets.QLabel(self.frame)
        self.Photo.setGeometry(QtCore.QRect(720, 10, 71, 61))
        self.Photo.setStyleSheet("background: transparent;\n"
"")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap(":/dfsfsd/user.PNG"))
        self.Photo.setScaledContents(True)
        self.Photo.setObjectName("Photo")
        self.textBrowser_DescripctioShop = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_DescripctioShop.setGeometry(QtCore.QRect(250, 70, 511, 141))
        self.textBrowser_DescripctioShop.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"border-radius: 22px solid;\n"
"color: rgb(225,225,225);\n"
"padding-left: 10px;\n"
"padding-top: 5px;\n"
"")
        self.textBrowser_DescripctioShop.setObjectName("textBrowser_DescripctioShop")
        self.label_Description = QtWidgets.QLabel(self.frame)
        self.label_Description.setGeometry(QtCore.QRect(260, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Description.setFont(font)
        self.label_Description.setStyleSheet("background: transparent;\n"
"color: rgb(225,225,225)")
        self.label_Description.setObjectName("label_Description")
        self.Label_Name_Shop = QtWidgets.QLabel(self.frame)
        self.Label_Name_Shop.setGeometry(QtCore.QRect(20, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Label_Name_Shop.setFont(font)
        self.Label_Name_Shop.setStyleSheet("background: transparent;\n"
"color: rgb(225,225,225);")
        self.Label_Name_Shop.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Name_Shop.setObjectName("Label_Name_Shop")
        self.pushButton_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_back.setGeometry(QtCore.QRect(0, 0, 61, 23))
        self.pushButton_back.setAutoFillBackground(False)
        self.pushButton_back.setStyleSheet("background-color: rgb(20,100,246);\n"
"border: 1px solid rgb(225,225,225);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"\n"
"")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_Home = QtWidgets.QPushButton(self.frame)
        self.pushButton_Home.setGeometry(QtCore.QRect(380, 0, 61, 23))
        self.pushButton_Home.setAutoFillBackground(False)
        self.pushButton_Home.setStyleSheet("background-color: rgb(20,100,246);\n"
"border: 1px solid rgb(225,225,225);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.tableWidget_Comments = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_Comments.setGeometry(QtCore.QRect(250, 220, 511, 151))
        self.tableWidget_Comments.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"border-top-left-radius: 22px 22px;\n"
"border-top-right-radius: 22px 22px;\n"
"\n"
"\n"
"")
        self.tableWidget_Comments.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_Comments.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_Comments.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_Comments.setColumnCount(2)
        self.tableWidget_Comments.setObjectName("tableWidget_Comments")
        self.tableWidget_Comments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Comments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Comments.setHorizontalHeaderItem(1, item)
        self.tableWidget_Comments.horizontalHeader().setVisible(False)
        self.tableWidget_Comments.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_Comments.verticalHeader().setVisible(False)
        self.textComentario = QtWidgets.QTextBrowser(self.frame)
        self.textComentario.setGeometry(QtCore.QRect(250, 371, 511, 61))
        self.textComentario.setStyleSheet("background-color: rgb(255, 255, 255,200);\n"
"border: transparent;\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px 0px;\n"
"border-top-right-radius: 0px 0px;\n"
"color: rgb(225,225,225);")
        self.textComentario.setObjectName("textComentario")
        self.textBrowser_SheduleShop = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_SheduleShop.setGeometry(QtCore.QRect(20, 241, 211, 181))
        self.textBrowser_SheduleShop.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"border-radius: 3px")
        self.textBrowser_SheduleShop.setObjectName("textBrowser_SheduleShop")
        self.tableWidget_Galeria = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_Galeria.setGeometry(QtCore.QRect(250, 450, 511, 141))
        self.tableWidget_Galeria.setStyleSheet("background: transparent;\n"
"border: transparent;")
        self.tableWidget_Galeria.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_Galeria.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_Galeria.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_Galeria.setObjectName("tableWidget_Galeria")
        self.tableWidget_Galeria.setColumnCount(0)
        self.tableWidget_Galeria.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Galeria.setVerticalHeaderItem(0, item)
        self.tableWidget_Galeria.horizontalHeader().setMinimumSectionSize(42)
        self.tableWidget_Galeria.verticalHeader().setVisible(False)
        self.tableWidget_Galeria.verticalHeader().setDefaultSectionSize(139)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_DescripctioShop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here you can add a description shop</p></body></html>"))
        self.label_Description.setText(_translate("MainWindow", "Description:"))
        self.Label_Name_Shop.setText(_translate("MainWindow", "NombreApp"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        item = self.tableWidget_Comments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_Comments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "coments"))
        self.textComentario.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_Galeria.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Img"))

import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

