import sys
sys.path.append('../connection')
from db_connection import DBconn

class Shop:
	def __init__(self):
		self.name = ""
		self.address = ""
		self.number = ""
		self.description = ""

	def registrar(self, user):
		self.query = "INSERT INTO shop(name, street_name, street_num, person) VALUES (%s, %s, %s, %s)"
		self.values = (self.name, self.address, self.number, user.username)
		return self.db.insertar(self.query,self.values)