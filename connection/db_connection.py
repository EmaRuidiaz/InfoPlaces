import mysql.connector

class DBconn:
    def __init__(self, db_host="localhost", db_user="root", db_pass="flechaverde1", db_name="infoplaces"):
        self.db_name = db_name
        self.db_pass = db_pass
        self.db_user = db_user
        self.db_host = db_host

    def conectar(self):
        self.conexion = mysql.connector.connect(user=self.db_user, password=self.db_pass, host=self.db_host, database=self.db_name)
        '''if self.conexion.is_connected():
                                    print("Se conecto")'''

    def abrir_cursor(self):
        self.cursor = self.conexion.cursor(prepared=True)

    def ejecutar_consulta(self, query, values="", querytype=""):
        if querytype == "select":
            if values != "":
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
        elif querytype == "insert":
            if values != "":
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

    def send_commit(self, query):
        sql = query.lower()
        es_lectura = sql.count('select')
        if es_lectura < 1:
            self.conexion.commit()

    def traer_datos(self):
        self.datos = self.cursor.fetchall()
        #print(self.datos, "  datoss de la consulta")

    def cerrar_cursor(self):
        self.cursor.close()

    def ejecutar(self, query, values=""):
        if (self.db_host and self.db_user and self.db_pass and self.db_name and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query,values,"select")
            self.send_commit(query)
            self.traer_datos()
            self.cerrar_cursor()
            return self.datos

    def insertar(self, query, values=""):
        if (self.db_host and self.db_user and self.db_pass and self.db_name and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query,values,"insert")
            self.send_commit(query)
            self.cerrar_cursor()
            return "1"