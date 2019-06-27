import sys
sys.path.append('../connection')
from db_connection import DBconn

class Schedule:
	def __init__(self):
		self.day = ""
		self.turn = ""
		self.opening = ""
		self.closing = ""