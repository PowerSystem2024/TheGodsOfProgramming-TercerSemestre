from psycopg2 import pool  # Importamos el módulo de psycopg2 para manejar un pool de conexiones
from logger_base import log  # Importamos el sistema de logging personalizado
import sys  # Importamos sys para poder terminar el programa con sys.exit() en caso de error crítico

class Conexion:
    # Datos de configuración para conectarse a la base de datos PostgreSQL
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'

    # Parámetros del pool de conexiones
    _MIN_CON = 1  # Cantidad mínima de conexiones activas en el pool
    _MAX_CON = 5  # Cantidad máxima de conexiones permitidas en el pool
    _pool = None  # Variable para almacenar el pool (será inicializado una única vez)

    @classmethod
    def obtenerPool(cls):
        """Devuelve el pool de conexiones, lo crea si aún no fue creado."""
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        """Obtiene una conexión desde el pool."""
        conexion = cls.obtenerPool().getconn()  # Se obtiene una conexión activa del pool
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def obtenerCursor(cls):
        """(A implementar) Retorna un cursor asociado a una conexión del pool."""
        pass  # Podés completar este método si querés manejar cursor directamente desde aquí

# Bloque de prueba: se ejecuta solo si el archivo se corre directamente
if __name__ == '__main__':
    # Se solicitan conexiones desde el pool (hasta el máximo permitido)
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    # conexion6 = Conexion.obtenerConexion()  # Si se descomenta, excede el máximo y lanza error
