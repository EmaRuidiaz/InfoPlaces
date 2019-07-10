import sys
sys.path.append('../connection')
from db_connection import DBconn

class Favorite:
	def __init__(self):
		self.id_person = ""
		self.id_shop = ""
		self.db = DBconn()

	def checkFav(self):
		self.query = "SELECT * FROM favorite WHERE idperson = %s AND idshop = %s"
		self.values = (self.id_person, self.id_shop)
		return self.db.ejecutar(self.query,self.values)

	def insertFav(self):
		self.query = "INSERT INTO favorite(idperson, idshop) VALUES (%s,%s)"
		self.values = (self.id_person, self.id_shop)
		return self.db.insertar(self.query,self.values)

	def deleteFav(self):
		self.query = "DELETE FROM favorite WHERE idperson = %s AND idshop = %s"
		self.values = (self.id_person, self.id_shop)
		return self.db.insertar(self.query,self.values)
