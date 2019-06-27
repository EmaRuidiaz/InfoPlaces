import sys
sys.path.append('../connection')
from model_RegisteredUser import RegisteredUser
from db_connection import DBconn

class ShopOwner(RegisteredUser):
	def __init__(self):
		RegisteredUser.__init__(self)

	def answer(self):
		pass

	def modify(self):
		pass

	def createshop(self):
		pass