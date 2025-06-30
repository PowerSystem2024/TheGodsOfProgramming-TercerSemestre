"""
Configuración de conexión a MongoDB
"""
import mongoengine as me
import logging
from config.configuracion import Config

logger = logging.getLogger(__name__)
config = Config()

def conectar():
    """
    Establece la conexión con MongoDB usando configuración centralizada
    """
    try:
        mongodb_config = config.get_mongodb_config()
        
        me.connect(**mongodb_config)
        
        logger.info("Conexión a MongoDB establecida exitosamente")
        print("✅ Conexión a MongoDB establecida exitosamente")
        return True
        
    except Exception as e:
        logger.error(f"Error al conectar con MongoDB: {e}")
        print(f"❌ Error al conectar con MongoDB: {e}")
        print("⚠️  Asegúrate de que MongoDB esté ejecutándose")
        return False

def desconectar():
    """
    Desconecta de MongoDB
    """
    try:
        me.disconnect()
        logger.info("Desconectado de MongoDB")
        print("✅ Desconectado de MongoDB")
    except Exception as e:
        logger.error(f"Error al desconectar de MongoDB: {e}")
        print(f"❌ Error al desconectar de MongoDB: {e}")

def verificar_conexion():
    """
    Verifica si la conexión a MongoDB está activa
    
    Returns:
        bool: True si la conexión está activa
    """
    try:
        # Intentar una operación simple para verificar la conexión
        me.connection.get_connection()
        return True
    except Exception as e:
        logger.warning(f"Conexión no disponible: {e}")
        return False
