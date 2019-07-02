# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class HomeView(object):
    def __init__(self, MainWindow, user):
        self.busqueda = ""
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
        self.checkBox_5estrella.toggle()
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
        '''self.pushButton_back = QtWidgets.QPushButton(self.frame)
                                self.pushButton_back.setGeometry(QtCore.QRect(0, 0, 61, 23))
                                self.pushButton_back.setAutoFillBackground(False)
                                self.pushButton_back.setStyleSheet("background: rgb(225,225,225,60);\n"
                        "border: 1px solid rgb(225,225,225,60);\n"
                        "border-radius: 6px;\n"
                        "color: rgb(225,225,225);\n"
                        "")
                                self.pushButton_back.setObjectName("pushButton_back")'''
        self.Search = QtWidgets.QLineEdit(self.frame)
        self.Search.setGeometry(QtCore.QRect(170, 50, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Search.setFont(font)
        self.Search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Search.setCursorPosition(0)
        self.Search.setObjectName("Search")

        
        #self.perfil.setText("")
        '''
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(420, 0, 75, 21))
        self.pushButton.setStyleSheet("background: rgb(225,225,225,60);\n"
"border: 1px solid rgb(225,225,225,60);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);")
        self.pushButton.setObjectName("pushButton")
'''
        self.Photo = QtWidgets.QLabel(self.frame)
        self.Photo.setGeometry(QtCore.QRect(700, 10, 91, 81))
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
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(170, 140, 611, 431))
        self.scrollArea.setStyleSheet("background:transparent;\n"
"border: transprent;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 611, 431))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 181, 131))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Tienda/Adidas-Splau-650.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 181, 131))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/Tienda/image_content_7298511_20160625221849.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 181, 131))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/Tienda/resizeimg.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(210, 10, 391, 131))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.titulo_tienda1 = QtWidgets.QLabel(self.frame_3)
        self.titulo_tienda1.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titulo_tienda1.setFont(font)
        self.titulo_tienda1.setObjectName("titulo_tienda1")
        self.textBrowser_Descripcion1 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_Descripcion1.setGeometry(QtCore.QRect(10, 30, 371, 71))
        self.textBrowser_Descripcion1.setObjectName("textBrowser_Descripcion1")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setGeometry(QtCore.QRect(210, 290, 391, 131))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.titulo_tienda3 = QtWidgets.QLabel(self.frame_4)
        self.titulo_tienda3.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titulo_tienda3.setFont(font)
        self.titulo_tienda3.setObjectName("titulo_tienda3")
        self.textBrowser_Descripcion3 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_Descripcion3.setGeometry(QtCore.QRect(10, 30, 371, 71))
        self.textBrowser_Descripcion3.setObjectName("textBrowser_Descripcion3")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setGeometry(QtCore.QRect(210, 150, 391, 131))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.titulo_tienda2 = QtWidgets.QLabel(self.frame_5)
        self.titulo_tienda2.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titulo_tienda2.setFont(font)
        self.titulo_tienda2.setObjectName("titulo_tienda2")
        self.textBrowser_Descripcion2 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_Descripcion2.setGeometry(QtCore.QRect(10, 30, 371, 71))
        self.textBrowser_Descripcion2.setObjectName("textBrowser_Descripcion2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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

        self.pushButton_Search = QtWidgets.QPushButton(self.frame)
        self.pushButton_Search.setGeometry(QtCore.QRect(638, 94, 50, 20))
        self.pushButton_Search.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.pushButton_Search.setObjectName("pushButton")

        if user.type != 3:
            self.perfil = QtWidgets.QPushButton(self.frame)
            self.perfil.setGeometry(QtCore.QRect(420, 0, 91, 21))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.perfil.setFont(font)
            self.perfil.setStyleSheet("background: rgb(225,225,225,60);\n"
                                        "border: 1px solid rgb(225,225,225,60);\n"
                                        "border-radius: 6px;\n"
                                        "color: rgb(225,225,225);")
            self.perfil.setObjectName("perfil")
            self.perfil.raise_()
            if user.type == 2:
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
        self.frame_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        #self.pushButton_back.raise_()
        self.Search.raise_()
        self.Photo.raise_()
        self.label_7.raise_()
        self.pushButton_Log_Out.raise_()
        self.scrollArea.raise_()
        self.comboBox.raise_()
        self.pushButton_Search.raise_()

        #self.pushButton_Search.clicked.connect(lambda: self.update())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow,user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


        MainWindow.show()

    def update(self):
        self.busqueda = self.Search.text()
        print("La busqueda es ",self.busqueda)

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
        self.titulo_tienda1.setText(_translate("MainWindow", "Store_1"))
        self.textBrowser_Descripcion1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description_1</p></body></html>"))
        self.titulo_tienda3.setText(_translate("MainWindow", "Store_3"))
        self.textBrowser_Descripcion3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description_3</p></body></html>"))
        self.titulo_tienda2.setText(_translate("MainWindow", "Store_2"))
        self.textBrowser_Descripcion2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description_2</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sort by"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Descendent Rate"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ascendent Rate"))
        self.comboBox.setItemText(3, _translate("MainWindow", "A-Z"))
        self.comboBox.setItemText(4, _translate("MainWindow", "A-A"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))
        if user.type != 3:
            self.perfil.setText(_translate("MainWindow","Edit Profile"))
            if user.type == 2:
                self.pushButton_Create_Store.setText(_translate("MainWindow", "Create Store"))


'''
import imagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    sys.exit(app.exec_())

'''