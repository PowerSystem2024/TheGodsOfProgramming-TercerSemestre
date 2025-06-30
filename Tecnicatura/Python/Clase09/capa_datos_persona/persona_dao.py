from Persona import Persona  # Importamos la clase Persona que representa el modelo de datos
from conexion import Conexion  # Importamos la clase Conexion para conectarnos a la base de datos
from logger_base import log  # Importamos el logger personalizado para registrar actividad

class PersonaDAO:
    """
    DAO -> Data Access Object
    Esta clase gestiona las operaciones de acceso a datos de la entidad Persona.

    CRUD:
    - Create (Insertar)
    - Read (Seleccionar)
    - Update (Actualizar)
    - Delete (Eliminar)
    """

    # Sentencias SQL preparadas como atributos de clase (usando placeholders %s)
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Método para obtener todos los registros de la tabla persona
    @classmethod
    def seleccionar(cls):
        # Manejo automático de conexión y cursor usando 'with'
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()  # Devuelve una lista de tuplas
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas  # Devuelve una lista de objetos Persona

    # Método para insertar un nuevo registro en la base de datos
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Personas insertadas: {persona}')
                return cursor.rowcount  # Devuelve la cantidad de registros insertados

    # Método para actualizar un registro existente
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Personas actualizadas: {persona}')
                return cursor.rowcount  # Devuelve cuántos registros fueron modificados

    # Método para eliminar un registro por ID
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Personas eliminadas: {persona}')
                return cursor.rowcount  # Devuelve la cantidad de registros eliminados

# Bloque de prueba: se ejecuta solo si el archivo se corre directamente
if __name__ == '__main__':
    # === PRUEBAS DE FUNCIONALIDAD ===

    # --- Eliminar un registro ---
    # persona1 = Persona(id_persona=10)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # --- Actualizar un registro ---
    # persona1 = Persona(12, 'Florencia', 'Alonso', 'florencia@gmail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # --- Insertar un nuevo registro ---
    # persona1 = Persona(nombre='Alejandro', apellido='Aguilera', email='alejandro@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # --- Seleccionar todos los registros ---
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
