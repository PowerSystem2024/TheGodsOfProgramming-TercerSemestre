import pytest
import mongoengine
from db.conexion import conectar

@pytest.fixture(scope="session", autouse=True)
def mongodb_test():
    # Conecta a una base de datos de pruebas. Cambia el nombre si lo deseas.
    mongoengine.disconnect()
    mongoengine.connect("proyectointegrador_test", host="mongodb://localhost:27017/proyectointegrador_test")
    yield
    mongoengine.disconnect()