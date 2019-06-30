import sys
sys.path.append('../connection')
from db_connection import DBconn

class Schedule:
	def __init__(self):
		self.day = ""
		self.turn = ""
		self.opening = ""
		self.closing = ""
		self.db = DBconn()

	def register(self, schedule, idShop):
		self.query = "INSERT INTO schedule(shop,day,turn,opening,closing) VALUES (%s,%s,%s,%s,%s)"
		self.values = ((idShop,schedule[0][0],schedule[0][1],schedule[0][2],schedule[0][3]),(idShop,schedule[1][0],schedule[1][1],schedule[1][2],schedule[1][3]))
		return self.db.insertar(self.query, self.values)