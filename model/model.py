import sys
sys.path.insert(0, '/home/ema/Documentos/InfoPlaces/connection')
import db_connection


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

	def addtofavorites(self):
		pass

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

class Commet:
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

