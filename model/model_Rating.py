import sys
sys.path.append('../connection')
from db_connection import DBconn

class Rating:
	def __init__(self):
		self.id_person = ""
		self.id_shop = ""
		self.rating = ""
		self.db = DBconn()

	def registerInitialRate(self):
		self.query = "INSERT INTO rating(id_person, idshop, rating) VALUES (%s,%s,%s)"
		self.values = (self.id_person, self.id_shop, self.rating)
		return self.db.insertar(self.query, self.values)