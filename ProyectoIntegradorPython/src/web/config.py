"""
Configuración para la aplicación Flask
"""

import os
from src.config.configuracion import Config

class FlaskConfig:
    """Configuración de Flask usando la configuración del sistema existente"""
    
    # Clave secreta para formularios
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Configuración de debug
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Configuración de testing
    TESTING = False
    
    # Configuración WTF
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
    
    @staticmethod
    def get_db_config():
        """Obtiene la configuración de base de datos del sistema existente"""
        config = Config()
        return {
            'host': config.MONGODB_HOST,
            'port': config.MONGODB_PORT,
            'db_name': config.MONGODB_DB_NAME
        }
