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


	def TraerComentario(self):
		self.query = "SELECT ph.image, p.user_name, c.content FROM comment c INNER JOIN person p ON c.idperson = p.user_name INNER JOIN photo ph ON p.user_name = ph.user_name group by c.id;"
		self.values = ()
		return self.db.ejecutar(self.query, self.values)