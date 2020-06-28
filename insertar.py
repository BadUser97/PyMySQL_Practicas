import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="", 
                           database="demo")
cursor = conexion.cursor()

# Definir comandos para insertar registros
registro1 = "INSERT INTO Oficinas VALUES ('Central', 'monterey');"
registro2 = "INSERT INTO Oficinas VALUES ('Norte', 'chihuahua');"
registro3 = "INSERT INTO Oficinas VALUES ('Extremadura', 'chiapas');"

# Ejecutar comandos
cursor.execute(registro1)
cursor.execute(registro2)
cursor.execute(registro3)


print("Se han agregado correctamente los datos")

# Finalizar transacción y cerrar
conexion.commit()
conexion.close()