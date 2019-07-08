import sys
sys.path.append('../connection')
from db_connection import DBconn

class Comment:
	def __init__(self):
		self.content = ""
		self.date = ""
		self.person = ""
		self.shop = ""
		self.db = DBconn()

	def register(self):
		self.query = "INSERT INTO comment(content, datetime, idperson, idshop) VALUES (%s,%s,%s,%s);"
		self.values = (self.content, self.date, self.person, self.shop)
		return self.db.insertar(self.query, self.values)
