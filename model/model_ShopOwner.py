import sys
sys.path.append('../connection')
from model_RegisteredUser import RegisteredUser
from model_User import User
from db_connection import DBconn

class ShopOwner(RegisteredUser):
	def __init__(self):
		RegisteredUser.__init__(self)

	def myShops(self):
		self.query = "SELECT * FROM shop WHERE person = %s"
		self.values = (self.username,)
		return self.db.ejecutar(self.query, self.values)

	def answer(self):
		pass

	def modify(self):
		pass

	def createshop(self):
		pass