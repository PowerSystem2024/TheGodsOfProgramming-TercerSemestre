import pytest
import mongoengine
import os
import sys

# Agregar el directorio raíz al path para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db.conexion import conectar

@pytest.fixture(scope="session", autouse=True)
def mongodb_test():
    """Fixture para configurar base de datos de pruebas"""
    # Conecta a una base de datos de pruebas separada
    mongoengine.disconnect()
    try:
        mongoengine.connect("proyectointegrador_test", host="mongodb://localhost:27017/proyectointegrador_test")
        yield
    except Exception as e:
        # Si no hay MongoDB disponible, usar alias de prueba mock
        print(f"Warning: MongoDB no disponible para tests: {e}")
        yield
    finally:
        mongoengine.disconnect()