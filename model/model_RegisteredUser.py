import sys
sys.path.append('../connection')
from model_User import User
from db_connection import DBconn

class RegisteredUser(User):
	def __init__(self):
		User.__init__(self)
		self.firstame = ""
		self.lastname = ""
		self.username = ""
		self.birthdate = ""
		self.email = ""
		self.password = ""
		self.type = ""
		self.phone_number = ""
		self.image = ""
		self.db = DBconn()

	def UpdateInfo(self, userresguardo):
		self.query = "UPDATE person SET first_name = %s, last_name = %s, phone_number = %s, user_name = %s, password = %s WHERE user_name = %s"
		self.values = (self.firstname, self.lastname, self.phone_number, self.username, self.password, userresguardo)
		return self.db.insertar(self.query, self.values)

	def UpdatePhoto(self, userresguardo):
		self.query = "UPDATE photo SET user_name = %s, image = %s WHERE user_name = %s"
		self.values = (self.username, self.image, userresguardo)
		return self.db.insertar(self.query, self.values)

	def RegisterPhoto(self):
		self.query = "INSERT INTO photo(image, user_name) VALUES (%s, %s)"
		self.values = (self.image, self.username)
		return self.db.insertar(self.query,self.values)

	def SignIn(self):
		self.query = "SELECT p.user_name, p.type, p.first_name, p.last_name, p.email, p.password, p.birthdate, p.phone_number, ph.image FROM person p left join photo ph on p.user_name = ph.user_name  WHERE (p.user_name = %s OR p.email = %s) AND p.password = %s AND p.type = %s"
		self.values = (self.username, self.email, self.password, self.type)
		return self.db.ejecutar(self.query,self.values)

### no tengo NI IDEA de como poner un solo value, me explota todo el programa con uno solo (adaptarse. sobrevivir. vencer)... ###
	def CheckReg(self):
		self.query = "SELECT user_name FROM person WHERE email = %s or user_name = %s"
		self.values = (self.email, self.username)
		return self.db.ejecutar(self.query,self.values)

	def Register(self):
		self.query = "INSERT INTO person(user_name, type, first_name, last_name, email, password, birthdate, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		self.values = (self.username, self.type, self.firstname, self.lastname,self.email, self.password, self.birthdate, self.phone_number)
		return self.db.insertar(self.query,self.values)

	def comment(self):
		pass

	def rate(self):
		pass