import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="", 
                           database="demo")
cursor = conexion.cursor()

# Recuperar registros de la tabla 'Oficinas'
tablas = "SHOW TABLES;"
registros = "SELECT * FROM Oficinas;"

# Mostrar tablas
cursor.execute(tablas)
filas = cursor.fetchall()
print("Tablas de 'personal':")
for fila in filas:
   print(fila)

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
print("Registros de 'Oficinas':")
for fila in filas:
   print(fila[0], ":", fila[1])

# Finalizar 
conexion.commit()
conexion.close()