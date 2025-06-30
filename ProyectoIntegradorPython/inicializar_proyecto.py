"""
Script de inicialización del proyecto con la nueva estructura
"""
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from utils.logging_config import configurar_logging
from db.conexion import conectar, desconectar
from services.datos_basicos_service import DatosBasicosService
from services.anuncio_service import AnuncioService
from config.configuracion import Config


def inicializar_proyecto():
    """
    Inicializa el proyecto con la nueva estructura
    """
    print("🚀 Inicializando Sistema de Gestión de Anuncios Publicitarios v2.0")
    print("=" * 70)
    
    # Configurar logging
    logger = configurar_logging()
    logger.info("Iniciando inicialización del proyecto")
    
    # Mostrar configuración
    config = Config()
    print(config)
    
    # Conectar a MongoDB
    if not conectar():
        print("❌ No se pudo conectar a MongoDB")
        return False
    
    try:
        print("🔄 Inicializando datos básicos...")
        
        # Inicializar datos básicos
        medios = DatosBasicosService.inicializar_medios_comunicacion()
        modulos = DatosBasicosService.inicializar_tipos_modulos()
        frecuencias = DatosBasicosService.inicializar_frecuencias_publicacion()
        
        print(f"✅ {len(medios)} medios de comunicación inicializados")
        print(f"✅ {len(modulos)} tipos de módulos inicializados") 
        print(f"✅ {len(frecuencias)} frecuencias de publicación inicializadas")
        
        # Inicializar anuncios de prueba si están habilitados
        if config.CREAR_DATOS_PRUEBA:
            print("🔄 Inicializando anuncios de prueba...")
            AnuncioService.inicializar_anuncios_prueba(medios, modulos, frecuencias)
            anuncios = AnuncioService.obtener_todos_los_anuncios()
            print(f"✅ {len(anuncios)} anuncios de prueba inicializados")
        
        # Mostrar estadísticas finales
        total_ingresos = AnuncioService.calcular_ingresos_totales()
        print(f"\n📊 ESTADÍSTICAS DEL SISTEMA:")
        print(f"💰 Ingresos totales: ${total_ingresos:,.2f}")
        
        print("\n🎉 ¡Proyecto inicializado exitosamente!")
        print("💡 Para usar el sistema:")
        print("   - Aplicación principal: python src/main_nuevo.py")
        print("   - Aplicación antigua: python src/main.py")
        print("   - Tests: python -m unittest discover tests")
        print("   - Demostración: python demo_mongodb.py")
        
        logger.info("Proyecto inicializado exitosamente")
        return True
        
    except Exception as e:
        print(f"❌ Error durante la inicialización: {e}")
        logger.error(f"Error durante la inicialización: {e}", exc_info=True)
        return False
    
    finally:
        desconectar()


if __name__ == "__main__":
    inicializar_proyecto()
