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
		self.db = DBconn()

	def SignIn(self):
		self.query = "Select id from person where user_name = %s and password = %s and type = %s"
		self.values = (self.username, self.password, self.type)
		return self.db.ejecutar(self.query,self.values)

	def Register(self):
		self.query = "Select id from person where user_name = %s"
		self.values = self.username
		return self.db.ejecutar(self.query, self.values)

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

