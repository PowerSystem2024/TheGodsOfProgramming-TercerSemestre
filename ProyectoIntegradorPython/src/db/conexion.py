"""
Configuración de conexión a MongoDB
"""
import mongoengine as me

def conectar():
    """
    Establece la conexión con MongoDB
    """
    try:
        # Cambia según tu conexión de MongoDB
        me.connect(
            db="proyecto_anuncios_publicitarios",
            host="mongodb://localhost:27017/proyecto_anuncios_publicitarios"
        )
        print("✅ Conexión a MongoDB establecida exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error al conectar con MongoDB: {e}")
        print("⚠️  Asegúrate de que MongoDB esté ejecutándose")
        return False

def desconectar():
    """
    Desconecta de MongoDB
    """
    try:
        me.disconnect()
        print("✅ Desconectado de MongoDB")
    except Exception as e:
        print(f"❌ Error al desconectar de MongoDB: {e}")
