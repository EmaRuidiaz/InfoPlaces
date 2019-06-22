import sys
sys.path.append('../connection')
from db_connection import DBconn


class User:
	def __init__(self):
		pass

	def register(self):
		pass

	def search(self):
		pass



class RegisteredUser(User):
	def __init__(self):
		User.__init__(self)
		self.firstame = ""
		self.lastname = ""
		self.username = ""
		self.birthdate = ""
		self.email = ""
		self.password = ""
		self.type = ""
		self.phone_number = ""
		self.db = DBconn()

	def SignIn(self):
		self.query = "SELECT * FROM person WHERE (user_name = %s OR email = %s) AND password = %s AND type = %s"
		self.values = (self.username, self.email, self.password, self.type)
		return self.db.ejecutar(self.query,self.values)

### no tengo NI IDEA de como poner un solo value, me explota todo el programa con uno solo (adaptarse. sobrevivir. vencer)... ###
	def CheckReg(self):
		self.query = "SELECT id FROM person WHERE email = %s or user_name = %s"
		self.values = (self.email, self.username)
		return self.db.ejecutar(self.query,self.values)

	def Register(self):
		self.query = "INSERT INTO person (user_name, type, first_name, last_name, email, password, birthdate, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		self.values = (self.username, self.type, self.firstname, self.lastname,self.email, self.password, self.birthdate, self.phone_number)
		return self.db.insertar(self.query,self.values)

	def comment(self):
		pass

	def rate(self):
		pass

class ShopOwner(RegisteredUser):
	def __init__(self):
		RegisteredUser.__init__(self)

	def answer(self):
		pass

	def modify(self):
		pass

	def createshop(self):
		pass

class Administrator(ShopOwner):
	def __init__(self):
		ShopOwner.__init__(self)

	def createaccount(self):
		pass

class Type:
	def __init__(self):
		self.description = ""

class Shop:
	def __init__(self):
		self.name = ""
		self.phone = ""
		self.streetname = ""
		self.streetnumber = ""

class Comment:
	def __init__(self):
		self.date = ""

class Rating:
	def __init__(self):
		self.number

class Favorite:
	def __init__(self):
		pass

class Answer:
	def __init__(self):
		pass

class Schedule:
	def __init__(self):
		self.day = ""
		self.turn = ""
		self.opening = ""
		self.closing = ""

x = RegisteredUser()

