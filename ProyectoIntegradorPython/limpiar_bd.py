"""
Script para limpiar la base de datos MongoDB del proyecto
ADVERTENCIA: Este script elimina TODOS los datos de la base de datos
"""
import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from db.conexion import conectar, desconectar
from models.anuncio import Anuncio
from models.medio_comunicacion import MedioComunicacion
from models.tipo_modulo import TipoModulo
from models.frecuencia_publicacion import FrecuenciaPublicacion

def confirmar_limpieza():
    """
    Solicita confirmación del usuario antes de limpiar la BD
    """
    print("⚠️  ADVERTENCIA: Esta acción eliminará TODOS los datos del sistema!")
    print("📊 Base de datos: proyecto_anuncios_publicitarios")
    print("📋 Colecciones que se limpiarán:")
    print("   - anuncios")
    print("   - medios_comunicacion")
    print("   - tipos_modulos")
    print("   - frecuencias_publicacion")
    
    while True:
        respuesta = input("\n¿Estás seguro de que quieres continuar? (escribe 'CONFIRMAR' para continuar): ")
        if respuesta == "CONFIRMAR":
            return True
        elif respuesta.lower() in ['no', 'n', 'cancelar', 'cancel']:
            return False
        else:
            print("❌ Respuesta inválida. Escribe 'CONFIRMAR' para continuar o 'no' para cancelar.")

def limpiar_base_datos():
    """
    Limpia todas las colecciones de la base de datos
    """
    try:
        # Conectar a MongoDB
        if not conectar():
            print("❌ No se pudo conectar a MongoDB")
            return False
        
        print("🔄 Iniciando limpieza de la base de datos...")
        
        # Contar documentos antes de limpiar
        count_anuncios = Anuncio.objects.count()
        count_medios = MedioComunicacion.objects.count()
        count_modulos = TipoModulo.objects.count()
        count_frecuencias = FrecuenciaPublicacion.objects.count()
        
        print(f"📊 Documentos a eliminar:")
        print(f"   - Anuncios: {count_anuncios}")
        print(f"   - Medios: {count_medios}")
        print(f"   - Módulos: {count_modulos}")
        print(f"   - Frecuencias: {count_frecuencias}")
        print(f"   - Total: {count_anuncios + count_medios + count_modulos + count_frecuencias}")
        
        # Eliminar todas las colecciones
        print("\n🗑️  Eliminando datos...")
        
        Anuncio.drop_collection()
        print("✅ Colección 'anuncios' eliminada")
        
        MedioComunicacion.drop_collection()
        print("✅ Colección 'medios_comunicacion' eliminada")
        
        TipoModulo.drop_collection()
        print("✅ Colección 'tipos_modulos' eliminada")
        
        FrecuenciaPublicacion.drop_collection()
        print("✅ Colección 'frecuencias_publicacion' eliminada")
        
        print("\n✅ Base de datos limpiada exitosamente")
        print("💡 La próxima vez que ejecutes el sistema, se crearán los datos iniciales automáticamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al limpiar la base de datos: {e}")
        return False
    
    finally:
        desconectar()

def main():
    """
    Función principal
    """
    print("🧹 SCRIPT DE LIMPIEZA DE BASE DE DATOS")
    print("="*50)
    
    if confirmar_limpieza():
        if limpiar_base_datos():
            print("\n🎉 Limpieza completada exitosamente")
            print("💡 Para volver a usar el sistema, ejecuta: python src/main.py")
        else:
            print("\n❌ La limpieza falló")
    else:
        print("\n🚫 Limpieza cancelada por el usuario")
        print("📊 Los datos permanecen intactos")

if __name__ == "__main__":
    main()
