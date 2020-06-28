import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="", 
                           database="demo")
cursor = conexion.cursor()

# Construir comando para borrar tabla
BorrarRegistro = "DELETE from oficinas WHERE id = 1"

# Borrar tabla
cursor.execute(BorrarRegistro)
print("Se ha suprimido una tabla de la base de datos")

# Finalizar transacción y cerrar
conexion.commit()
conexion.close()