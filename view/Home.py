# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append('../model')
from PyQt5 import QtCore, QtGui, QtWidgets
from db_connection import DBconn
from model_Shop import Shop

class HomeView(object):
    def __init__(self, MainWindow, user,b):
        self.shopPosition = None
        self.buttonList = []
        self.busqueda = ""
        self.numeroResultados = str(len(b))
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
        self.results = QtWidgets.QLabel(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(500, 120, 211, 22))
        self.results.setObjectName("results")
        self.results.setStyleSheet("background: transparent;\n"
            "color: rgb(0,0,0);")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setStyleSheet("background-color: rgb(3, 48, 118,180);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(30, 210, 121, 221))
        self.groupBox.setStyleSheet("background: transparent;\n"
"border: transparent;\n"
"color: rgb(225,225,225);")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 84, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_Sports = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Sports.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Sports.setObjectName("radioButton_Sports")
        self.verticalLayout.addWidget(self.radioButton_Sports)
        self.radioButton_Restaurant = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Restaurant.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Restaurant.setObjectName("radioButton_Restaurant")
        self.verticalLayout.addWidget(self.radioButton_Restaurant)
        self.radioButton_Kitchen = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Kitchen.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Kitchen.setObjectName("radioButton_Kitchen")
        self.verticalLayout.addWidget(self.radioButton_Kitchen)
        self.radioButton_Gardening = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Gardening.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Gardening.setObjectName("radioButton_Gardening")
        self.verticalLayout.addWidget(self.radioButton_Gardening)
        self.radioButton_Bookstore = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Bookstore.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Bookstore.setObjectName("radioButton_Bookstore")
        self.verticalLayout.addWidget(self.radioButton_Bookstore)
        self.radioButton_Toy_store = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Toy_store.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Toy_store.setObjectName("radioButton_Toy_store")
        self.verticalLayout.addWidget(self.radioButton_Toy_store)
        self.radioButton_Tools = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Tools.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Tools.setObjectName("radioButton_Tools")
        self.verticalLayout.addWidget(self.radioButton_Tools)
        self.radioButton_Other = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_Other.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_Other.setObjectName("radioButton_Other")
        self.verticalLayout.addWidget(self.radioButton_Other)
        self.radioButton_All = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_All.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_All.setChecked(True)
        self.radioButton_All.setObjectName("radioButton_All")
        self.verticalLayout.addWidget(self.radioButton_All)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 440, 120, 141))
        self.groupBox_2.setStyleSheet("background: transparent;\n"
"border: transparent;\n"
"color: rgb(225,225,225);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_5estrella = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5estrella.setGeometry(QtCore.QRect(11, 24, 19, 16))
        self.checkBox_5estrella.setText("")
        self.checkBox_5estrella.setObjectName("checkBox_5estrella")
        self.checkBox_4estrella = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4estrella.setGeometry(QtCore.QRect(11, 46, 16, 16))
        self.checkBox_4estrella.setText("")
        self.checkBox_4estrella.setObjectName("checkBox_4estrella")
        self.checkBox_3estrella = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3estrella.setGeometry(QtCore.QRect(11, 68, 16, 16))
        self.checkBox_3estrella.setText("")
        self.checkBox_3estrella.setObjectName("checkBox_3estrella")
        self.checkBox_2_estrella = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2_estrella.setGeometry(QtCore.QRect(11, 90, 16, 16))
        self.checkBox_2_estrella.setText("")
        self.checkBox_2_estrella.setObjectName("checkBox_2_estrella")
        self.checkBox_1estrella = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_1estrella.setGeometry(QtCore.QRect(11, 112, 16, 16))
        self.checkBox_1estrella.setText("")
        self.checkBox_1estrella.setObjectName("checkBox_1estrella")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 24, 51, 16))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/dfsfsd/5_estrella.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 46, 51, 16))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/dfsfsd/4_estrella.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 68, 51, 16))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/dfsfsd/3_estrella.PNG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 51, 16))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/dfsfsd/2_estrella.PNG"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 112, 51, 16))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/dfsfsd/1_estrella.PNG"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.Search = QtWidgets.QLineEdit(self.frame)
        self.Search.setGeometry(QtCore.QRect(170, 50, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Search.setFont(font)
        self.Search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Search.setCursorPosition(0)
        self.Search.setObjectName("Search")
        self.Photo = QtWidgets.QLabel(self.frame)
        self.Photo.setGeometry(QtCore.QRect(700, 10, 88, 78))
        self.Photo.setStyleSheet("background: transparent;\n"
"")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap(user.image))
        self.Photo.setScaledContents(True)
        self.Photo.setObjectName("Photo")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(15, 35, 140, 140))
        self.label_7.setStyleSheet("background:transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../view/InfoPlaces-Logo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 200, 141, 381))
        self.frame_2.setStyleSheet("background: rgb(225,225,225,60);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_Log_Out = QtWidgets.QPushButton(self.frame)
        self.pushButton_Log_Out.setGeometry(QtCore.QRect(710, 90, 71, 23))
        self.pushButton_Log_Out.setAutoFillBackground(False)
        self.pushButton_Log_Out.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_Log_Out.setObjectName("pushButton_Log_Out")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(180, 143, 601, 451))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background: transparent;\n"
"border: transparent;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(131)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(570, 120, 211, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 6px")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame_camu = QtWidgets.QFrame(self.frame)
        self.frame_camu.setGeometry(QtCore.QRect(640, 50, 51, 41))
        self.frame_camu.setStyleSheet("background: white;\n"
"border-radius: 6px")
        self.frame_camu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_camu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_camu.setObjectName("frame_camu")
        self.label_11 = QtWidgets.QLabel(self.frame_camu)
        self.label_11.setGeometry(QtCore.QRect(10, 4, 41, 31))
        self.label_11.setStyleSheet("background: transparent;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/dfsfsd/buscador.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_Search = QtWidgets.QPushButton(self.frame_camu)
        self.pushButton_Search.setGeometry(QtCore.QRect(10, 0, 41, 41))
        self.pushButton_Search.setStyleSheet("background: transparent;")
        self.pushButton_Search.setText("")
        self.pushButton_Search.setObjectName("pushButton")        
        self.frame_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.Search.raise_()
        self.Photo.raise_()
        self.label_7.raise_()
        self.pushButton_Log_Out.raise_()
        self.comboBox.raise_()
        self.pushButton_Search.raise_()
        self.frame_camu.raise_()
        self.tableWidget.raise_()

        if user.type != 3:
            self.perfil = QtWidgets.QPushButton(self.frame)
            self.perfil.setGeometry(QtCore.QRect(700, 10, 88, 78))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.perfil.setFont(font)
            self.perfil.setStyleSheet("background: transparent;")
            self.perfil.setObjectName("perfil")
            self.ver_favoritos = QtWidgets.QPushButton(self.frame)
            self.ver_favoritos.setGeometry(QtCore.QRect(187, 120,75,21))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.ver_favoritos.setFont(font)
            self.ver_favoritos.setStyleSheet("background: rgb(225,225,225,60);\n"
                                        "border: 1px solid rgb(225,225,225,60);\n"
                                        "border-radius: 6px;\n"
                                        "color: rgb(225,225,225);")
            self.ver_favoritos.setObjectName("ver_favoritos")
            self.ver_favoritos.raise_()
            self.perfil.raise_()
            if user.type == 2:
                self.misTiendas = QtWidgets.QPushButton(self.frame)
                self.misTiendas.setGeometry(QtCore.QRect(35,175,91,21))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.misTiendas.setFont(font)
                self.misTiendas.setStyleSheet("background: rgb(225,225,225,60);\n"
                                             "border: 1px solid rgb(225,225,225,60);\n"
                                            "border-radius: 6px;\n"
                                            "color: rgb(225,225,225);")
                self.misTiendas.setObjectName("misTiendas")
                self.misTiendas.raise_()
                self.pushButton_Create_Store = QtWidgets.QPushButton(self.frame)
                self.pushButton_Create_Store.setGeometry(QtCore.QRect(317, 0, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(False)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(50)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.pushButton_Create_Store.setFont(font)
                self.pushButton_Create_Store.setStyleSheet("background: rgb(225,225,225,60);\n"
                                                        "border: 1px solid rgb(225,225,225,60);\n"
                                                        "border-radius: 6px;\n"
                                                        "color: rgb(225,225,225);")
                self.pushButton_Create_Store.setObjectName("pushButton_Create_Store")
                self.pushButton_Create_Store.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow,user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Cargar_tienda(b)
        MainWindow.show()

    def update(self):
        self.busqueda = self.Search.text()

    def Cargar_tienda(self,consulta):
        tiendas = consulta
        self.numeroResultados = str(len(tiendas))
        self.results.setText("Results: "+self.numeroResultados)
        self.results.setStyleSheet("background: transparent;")
        self.tableWidget.setRowCount(len(tiendas))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        columna = 0

        for i in range(len(tiendas)):
            tienda = tiendas[i]
            imagen = tienda[0]
            nombre = tienda[1]
            rating = tienda[5]
            descripcion = tienda[2]
            caja = QtWidgets.QHBoxLayout()
            # Crea las imagenes de la tiendas
            imagen_tienda = QtWidgets.QLabel(self.tableWidget)
            imagen_tienda.setGeometry(QtCore.QRect(0,0,100,50))
            imagen_tienda.setText("")
            imagen_tienda.setPixmap(QtGui.QPixmap(imagen))
            imagen_tienda.setScaledContents(True)
            imagen_tienda.setObjectName("imagen_tienda")
            imagen_tienda.setMaximumSize(181,131)

            caja.addWidget(imagen_tienda)
            celda = QtWidgets.QWidget()
            #celda.setStyleSheet("background: green")
            celda.setLayout(caja)

            self.boton_Tienda(i,imagen_tienda)

            textBrowser = QtWidgets.QTextBrowser(self.tableWidget)
            textBrowser.setGeometry(QtCore.QRect(0, 0, 368, 131))
            textBrowser.setMinimumSize(368,131)
            textBrowser.setMaximumSize(368,131)
            textBrowser.setStyleSheet("background: rgb(225,225,225,60);\n"
    "border: 1px solid rgb(225,225,225,60);\n"
    "border-radius: 6px;\n"
    "color: rgb(225,225,225);")
            textBrowser.setPlaceholderText("")

            _translate = QtCore.QCoreApplication.translate
            textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<b style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(nombre)+"</b>"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(descripcion)+"</p></body></html>"))

            textBrowser.setObjectName("textBrowser")
            caja2 = QtWidgets.QHBoxLayout()
            caja2.addWidget(textBrowser)
            celda2 = QtWidgets.QWidget()
            celda2.setLayout(caja2)
            self.tableWidget.setCellWidget(i,1,celda2)
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()

            # agregar el texto de la descripcion de la tienda y el nombre en el momento que se crea la tienda.

            self.tableWidget.setCellWidget(i,0,celda)
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()
            columna = columna + 1

    def clickedo(self,boton, posicion):
            self.shopPosition = posicion
            fila = self.tableWidget.currentRow()
    
    def boton_Tienda(self,posicion,img):
        nombreboton = "pushButton_tienda" + str(posicion)
        pushButton_tienda = QtWidgets.QPushButton(img)
        self.buttonList.append(pushButton_tienda)
        pushButton_tienda.setGeometry(QtCore.QRect(0,0,181,131))
        pushButton_tienda.setAutoFillBackground(False)
        pushButton_tienda.setStyleSheet("background: transparent;")
        pushButton_tienda.setObjectName(nombreboton)
        pushButton_tienda.clicked.connect(lambda: self.clickedo(pushButton_tienda, posicion))
    
    def retranslateUi(self, MainWindow,user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Type"))
        self.radioButton_Sports.setText(_translate("MainWindow", "Sports"))
        self.radioButton_Restaurant.setText(_translate("MainWindow", "Restaurant"))
        self.radioButton_Kitchen.setText(_translate("MainWindow", "Kitchen"))
        self.radioButton_Gardening.setText(_translate("MainWindow", "Gardening"))
        self.radioButton_Bookstore.setText(_translate("MainWindow", "Bookstrore"))
        self.radioButton_Toy_store.setText(_translate("MainWindow", "Toy store"))
        self.radioButton_Tools.setText(_translate("MainWindow", "Tools"))
        self.radioButton_Other.setText(_translate("MainWindow", "Other"))
        self.radioButton_All.setText(_translate("MainWindow", "All"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Valoración"))
        self.Search.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.pushButton_Log_Out.setText(_translate("MainWindow", "Log Out"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sort by"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Descendent Rate"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ascendent Rate"))
        self.comboBox.setItemText(3, _translate("MainWindow", "A-Z"))
        self.comboBox.setItemText(4, _translate("MainWindow", "A-A"))
        self.pushButton_Search.setText(_translate("MainWindow", ""))
        self.results.setText(_translate("MainWindow", "Results: "+self.numeroResultados))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Imagen"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        self.pushButton_Search.setText(_translate("MainWindow", ""))
        if user.type != 3:
            self.perfil.setText(_translate("MainWindow",""))
            self.ver_favoritos.setText(_translate("MainWindow","Favorites"))
            if user.type == 2:
                self.misTiendas.setText(_translate("MainWindow", "My Shops"))
                self.pushButton_Create_Store.setText(_translate("MainWindow", "Create Store"))