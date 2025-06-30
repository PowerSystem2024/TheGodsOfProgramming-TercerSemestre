"""
Configuración del sistema de logging para el proyecto
"""
import os
import logging
import logging.config
from config.configuracion import Config


def configurar_logging():
    """
    Configura el sistema de logging de la aplicación
    """
    config = Config()
    
    # Crear directorio de logs si no existe
    log_dir = os.path.dirname(config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    
    # Aplicar configuración de logging
    logging_config = config.get_logging_config()
    logging.config.dictConfig(logging_config)
    
    # Logger principal
    logger = logging.getLogger(__name__)
    logger.info(f"Sistema de logging configurado - Nivel: {config.LOG_LEVEL}")
    logger.info(f"Archivo de log: {config.LOG_FILE}")
    
    return logger


def obtener_logger(nombre: str) -> logging.Logger:
    """
    Obtiene un logger para un módulo específico
    
    Args:
        nombre: Nombre del módulo/logger
        
    Returns:
        Logger configurado
    """
    return logging.getLogger(nombre)
