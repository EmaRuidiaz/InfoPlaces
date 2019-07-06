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
		
		if ventana1.terms:
			if self.reguser.firstname and self.reguser.lastname and self.reguser.username and self.reguser.email and self.reguser.password and (self.reguser.password == self.confirmuser):
				if ventana1.fechacontrol < 2019:
					if len(self.reguser.password) > 7:
						if not self.reguser.CheckReg():
							if self.reguser.Register():
								self.reguser.RegisterPhoto()
								QMessageBox.about(Ventana_Principal, "Succefully registered", "User registered!")
								self.menuPrincipal(Ventana_Principal)
							else:
								pass
						else:
							QMessageBox.about(Ventana_Principal, "Username or E-Mail invalid.", "The username or email already exist")
					else:
						QMessageBox.about(Ventana_Principal, "Weak password.", "The password needs to be more than 8 characters")
				else:
					QMessageBox.about(Ventana_Principal, "Birthdate is invalid.", "birthdate is non-existent")
			else:
				QMessageBox.about(Ventana_Principal, "Error", "You need to complete all the required fields.")
		else:
			QMessageBox.about(Ventana_Principal, "Terms and conditions", "You need to read and accept Terms and conditions")

	def Home(self, Ventana_Principal,user):
		a = Shop()
		b = a.TraerTiendas()
		print(b)
		ventana1 = HomeView(Ventana_Principal, user,b)
		search = Shop()
		#resultado = []
		
		ventana1.pushButton_Search.clicked.connect(lambda: self.Search(search, ventana1, b))
		try:
			ventana1.perfil.clicked.connect(lambda: self.user(Ventana_Principal, user))
			ventana1.pushButton_Create_Store.clicked.connect(lambda: self.crearStore(Ventana_Principal, user))
		except:
			pass
		ventana1.pushButton_Log_Out.clicked.connect(lambda: self.logOut(Ventana_Principal, user))

	def filterShop(self,ventana1, resultado):
		if ventana1.radioButton_Sports.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Sports":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Restaurant.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Restaurant":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Kitchen.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Kitchen":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Gardening.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Gardening":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Restaurant.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Restaurant":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Bookstore.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Bookstore":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Toy_store.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Toy Store":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Tools.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Tools":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_Other.isChecked():
			for i in range(len(resultado),0,-1):
				if resultado[len(resultado) - i][3] != "Other":
					resultado.pop(len(resultado) -i)
		elif ventana1.radioButton_All.isChecked():
			pass

	def Search(self, search, ventana1, resultado):
		ventana1.update()
		
		search.name = ventana1.busqueda
		print("antes de busqueda primera: ",resultado)
		resultado = search.searchShop()
		print("antes de filtrado: ",resultado)
		self.filterShop(ventana1,resultado) 
		print("Despues de filtro: ",resultado)
		ventana1.Cargar_tienda(resultado)
		print("Despues de busqueda: ",resultado)
		return resultado

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
			print(type(passwd),type(user))
			if (user != ""):
				if passwd != "":
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
						msj = QMessageBox.critical(Ventana_Principal, "Incorrect username or password", "Please, try again.\nIf you don't have an account you can create one free!")
				else:
					msj = QMessageBox.critical(Ventana_Principal, "No password", "Complete the password field and try again")
			else:
				msj = QMessageBox.critical(Ventana_Principal, "No email or username", "Complete the username or email field and try again")
		elif typeu == 2:
			print("Tipo: ", typeu)
			owner = ShopOwner()
			owner.username = user
			owner.email = user
			owner.password = passwd
			owner.type = typeu
			self.validacion = owner.SignIn()
			#self.reguser.username, self.reguser.password)
			print(self.validacion)
			if (user != ""):
				if passwd != "":
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
						QMessageBox.critical(Ventana_Principal, "Incorrect username or password", "Please, try again.\nIf you don't have an account you can create one free!")
				else:
					msj = QMessageBox.critical(Ventana_Principal, "No password", "Complete the password field and try again")
			else:
				msj = QMessageBox.critical(Ventana_Principal, "No email or username", "Complete the username or email field and try again")
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
		if shop.name and shop.address and shop.number and shop.description and ventana1.flagPhoto and ventana1.flagType:
			shop.register(user)
			idShop = shop.getID()
			print("Este es el id de la tienda: ",idShop)
			shop.registerPhoto(idShop[0][0])
			print("VENTANA1.SCHEDULE: ",ventana1.schedule)
			for i in range(1,15):
				schedule.register(ventana1.schedule, idShop[0][0], i-1)
			QMessageBox.about(Ventana_Principal, "Register", "The shop was registered succefully!")
		else:
			QMessageBox.critical(Ventana_Principal, "Error - Register", "The shop wasn't registered!")
			print("Error - No se ha registrado")


	def editarUser(self, Ventana_Principal, user, userresguardo):
		import imagen_rc
		self.userresguardo = user
		ventana1 = UserEditView(Ventana_Principal, user)
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_cancel.clicked.connect(lambda: self.user(Ventana_Principal, user))
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
				QMessageBox.about(Ventana_Principal, "Update Succefull", "Personal data Updated!")
				self.user(Ventana_Principal, user)
			else:
				QMessageBox.warning(Ventana_Principal, "Error", "Username already exist")
				user = userresguardo
				user.username = self.usernameresguardo
				user.email = self.emailresguardo
				self.editarUser(Ventana_Principal, user, userresguardo)
		else:
			QMessageBox.warning(Ventana_Principal, "Error", "You need to complete all fields")
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