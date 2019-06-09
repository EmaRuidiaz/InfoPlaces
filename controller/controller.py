import sys
sys.path.insert(0, '/home/ema/Documentos/InfoPlaces/connection')
sys.path.insert(0, 'C:/Users/Apagu/Desktop/InfoPlaces/prueba')
import interfaz_ui
import db_connection

import os


class UserController:
	def __init__(self):
		op = menu(self)
		while op != "5":
			if op == "1":  ##
				print("Presionaste en buscar")
				llamoafuncionbuscar()
			elif op == "2":
				print("Presionaste un tag")
				llamoafunciontag()
			clear()
			op = menu(self)


class RegisteredUserController():
	def __init__(self):
		User.__init__(self)

		self.firstame = ""
		self.lastname = ""
		self.username = ""
		self.birthdate = ""
		self.email = ""
		self.password = ""

	def addtofavorites(self):
		pass

	def comment(self):
		pass

	def rate(self):
		pass

class ShopOwnerController():
	def __init__(self):
		RegisteredUser.__init__(self)

	def answer(self):
		pass

	def modify(self):
		pass

	def createshop(self):
		pass

class AdministratorController():
	def __init__(self):
		ShopOwner.__init__(self)

	def createaccount(self):
		pass

class TypeController:
	def __init__(self):
		self.description = ""

class ShopController:
	def __init__(self):
		self.name = ""
		self.phone = ""
		self.streetname = ""
		self.streetnumber = ""

class CommetController:
	def __init__(self):
		self.date = ""

class RatingController:
	def __init__(self):
		self.number

class FavoriteController:
	def __init__(self):
		pass

class AnswerController:
	def __init__(self):
		pass

class ScheduleController:
	def __init__(self):
		self.day = ""
		self.turn = ""
		self.opening = ""
		self.closing = ""


def menu(self):
	print("Hola, estas en el sistema!")
	op = input("Ingresa una opcion")
	return op

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

class ventanas:
	def __init__(self):
		v = ventana1()
		if v.op == "2":
			print("adelante")
		elif v.op == "3":
			print("atras")

x = ventanas()

