import sys
sys.path.append('../connection')
sys.path.append('../model')
sys.path.append('../view')
#from model import ShopOwner, Shop, Schedule
from model_RegisteredUser import RegisteredUser
from model_User import User
from model_ShopOwner import ShopOwner
from model_Shop import Shop
from model_Schedule import Schedule
from SignIn2 import IniciarSesionView
from User import UserProfileView
from UserEdit import UserEditView
from CreateAccount import CreateAccountView
from db_connection import DBconn
from RegisterStore import RegisterStoreView
from Home import HomeView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class ControllerUsuario:
	def imp(self):
		print("Controlador de usuario")


class Controller():

	def __init__(self):
		import sys
		import imagen_rc
		app = QtWidgets.QApplication(sys.argv)
		Ventana_Principal = QtWidgets.QMainWindow()
		self.menuPrincipal(Ventana_Principal)
		sys.exit(app.exec_())
		
	def Iniciar(self, Ventana_Principal):
		self.menuPrincipal(Ventana_Principal)

### falta la ventana de register, una vez hecha. el registro se podra hacer llamando a este metodo ###
	def crearCuenta(self, Ventana_Principal):
		ventana1=CreateAccountView(Ventana_Principal)
		self.reguser = RegisteredUser()
		ventana1.pushButton_Create_Account.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Create_Account.clicked.connect(lambda: self.cargarUsuario(ventana1,Ventana_Principal))
		ventana1.pushButton_cancel.clicked.connect(lambda: self.menuPrincipal(Ventana_Principal))

	def menuPrincipal(self, Ventana_Principal):
		ventana1=IniciarSesionView(Ventana_Principal)
		ventana1.pushButton_Sign_In.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Sign_In.clicked.connect(lambda: self.sign(ventana1.passwd, ventana1.user, ventana1.type,Ventana_Principal))
		ventana1.pushButton_Anonymous_access.clicked.connect(lambda: self.sign("User", "User", 3, Ventana_Principal))
		ventana1.pushButton_Create_Account.clicked.connect(lambda: self.crearCuenta(Ventana_Principal))

	def cargarUsuario(self, ventana1, Ventana_Principal):
		self.reguser.firstname = ventana1.firstname
		self.reguser.lastname = ventana1.lastname
		self.reguser.username = ventana1.username
		self.reguser.birthdate = ventana1.birthdate
		self.reguser.email = ventana1.email
		self.reguser.password = ventana1.password
		self.reguser.type = ventana1.type
		self.reguser.image = ventana1.image
		self.confirmuser = ventana1.confirmuser
		try:
			self.reguser.phone_number = int(ventana1.phone)
		except:
			if ventana1.phone:
				ventana1.terms = 0
				self.reguser.phone_number = None
			else:
				pass
		
		if ventana1.terms == 1 and (ventana1.fechacontrol < 2019) and self.reguser.firstname and self.reguser.lastname and self.reguser.username and self.reguser.email and self.reguser.password and (len(self.reguser.password) > 7) and (self.reguser.password == self.confirmuser):
			
			if not self.reguser.CheckReg():
				if self.reguser.Register():
					self.reguser.RegisterPhoto()
					QMessageBox.about(Ventana_Principal, "Registro Exitoso", "Usuario Registrado Satisfactoriamente!")
					self.menuPrincipal(Ventana_Principal)
				else:
					pass
			else:
				QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")
		else:
			QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")

	def Home(self, Ventana_Principal,user):
		ventana1 = HomeView(Ventana_Principal, user)
		try:
			ventana1.perfil.clicked.connect(lambda: self.user(Ventana_Principal, user))
			ventana1.pushButton_Create_Store.clicked.connect(lambda: self.crearStore(Ventana_Principal, user))
		except:
			pass
		ventana1.pushButton_Log_Out.clicked.connect(lambda: self.logOut(Ventana_Principal, user))

	def logOut(self, Ventana_Principal, user):
		del user
		self.menuPrincipal(Ventana_Principal)
		#self.Iniciar(Ventana_Principal)

	def sign(self, passwd=None, user=None, typeu=None, Ventana_Principal=None):
		if typeu == 1:
			print("Tipo: ", typeu)
			reguser = RegisteredUser()
			reguser.username = user
			reguser.email = user
			reguser.password = passwd
			reguser.type = typeu
			self.validacion = reguser.SignIn()
			#self.reguser.username, self.reguser.password)
			if (self.validacion):
				import sys
				import imagen_rc
				reguser.firstname = self.validacion[0][2]
				reguser.lastname = self.validacion[0][3]
				reguser.username = self.validacion[0][0]
				reguser.birthdate = self.validacion[0][6]
				reguser.email = self.validacion[0][4]
				reguser.password = self.validacion[0][5]
				reguser.type = self.validacion[0][1]
				reguser.phone_number = self.validacion[0][7]
				reguser.image = self.validacion[0][8]
				self.Home(Ventana_Principal,reguser)
			else:
				msj = QMessageBox.critical(Ventana_Principal, "Datos Incorrectos", "Por favor, intente nuevamente. Si no está registrado, puede hacerlo gratuitamente.")
		elif typeu == 2:
			print("Tipo: ", typeu)
			owner = ShopOwner()
			owner.username = user
			owner.email = user
			owner.password = passwd
			owner.type = typeu
			self.validacion = owner.SignIn()
			#self.reguser.username, self.reguser.password)
			if (self.validacion):
				import sys
				import imagen_rc
				owner.firstname = self.validacion[0][2]
				owner.lastname = self.validacion[0][3]
				owner.username = self.validacion[0][0]
				owner.birthdate = self.validacion[0][6]
				owner.email = self.validacion[0][4]
				owner.password = self.validacion[0][5]
				owner.type = self.validacion[0][1]
				owner.phone_number = self.validacion[0][7]
				owner.image = self.validacion[0][8]
				self.Home(Ventana_Principal,owner)
			else:
				QMessageBox.critical(Ventana_Principal, "Datos Incorrectos", "Por favor, intente nuevamente. Si no está registrado, puede hacerlo gratuitamente.")
		elif typeu == 3:
			user = User()
			self.Home(Ventana_Principal, user)
			#ventana1.pushButton_Log_Out.clicked.connect(lambda: self.menuPrincipal(Ventana_Principal))

	

	def crearStore(self, Ventana_Principal, user):
		self.shop = Shop()
		self.schedule = Schedule()
		ventana1 = RegisterStoreView(Ventana_Principal, user, self.shop, self.schedule)
		#ventana1.pushButton_Create_Store.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Create_Store.clicked.connect(lambda: self.AddStore(self.shop, user, ventana1, self.schedule, Ventana_Principal))
		ventana1.pushButton_Cancel.clicked.connect(lambda: self.Home(Ventana_Principal, user))

	def AddStore(self, shop, user, ventana1, schedule, Ventana_Principal):
		'''shop.name = ventana1.name
								shop.address = ventana1.address
								shop.number = ventana1.number
								shop.description = ventana1.description'''
		if shop.name and shop.address and shop.number and shop.description and ventana1.flag:
			shop.register(user)
			idShop = shop.getID()
			print("Este es el id de la tienda: ",idShop)
			shop.registerPhoto(idShop[0][0])
			print("VENTANA1.SCHEDULE: ",ventana1.schedule)
			for i in range(1,15):
				schedule.register(ventana1.schedule, idShop[0][0], i-1)
			QMessageBox.about(Ventana_Principal, "Register", "The shop was registered succefully!")
		else:
			print("Error - No se ha registrado")


	def editarUser(self, Ventana_Principal, user, userresguardo):
		import imagen_rc
		self.userresguardo = user
		ventana1 = UserEditView(Ventana_Principal, user)
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.UpdateUserEdit(user,self.userresguardo,ventana1, Ventana_Principal))
		#ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.Home(Ventana_Principal, user, user.type))
		#ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.user(Ventana_Principal, user))
		

	def UpdateUserEdit(self, user, userresguardo, ventana1, Ventana_Principal):
		self.usernameresguardo = user.username
		self.emailresguardo = user.email
		user.firstname = ventana1.firstname
		user.lastname = ventana1.lastname
		user.username = ventana1.username
		user.password = ventana1.password
		user.phone_number = ventana1.phone
		user.image = ventana1.fileName
		print("Username: ",user.username, " Username Resguardo: ",userresguardo.username)
		if user.firstname and user.lastname and user.password and (len(user.password) > 7):
			self.var = user.CheckReg()
			if len(self.var) == 0 or self.var[0][0] == self.usernameresguardo:
				user.UpdateInfo(self.usernameresguardo)
				user.UpdatePhoto(self.usernameresguardo)
				QMessageBox.about(Ventana_Principal, "Update Succefull", "Se ha actualizado correctamente sus datos.")
				self.user(Ventana_Principal, user)
			else:
				QMessageBox.warning(Ventana_Principal, "Error", "El username, el email ya está en uso")
				user = userresguardo
				user.username = self.usernameresguardo
				user.email = self.emailresguardo
				self.editarUser(Ventana_Principal, user, userresguardo)
		else:
			QMessageBox.critical(Ventana_Principal, "Error", "Datos Incompletos")
			user = userresguardo
			self.editarUser(Ventana_Principal, user, userresguardo)

	def user(self, Ventana_Principal, user):
		import imagen_rc
		ventana1 = UserProfileView(Ventana_Principal, user)
		ventana1.pushButton_back.clicked.connect(lambda: self.Home(Ventana_Principal, user))
		ventana1.pushButton_editUser.clicked.connect(lambda: self.editarUser(Ventana_Principal, user, user))

def clear():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system ("cls")

if __name__ == "__main__":
	cs = Controller()
	cs.Iniciar()