import sys
sys.path.append('../connection')
from db_connection import DBconn

class Comment:
	def __init__(self):
		self.date = ""