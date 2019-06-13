import sys
sys.path.append('../connection')

import db_connection


from PyQt5 import QtCore, QtGui, QtWidgets

import os


class Controller():

	def __init__(self):
		pass
		
	def Iniciar(self):
		import sys
		app = QtWidgets.QApplication(sys.argv)
		Ventana_Principal = QtWidgets.QMainWindow()
		print("abajo de 1")
		ISV = IniciarSesionView(Ventana_Principal)
		print("abajo de 2")
		print("abajo de 3")
		sys.exit(app.exec_())
		print("abajo de exit")
		

	def iniciar_busqueda(self):
		print("Inicio Busqueda")

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

class IniciarSesionView(object):


    def __init__(self, Ventana_1):
        self.op = ""
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
        

        #self.retranslateUi(Ventana_1)
        self.pushButton.clicked.connect(self.adelante(Ventana_1(self)))

        self.pushButton_2.clicked.connect(self.adelante2(Ventana_1(self)))
        QtCore.QMetaObject.connectSlotsByName(Ventana_1)

    def adelante2(self, v):
        v.close()
        return self.op

    def adelante(self, v):
        self.op = "2"
        v.close()
        return self.op



cs = Controller()
cs.Iniciar()