import sys
sys.path.append('../connection')
from db_connection import DBconn


class User:
	def __init__(self):
		self.image = "../../InfoPlaces/view/user.PNG"
		self.type = 3


	def search(self):
		pass