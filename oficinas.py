import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="", 
                           database="demo")
cursor = conexion.cursor()

# Agregar nueva tabla 'Oficinas' a la base de datos 'demo'
TablaOficinas = """CREATE TABLE Oficinas(
denom CHAR(20),
provin CHAR(10),
PRIMARY KEY (denom))"""

cursor.execute(TablaOficinas)
print("Se ha agregado la tabla 'Oficinas' a la base de datos")

# Cerrar conexión
conexion.close()