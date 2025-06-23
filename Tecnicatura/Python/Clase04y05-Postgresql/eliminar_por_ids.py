from config_db import DB_CONFIG
import psycopg2

try:
    connection = psycopg2.connect(**DB_CONFIG)
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM persona WHERE id_persona IN %s'
            user_input = input('🗑️ Ingrese los IDs a eliminar (separados por coma): ')
            try:
                ids = tuple(int(x.strip()) for x in user_input.split(',') if x.strip().isdigit())
            except ValueError:
                print("Entrada inválida: ingrese solo números separados por comas.")
                ids = ()
            if not ids:
                print('No se ingresaron IDs válidos.')
            else:
                cursor.execute(query, (ids,))
                print(f"Registros eliminados: {cursor.rowcount}")
except Exception as e:
    print(f"❌ Error al eliminar registros: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")