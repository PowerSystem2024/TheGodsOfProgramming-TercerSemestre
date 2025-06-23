from config_db import DB_CONFIG
import psycopg2

try:
    connection = psycopg2.connect(**DB_CONFIG)
    with connection:
        with connection.cursor() as cursor:
            query = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            values = [
                ('Nahuel', 'Ramirez', 'example@mail.com'),
                ('Juliana', 'Rueda', 'example1@mail.com'),
                ('Uriel', 'Ramirez', 'example2@mail.com'),
            ]
            cursor.executemany(query, values)
            print(f"✅ Registros insertados: {cursor.rowcount}")
except Exception as e:
    print(f"❌ Error al insertar registros: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")