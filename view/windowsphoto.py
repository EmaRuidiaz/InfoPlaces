from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys

from PyQt5.QtGui import QPixmap
 
 
 
 
 
 
 
class WindowPhoto(QWidget):
  def __init__(self):
    super().__init__()

    self.title = "PyQt5 Open File"
    self.top = 200
    self.left = 500
    self.width = 400
    self.height = 300


    #self.InitWindow()
 

  def InitWindow(self, window):
    window.setWindowIcon(QtGui.QIcon("icon.png"))
    window.setWindowTitle(self.title)
    window.setGeometry(self.left, self.top, self.width, self.height)

    vbox = QVBoxLayout()

    self.btn1 = QPushButton("Open Image")
    self.btn1.clicked.connect(self.getImage)

    vbox.addWidget(self.btn1)

    self.label = QLabel("Hello")
    vbox.addWidget(self.label)

    window.setLayout(vbox)
    window.show()

  def getImage(self):
    fname = QFileDialog.getOpenFileName(self, 'Open file')
    imagePath = fname[0]
    print(imagePath)
    pixmap = QPixmap(imagePath)
    self.label.setPixmap(QPixmap(pixmap))
    self.resize(97, 64)


'''def fileSave(self, imagePath):
    import datetime, time
    d = datetime.datetime.utcnow()
    datetime_in_microseconds_creo = int(time.mktime(d.timetuple())) * 1000

    with open(imagePath, 'rb') as f:
      data = f.read()

    new_route = './images'
    extension = imagePath.split('.').pop()
    new_route_name_img = f'{new_route}/{datetime_in_microseconds_creo}.{extension}'
    
    with open(new_route_name_img, 'wb') as f:
      f.write(data)
 
App = QApplication(sys.argv)
window = Window()
'''