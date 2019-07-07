import sys
sys.path.append('../connection')
from db_connection import DBconn

class Shop:
	def __init__(self):
		self.name = ""
		self.address = ""
		self.number = ""
		self.description = ""
		self.type = ""
		self.photos = []
		self.schedule = []
		self.db = DBconn()

	def register(self, user):
		self.query = "INSERT INTO shop(name, street_name, street_num, person, type, description) VALUES (%s, %s, %s, %s, %s, %s)"
		self.values = (self.name, self.address, self.number, user.username, self.type, self.description)
		return self.db.insertar(self.query,self.values)

	def getID(self):
		self.query = "SELECT id FROM shop WHERE name = %s and street_name = %s and street_num = %s"
		self.values = (self.name, self.address, self.number)
		return self.db.ejecutar(self.query, self.values)

	def registerPhoto(self,idShop):
		self.query = "INSERT INTO photo(shop, image) VALUES (%s,%s),(%s,%s),(%s,%s),(%s,%s),(%s,%s)"
		self.values = (idShop, self.photos[0], idShop, self.photos[1], idShop, self.photos[2], idShop, self.photos[3], idShop, self.photos[4])
		return self.db.insertar(self.query, self.values)

	def searchShop(self):
		self.query = "SELECT distinct p.image, s.name, s.description, s.id, s.type  FROM shop s INNER JOIN schedule sc on s.id = sc.shop INNER JOIN photo p on p.shop = s.id WHERE s.name like %s GROUP BY s.id;"
		self.values = ("%"+self.name+"%",)
		return self.db.ejecutar(self.query, self.values)

	def TraerTiendas(self):
		self.query = "SELECT p.image, s.name, s.description, s.id FROM shop s INNER JOIN photo p on s.id = p.shop GROUP BY s.id;"
		self.values = ()
		return self.db.ejecutar(self.query, self.values)

	def getShopDescription(self, ide):
		self.query = "SELECT * FROM shop WHERE id = %s"
		self.values = (ide,)
		return self.db.ejecutar(self.query, self.values)

	def getShopSchedule(self, ide):
		self.query = "SELECT id, shop, day, turn, hour(opening), minute(opening),hour(closing), minute(closing) FROM schedule WHERE shop = %s"
		self.values = (ide,)
		return self.db.ejecutar(self.query, self.values)

	def getShopPhotos(self, ide):
		self.query = "SELECT * FROM photo WHERE shop = %s"
		self.values = (ide,)
		return self.db.ejecutar(self.query, self.values)