"""
Configuración del sistema de gestión de anuncios publicitarios
"""
import os
from typing import Dict, Any


class Config:
    """
    Clase de configuración centralizada para el sistema
    """
    
    def __init__(self):
        # Configuración de MongoDB
        self.MONGODB_HOST = os.getenv('MONGODB_HOST', 'localhost')
        self.MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
        self.MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME', 'proyecto_anuncios_publicitarios')
        self.MONGODB_URL = f"mongodb://{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DB_NAME}"
        
        # Configuración de logging
        self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
        self.LOG_FILE = os.getenv('LOG_FILE', 'logs/sistema.log')
        self.LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', 10485760))  # 10MB
        self.LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', 3))
        
        # Configuración de validación
        self.MIN_EMPRESA_LENGTH = int(os.getenv('MIN_EMPRESA_LENGTH', 2))
        self.MAX_EMPRESA_LENGTH = int(os.getenv('MAX_EMPRESA_LENGTH', 100))
        
        # Configuración de la aplicación
        self.APP_NAME = os.getenv('APP_NAME', 'Sistema de Gestión de Anuncios Publicitarios')
        self.APP_VERSION = os.getenv('APP_VERSION', '2.0.0')
        self.DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
        
        # Configuración de datos de prueba
        self.CREAR_DATOS_PRUEBA = os.getenv('CREAR_DATOS_PRUEBA', 'True').lower() == 'true'
        
    def get_mongodb_config(self) -> Dict[str, Any]:
        """
        Retorna la configuración de MongoDB
        
        Returns:
            Dict con configuración de MongoDB
        """
        return {
            'host': self.MONGODB_URL,
            'db': self.MONGODB_DB_NAME,
            'connect': False,  # Para evitar problemas con threading
            'serverSelectionTimeoutMS': 3000,  # Timeout de conexión
            'connectTimeoutMS': 3000,
            'socketTimeoutMS': 3000
        }
    
    def get_logging_config(self) -> Dict[str, Any]:
        """
        Retorna la configuración de logging
        
        Returns:
            Dict con configuración de logging
        """
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
                'detailed': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'level': self.LOG_LEVEL,
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard',
                    'stream': 'ext://sys.stdout'
                },
                'file': {
                    'level': self.LOG_LEVEL,
                    'class': 'logging.handlers.RotatingFileHandler',
                    'formatter': 'detailed',
                    'filename': self.LOG_FILE,
                    'maxBytes': self.LOG_MAX_BYTES,
                    'backupCount': self.LOG_BACKUP_COUNT
                }
            },
            'loggers': {
                '': {  # root logger
                    'handlers': ['console', 'file'],
                    'level': self.LOG_LEVEL,
                    'propagate': False
                }
            }
        }
    
    def __str__(self) -> str:
        """
        Representación en string de la configuración (ocultando datos sensibles)
        """
        return f"""
{self.APP_NAME} v{self.APP_VERSION}
===========================================
MongoDB: {self.MONGODB_HOST}:{self.MONGODB_PORT}
Base de datos: {self.MONGODB_DB_NAME}  
Logging: {self.LOG_LEVEL} -> {self.LOG_FILE}
Debug: {self.DEBUG}
Datos de prueba: {self.CREAR_DATOS_PRUEBA}
===========================================
        """
