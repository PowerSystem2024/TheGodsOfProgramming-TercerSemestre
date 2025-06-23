from config_db import DB_CONFIG
import psycopg2

try:
    connection = psycopg2.connect(**DB_CONFIG)
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM persona WHERE id_persona = %s'
            input_id = input('🗑️ Ingrese el ID de registro a eliminar: ')
            cursor.execute(query, (input_id,))
            print(f"Registros eliminados: {cursor.rowcount}")
except Exception as e:
    print(f"❌ Error al eliminar registro: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")
