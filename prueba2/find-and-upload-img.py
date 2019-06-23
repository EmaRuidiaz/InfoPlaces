from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys

from PyQt5.QtGui import QPixmap
 
 
 
 
 
 
 
class Window(QWidget):
  def __init__(self):
    super().__init__()

    #Crea la ventana contenedora
    self.title = "PyQt5 Open File"
    self.top = 200
    self.left = 500
    self.width = 400
    self.height = 300


    self.InitWindow()
 

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon("icon.png"))
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    vbox = QVBoxLayout()

    self.btn1 = QPushButton("Open Image") #Boton para agregar imagen
    self.btn1.clicked.connect(self.getImage) #La conexión del boton con la función para agregar imagen

    vbox.addWidget(self.btn1)

    self.label = QLabel("Hello")
    vbox.addWidget(self.label)

    self.setLayout(vbox)
    self.show()

  def getImage(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file')
    imagePath = fname[0]
    print(imagePath)
    pixmap = QPixmap(imagePath)
    self.label.setPixmap(QPixmap(pixmap))
    self.setMinimumSize(500,500) # Tamaño minimo de la ventana
    self.setMaximumSize(500,500) # Tamaño maximo de la ventana
    self.resize(pixmap.width(), pixmap.height())
    self.label.setScaledContents(True)
    self.fileSave(imagePath) # Llama a la función para que guarde la imagen

  def fileSave(self, imagePath):
    import datetime, time
    d = datetime.datetime.utcnow()
    datetime_in_microseconds_creo = int(time.mktime(d.timetuple())) * 1000

    with open(imagePath, 'rb') as f:
      data = f.read()

    new_route = './images'
    extension = imagePath.split('.').pop() # admite cualquier tipo de extención en la imagen (Creo)
    new_route_name_img = f'{new_route}/{datetime_in_microseconds_creo}.{extension}' # Guarda con un nombre en micro segundo
    
    with open(new_route_name_img, 'wb') as f:
      f.write(data)
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())