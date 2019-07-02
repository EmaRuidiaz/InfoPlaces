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

	def register(self, schedule, idShop, i):
		self.query = "INSERT INTO schedule(shop,day,turn,opening,closing) VALUES (%s,%s,%s,%s,%s)"
		self.values = ((idShop,schedule[i][0],schedule[i][1],schedule[i][2],schedule[i][3]))
		return self.db.insertar(self.query, self.values)