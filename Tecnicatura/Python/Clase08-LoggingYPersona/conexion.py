import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'db_test'
    _USERNAME = 'postgres'
    _PASSWORD = 'Passe01'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                            user=cls._USERNAME,
                                            password=cls._PASSWORD,
                                            port=cls._DB_PORT,
                                            database=cls._DATABASE)
                log.debug(f'Conexion con exito: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Error en la conexion: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Cursor con exito: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Error en la cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()