# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Store.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class StoreDescriptionView(object):
    def __init__(self, MainWindow, description, images, schedule, user, com):
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
        self.ImagenShop.setPixmap(QtGui.QPixmap(images[0][3]))
        self.ImagenShop.setScaledContents(True)
        self.ImagenShop.setObjectName("ImagenShop")
        self.Photo = QtWidgets.QLabel(self.frame)
        self.Photo.setGeometry(QtCore.QRect(720, 10, 71, 61))
        self.Photo.setStyleSheet("background: transparent;\n"
"")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap(user.image))
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
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(250, 371, 511, 61))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255,200);\n"
"border: transparent;\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px 0px;\n"
"border-top-right-radius: 0px 0px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_SendComent = QtWidgets.QPushButton(self.frame)
        self.pushButton_SendComent.setGeometry(QtCore.QRect(700, 430, 61, 20))
        self.pushButton_SendComent.setStyleSheet("background-color: rgb(20,100,246);\n"
"border: 1px solid rgb(225,225,225);\n"
"border-radius: 6px;\n"
"color: rgb(225,225,225);\n"
"")
        self.pushButton_SendComent.setObjectName("pushButton_SendComent")
        self.textBrowser_SheduleShop = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_SheduleShop.setGeometry(QtCore.QRect(20, 241, 211, 181))
        self.textBrowser_SheduleShop.setStyleSheet("background-color: rgb(254, 252, 224,60);\n"
"border: transparent;\n"
"border-radius: 3px;\n"
"color: rgb(225,225,225)")
        self.textBrowser_SheduleShop.setObjectName("textBrowser_SheduleShop")
        self.Gallery = QtWidgets.QLabel(self.frame)
        self.Gallery.setGeometry(QtCore.QRect(254, 434, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Gallery.setFont(font)
        self.Gallery.setStyleSheet("background: transparent;\n"
"color: rgb(225,225,225)")
        self.Gallery.setObjectName("Gallery")
        self.tableWidget_Galeria = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_Galeria.setGeometry(QtCore.QRect(250, 446, 511, 154))
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
        self.tableWidget_Galeria.horizontalHeader().setVisible(False)
        self.tableWidget_Galeria.horizontalHeader().setMinimumSectionSize(42)
        self.tableWidget_Galeria.verticalHeader().setVisible(False)
        self.tableWidget_Galeria.verticalHeader().setDefaultSectionSize(139)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, description, images, schedule)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Cargar_Comentarios(com)
        self.Cargar_imagenes(images)


    # Carga los comentarios
    '''
    def Cargar_Comentarios(self,consulta):
        comentario = consulta
        self.tableWidget_Comments.setRowCount(len(comentario))
        self.tableWidget_Comments.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        columna = 1
        for i in range(len(comentario)):
            coment = comentario[i]
            
            for x in coment:
                item = QTableWidgetItem(str(x))
                self.tableWidget_Comments.setItem(i,columna,item)
    '''
    def setComment(self):
        self.textEdit.clear()

    # Opción 2
    def Cargar_Comentarios(self,consulta):
        comentario = consulta
        self.tableWidget_Comments.setRowCount(len(comentario))
        self.tableWidget_Comments.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        columna = 0
        for i in range(len(comentario)):
            # foto, nombre y contenido tienen la posición "i" temporalmente hasta que sepa en que posición se hubica cada uno en la base de datos.
            coment = comentario[i]
            foto = coment[0]
            nombre = coment[1]
            contenido = coment[2]
            caja = QtWidgets.QHBoxLayout()
            foto_usuario = QtWidgets.QLabel(self.tableWidget_Comments)
            foto_usuario.setGeometry(QtCore.QRect(0,0,61,65))
            foto_usuario.setText("")
            foto_usuario.setPixmap(QtGui.QPixmap(foto))
            foto_usuario.setScaledContents(True)
            foto_usuario.setObjectName("imagen_tienda")
            foto_usuario.setMaximumSize(61,65)
            caja.addWidget(foto_usuario)
            celda = QtWidgets.QWidget()
            celda.setLayout(caja)

            textBrowser = QtWidgets.QTextBrowser(self.tableWidget_Comments)
            textBrowser.setGeometry(QtCore.QRect(0, 0, 393, 40))
            textBrowser.setMinimumSize(393,40)
            textBrowser.setMaximumSize(393,40)
            textBrowser.setStyleSheet("background: transparent;\n"
                                        "border-radius: 20px solid;")
            textBrowser.setPlaceholderText("")

            _translate = QtCore.QCoreApplication.translate
            textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<b style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(nombre)+"</b>"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(contenido)+"</p></body></html>"))

            textBrowser.setObjectName("textBrowser")
            caja2 = QtWidgets.QHBoxLayout()
            caja2.addWidget(textBrowser)
            celda2 = QtWidgets.QWidget()
            #celda2.setBaseSize(371,151)
            #celda2.setStyleSheet("background: red;")
            celda2.setLayout(caja2)
            self.tableWidget_Comments.setCellWidget(i,1,celda2)
            self.tableWidget_Comments.resizeRowsToContents()
            self.tableWidget_Comments.resizeColumnsToContents()

            # agregar el texto de la descripcion de la tienda y el nombre en el momento que se crea la tienda.

            self.tableWidget_Comments.setCellWidget(i,0,celda)
            self.tableWidget_Comments.resizeRowsToContents()
            self.tableWidget_Comments.resizeColumnsToContents()

            
            
            columna = columna + 1

    def Cargar_imagenes(self, consulta):
        imagenes = consulta
        print('estoy imprimiendo las imagenes de prueba: ',imagenes)
        self.tableWidget_Galeria.setColumnCount(len(imagenes))
        self.tableWidget_Galeria.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        columna = 0

        for i in range(len(imagenes)):
            imag = imagenes[i]
            img = imag[3]
            imagen_predeterminada = "../view/image.png"
            if img != imagen_predeterminada:
                caja = QtWidgets.QHBoxLayout()
                imagen_tienda = QtWidgets.QLabel(self.tableWidget_Galeria)
                imagen_tienda.setGeometry(QtCore.QRect(0,0,100,60))
                imagen_tienda.setText("")
                imagen_tienda.setPixmap(QtGui.QPixmap(img))
                imagen_tienda.setScaledContents(True)
                imagen_tienda.setObjectName("imagen_tienda")
                imagen_tienda.setMaximumSize(181,128)
                caja.addWidget(imagen_tienda)
                celda = QtWidgets.QWidget()
                celda.setLayout(caja)
                self.tableWidget_Galeria.setCellWidget(0,columna,celda)
                self.tableWidget_Galeria.resizeRowsToContents()
                self.tableWidget_Galeria.resizeColumnsToContents()
                columna = columna + 1


    def retranslateUi(self, MainWindow, description, images, schedule):
        p = int(len(schedule))
        horario = ''
        for i in range(p//2):
            a = str(schedule[i][2]) + ': ' + str(schedule[i][4]) + ':' + str(schedule[i][5]) + 'hs. to ' + str(schedule[i][6]) + ':' + str(schedule[i][7]) + 'hs. '
            horario = horario + a
            #print(horario) muestra la hora en la consola


        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_DescripctioShop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+description[0][2]+"</p></body></html>"))
        self.label_Description.setText(_translate("MainWindow", "Description:"))
        self.Label_Name_Shop.setText(_translate("MainWindow", description[0][1]))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        item = self.tableWidget_Comments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_Comments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "coments"))
        self.textBrowser_SheduleShop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+horario+"</p></body></html>"))
        item = self.tableWidget_Galeria.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Img"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Deje su comentario en este cuadrito =D"))
        self.pushButton_SendComent.setText(_translate("MainWindow", "Send"))
        self.Gallery.setText(_translate("MainWindow","Gallery"))

'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''

