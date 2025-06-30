"""
Punto de entrada principal del Sistema de Gestión de Anuncios Publicitarios
"""
import sys
import os

# Agregar el directorio actual al path para las importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.utils.logging_config import configurar_logging
from controllers.controlador_principal import ControladorPrincipal
from src.config.configuracion import Config


def main():
    """
    Función principal del programa
    """
    try:
        # Configurar logging
        logger = configurar_logging()
        
        # Mostrar información de configuración
        config = Config()
        if config.DEBUG:
            print(config)
        
        # Crear y ejecutar controlador principal
        print(f"🚀 Iniciando {config.APP_NAME} v{config.APP_VERSION}...")
        logger.info(f"Iniciando {config.APP_NAME} v{config.APP_VERSION}")
        
        controlador = ControladorPrincipal()
        controlador.ejecutar()
        
        logger.info("Aplicación finalizada correctamente")
        
    except KeyboardInterrupt:
        print("\n🛑 Programa interrumpido por el usuario")
        logger.info("Programa interrumpido por el usuario")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        logger.critical(f"Error crítico: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
