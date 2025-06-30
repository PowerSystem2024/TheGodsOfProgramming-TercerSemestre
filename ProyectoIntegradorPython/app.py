"""
Aplicación Flask para el Sistema de Gestión de Anuncios Publicitarios
"""

from flask import Flask
from src.web.routes import register_routes
from src.web.config import FlaskConfig
from src.utils.logging_config import configurar_logging
import logging

def create_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    
    # Configurar la aplicación
    app.config.from_object(FlaskConfig)
    
    # Configurar logging
    configurar_logging()
    
    # Registrar rutas
    register_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    logger = logging.getLogger(__name__)
    logger.info("Iniciando aplicación Flask")
    
    # Ejecutar en modo debug durante desarrollo
    app.run(debug=True, port=5000)
