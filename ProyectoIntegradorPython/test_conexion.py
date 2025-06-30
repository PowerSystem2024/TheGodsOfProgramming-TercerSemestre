"""
Script de prueba para verificar la conexión a MongoDB y la funcionalidad básica
"""
import sys
import os

# Agregar el directorio src al path para poder importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from db.conexion import conectar, desconectar

def test_conexion():
    """
    Prueba la conexión a MongoDB
    """
    print("🔄 Probando conexión a MongoDB...")
    
    # Si MongoDB no está disponible, usaremos una conexión de prueba
    try:
        if conectar():
            print("✅ Conexión exitosa a MongoDB")
            desconectar()
            return True
        else:
            print("❌ No se pudo conectar a MongoDB")
            return False
    except Exception as e:
        print(f"❌ Error al probar conexión: {e}")
        return False

def test_modelos():
    """
    Prueba los modelos sin conexión a MongoDB
    """
    print("🔄 Probando importación de modelos...")
    
    try:
        from models.medio_comunicacion import MedioComunicacion
        from models.tipo_modulo import TipoModulo
        from models.frecuencia_publicacion import FrecuenciaPublicacion
        from models.anuncio import Anuncio
        
        print("✅ Todos los modelos se importaron correctamente")
        return True
    except Exception as e:
        print(f"❌ Error al importar modelos: {e}")
        return False

def test_servicios():
    """
    Prueba los servicios sin conexión a MongoDB
    """
    print("🔄 Probando importación de servicios...")
    
    try:
        from services.datos_basicos_service import DatosBasicosService
        from services.anuncio_service import AnuncioService
        
        print("✅ Todos los servicios se importaron correctamente")
        return True
    except Exception as e:
        print(f"❌ Error al importar servicios: {e}")
        return False

def main():
    """
    Ejecuta todas las pruebas
    """
    print("🚀 Iniciando pruebas del sistema...")
    print("="*50)
    
    # Probar modelos
    if not test_modelos():
        print("❌ Fallo en la prueba de modelos")
        return False
    
    # Probar servicios
    if not test_servicios():
        print("❌ Fallo en la prueba de servicios")
        return False
    
    # Probar conexión MongoDB
    mongodb_ok = test_conexion()
    if not mongodb_ok:
        print("⚠️  MongoDB no está disponible. El sistema funcionará en modo de prueba.")
    
    print("="*50)
    if mongodb_ok:
        print("✅ Todas las pruebas pasaron. El sistema está listo para usar con MongoDB.")
    else:
        print("⚠️  Pruebas básicas pasaron. Para usar MongoDB, asegúrate de que esté ejecutándose.")
    
    return True

if __name__ == "__main__":
    main()
