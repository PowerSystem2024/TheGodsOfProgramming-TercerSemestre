"""
Aplicación Flask para el Sistema de Gestión de Anuncios Publicitarios
"""

from flask import Flask
from src.web.routes import register_routes
from src.web.api import api_bp
from src.web.config import FlaskConfig
from src.utils.logging_config import configurar_logging
import logging
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def create_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    
    # Configurar la aplicación
    app.config.from_object(FlaskConfig)
    
    # Configurar logging
    configurar_logging()
    
    # Registrar rutas web
    register_routes(app)
    
    # Registrar API REST con Swagger
    app.register_blueprint(api_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    logger = logging.getLogger(__name__)
    logger.info("Iniciando aplicación Flask con API y Swagger")
    
    # Configuración para diferentes entornos
    port = int(os.environ.get('PORT', 5000))  # Render asigna PORT automáticamente
    host = os.environ.get('HOST', '0.0.0.0')  # 0.0.0.0 para producción, localhost para desarrollo
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    if port == 5000:  # Desarrollo local
        logger.info("Documentación Swagger disponible en: http://localhost:5000/api/v1/docs/")
    else:  # Producción (Render u otros)
        logger.info(f"Aplicación ejecutándose en puerto {port}")
        logger.info("Documentación Swagger disponible en: /api/v1/docs/")
    
    # Ejecutar aplicación
    app.run(host=host, port=port, debug=debug)
