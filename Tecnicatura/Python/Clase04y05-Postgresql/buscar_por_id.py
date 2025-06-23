from config_db import DB_CONFIG
import psycopg2

try:
    connection = psycopg2.connect(**DB_CONFIG)
    with connection:
        with connection.cursor() as cursor:
            query = 'SELECT * FROM persona WHERE id_persona = %s'
            person_id = input('🔎 Ingrese el ID a buscar: ')
            cursor.execute(query, (person_id,))
            result = cursor.fetchone()
            if result:
                print("Resultado encontrado:", result)
            else:
                print("No se encontró ninguna persona con ese ID.")
except Exception as e:
    print(f"❌ Error en la búsqueda: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")