import pymysql  #importamos la libreria para poder trabajar python con MySQL

class DataBase:             #Definimos nuestra clase con el nombre de DataBase
    def __init__(self):      #Definimos nuestro metodo inicial
        self.connection = pymysql.connect(          #creamos nuestra conexion con nuestros datos de admin de MySQL
            host='localhost',           #seleccionamos nuestro host o ip de conexion
            user='root',                #nuestro ususario de administrador MySql
            password='',                #Password de admin
            db='demo',                  #seleccionamos la base de datos con la que deseamos trabajar
        )

        self.cursor = self.connection.cursor()          #definimos un cursor para verificar la conexion a nuestra base de datos


        print("Conexion Establecida Exitosamente")      #en caso de que la conexion este correcta se imprime un mensaje en pantalla

    #Procedemos  a interactuar con nuestros datos dentro de nuestra base de datos.

    def select_user(self, id):                                  #definimos nuestra clase para usuario
        sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)     #seleccionamos los datos que queremos obtener de nuestra base de datos y le damos formato el nombre de id.

        try:                #ejecutamos un metodo try
            self.cursor.execute(sql)        #ejecutamos un cursor sql 
            user = self.cursor.fetchone()   #utilizamos un metodo self.cursor para identificar nuestra matriz ya que reconoceran por  pocision de array

            print("Id:", user[0])           #imprimimos una variable llamada id que tomara el dato que se encuentre en la posicion de lista numero 0
            print("Username:", user[1])     #imprimimos una variable llamada username que tomara el dato que se encuentre en la posicion de lista numero 1
            print("Email:", user[2])        #imprimimos una variable llamada email que tomara el dato que se encuentre en la posicion de lista numero 2

        except Exception as e:              #en caso de haber un error nos devolvera un error   que entra dentro d euna excepcion.
            raise

database = DataBase()                       #finalmente imprimimos los elementos de nuestra clase llamada DataBase
database.select_user(1)                     #imprimimos solamente e este caso el dato que se posiciones en la primera fila de  nuestra base de datos.
