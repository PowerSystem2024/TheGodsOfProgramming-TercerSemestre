from config_db import DB_CONFIG
import psycopg2

try:
    connection = psycopg2.connect(**DB_CONFIG)
    print("✅ Conexión exitosa a la base de datos.")
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM persona"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                print("Personas encontradas:")
                for row in results:
                    print(row)
            else:
                print("No se encontraron personas en la tabla.")
except Exception as e:
    print(f"❌ Error al conectar o consultar la base de datos: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")
print("Fin del programa.")