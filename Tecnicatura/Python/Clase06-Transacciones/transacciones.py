from config_db import DB_CONFIG
import psycopg2 as bd

conexion = bd.connect(**DB_CONFIG)

try:
    cursor = conexion.cursor()
    sentecia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Marina', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentecia, valores)
    conexion.commit() #sentencia de commit manual
    print('Termina la transacción')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')

finally:
        conexion.close()