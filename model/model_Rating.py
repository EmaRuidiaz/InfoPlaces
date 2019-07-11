import sys
sys.path.append('../connection')
from db_connection import DBconn

class Rating:
	def __init__(self):
		self.id_person = ""
		self.id_shop = ""
		self.rating = ""
		self.db = DBconn()

	def registerRate(self):
		self.query = "INSERT INTO rating(idperson, idshop, rating) VALUES (%s,%s,%s)"
		self.values = (self.id_person, self.id_shop, self.rating)
		return self.db.insertar(self.query, self.values)

	def updateRate(self):
		self.query = "UPDATE rating SET rating = %s WHERE idperson = %s AND idshop = %s"
		self.values = (self.rating, self.id_person, self.id_shop)
		return self.db.insertar(self.query, self.values)

	def checkRate(self):
		self.query = "SELECT * FROM rating WHERE idperson = %s AND idshop = %s"
		self.values = (self.id_person, self.id_shop)
		return self.db.ejecutar(self.query, self.values)		