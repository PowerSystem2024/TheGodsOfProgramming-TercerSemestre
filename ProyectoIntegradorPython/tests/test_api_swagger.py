"""
Tests para la API REST con Swagger
"""

import pytest
import json
from unittest.mock import patch, MagicMock
from flask import url_for

# Importar la aplicación Flask
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app


class TestAPI:
    """Tests para la API REST"""
    
    @pytest.fixture
    def app(self):
        """Fixture para crear la aplicación Flask en modo testing"""
        with patch('src.web.api.controlador'):
            app = create_app()
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            app.config['SECRET_KEY'] = 'test-secret-key'
            return app
    
    @pytest.fixture
    def client(self, app):
        """Cliente de prueba para realizar requests HTTP"""
        return app.test_client()
    
    @pytest.fixture
    def mock_controlador(self):
        """Mock del controlador para usar en tests"""
        mock = MagicMock()
        
        # Mock del servicio de anuncios
        mock.anuncio_service = MagicMock()
        mock.anuncio_service.listar_anuncios.return_value = []
        mock.anuncio_service.obtener_anuncio_por_id.return_value = None
        mock.anuncio_service.buscar_anuncios.return_value = []
        mock.anuncio_service.crear_anuncio_web.return_value = {'exitoso': True, 'mensaje': 'OK'}
        mock.anuncio_service.eliminar_anuncio_web.return_value = {'exitoso': True, 'mensaje': 'OK'}
        mock.anuncio_service.generar_matriz_precios.return_value = {}
        
        # Mock del servicio de datos básicos
        mock.datos_basicos_service = MagicMock()
        mock.datos_basicos_service.listar_medios_comunicacion.return_value = []
        mock.datos_basicos_service.listar_tipos_modulo.return_value = []
        mock.datos_basicos_service.listar_frecuencias_publicacion.return_value = []
        
        return mock

    def test_swagger_docs_available(self, client):
        """Test que la documentación Swagger esté disponible"""
        response = client.get('/api/v1/docs/')
        assert response.status_code == 200
        assert b'swagger' in response.data.lower()

    def test_api_anuncios_list_get(self, client):
        """Test GET /api/v1/anuncios/"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.listar_anuncios.return_value = []
            
            response = client.get('/api/v1/anuncios/')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)

    def test_api_anuncios_list_post(self, client):
        """Test POST /api/v1/anuncios/"""
        anuncio_data = {
            'empresa': 'Test Corp',
            'precio': 1000.0,
            'medio_comunicacion_id': '507f1f77bcf86cd799439011',
            'tipo_modulo_id': '507f1f77bcf86cd799439012',
            'frecuencia_publicacion_id': '507f1f77bcf86cd799439013'
        }
        
        with patch('src.web.api.controlador') as mock_controlador:
            mock_anuncio = MagicMock()
            mock_anuncio.id = '507f1f77bcf86cd799439014'
            mock_controlador.anuncio_service.crear_anuncio_web.return_value = {
                'exitoso': True, 
                'mensaje': 'OK', 
                'anuncio': mock_anuncio
            }
            
            response = client.post('/api/v1/anuncios/', 
                                 data=json.dumps(anuncio_data),
                                 content_type='application/json')
            
            assert response.status_code == 201
            data = json.loads(response.data)
            assert data['exitoso'] == True

    def test_api_anuncio_detail_get(self, client):
        """Test GET /api/v1/anuncios/<id>"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_anuncio = MagicMock()
            mock_anuncio.id = '507f1f77bcf86cd799439011'
            mock_anuncio.empresa = 'Test Corp'
            mock_anuncio.precio = 1000.0
            mock_anuncio.medio.nombre = 'El Norteño'
            mock_anuncio.modulo.nombre = 'M1'
            mock_anuncio.frecuencia.nombre = 'Diario'
            mock_anuncio.fecha_creacion = None
            mock_anuncio.activo = True
            
            mock_controlador.anuncio_service.obtener_anuncio_por_id.return_value = mock_anuncio
            
            response = client.get('/api/v1/anuncios/507f1f77bcf86cd799439011')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['empresa'] == 'Test Corp'

    def test_api_anuncio_delete(self, client):
        """Test DELETE /api/v1/anuncios/<id>"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.eliminar_anuncio_web.return_value = {
                'exitoso': True, 
                'mensaje': 'Anuncio eliminado'
            }
            
            response = client.delete('/api/v1/anuncios/507f1f77bcf86cd799439011')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['exitoso'] == True

    def test_api_buscar_anuncios(self, client):
        """Test POST /api/v1/anuncios/buscar"""
        criterios = {
            'termino': 'test',
            'precio_min': 100,
            'precio_max': 2000
        }
        
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.buscar_anuncios.return_value = []
            
            response = client.post('/api/v1/anuncios/buscar', 
                                 data=json.dumps(criterios),
                                 content_type='application/json')
            
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)

    def test_api_configuracion_medios(self, client):
        """Test GET /api/v1/configuracion/medios"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.datos_basicos_service.listar_medios_comunicacion.return_value = []
            
            response = client.get('/api/v1/configuracion/medios')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)

    def test_api_configuracion_tipos(self, client):
        """Test GET /api/v1/configuracion/tipos"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.datos_basicos_service.listar_tipos_modulo.return_value = []
            
            response = client.get('/api/v1/configuracion/tipos')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)

    def test_api_configuracion_frecuencias(self, client):
        """Test GET /api/v1/configuracion/frecuencias"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.datos_basicos_service.listar_frecuencias_publicacion.return_value = []
            
            response = client.get('/api/v1/configuracion/frecuencias')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert isinstance(data, list)

    def test_api_matriz_precios(self, client):
        """Test GET /api/v1/reportes/matriz-precios"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.generar_matriz_precios.return_value = {
                'El Norteño': {
                    'M1': {'promedio': 1000, 'cantidad': 5}
                }
            }
            
            response = client.get('/api/v1/reportes/matriz-precios')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['exitoso'] == True
            assert 'datos' in data

    def test_api_estadisticas(self, client):
        """Test GET /api/v1/reportes/estadisticas"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_anuncio = MagicMock()
            mock_anuncio.precio = 1000.0
            
            mock_controlador.anuncio_service.listar_anuncios.return_value = [mock_anuncio]
            mock_controlador.datos_basicos_service.listar_medios_comunicacion.return_value = []
            mock_controlador.datos_basicos_service.listar_tipos_modulo.return_value = []
            mock_controlador.datos_basicos_service.listar_frecuencias_publicacion.return_value = []
            
            response = client.get('/api/v1/reportes/estadisticas')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['exitoso'] == True
            assert 'datos' in data

    def test_api_error_handling(self, client):
        """Test manejo de errores de la API"""
        # Test anuncio no encontrado
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.obtener_anuncio_por_id.return_value = None
            
            response = client.get('/api/v1/anuncios/507f1f77bcf86cd799439999')
            assert response.status_code == 404
            # Solo verificamos que el status code sea correcto

    def test_api_validation_errors(self, client):
        """Test validación de datos de entrada"""
        # Test POST sin datos requeridos
        anuncio_data = {
            'empresa': 'Test Corp'
            # Faltan campos requeridos
        }
        
        with patch('src.web.api.controlador'):
            response = client.post('/api/v1/anuncios/', 
                                 data=json.dumps(anuncio_data),
                                 content_type='application/json')
            
            assert response.status_code == 400
            data = json.loads(response.data)
            assert data['exitoso'] == False

    def test_api_content_type(self, client):
        """Test que la API devuelva JSON"""
        with patch('src.web.api.controlador') as mock_controlador:
            mock_controlador.anuncio_service.listar_anuncios.return_value = []
            
            response = client.get('/api/v1/anuncios/')
            assert response.status_code == 200
            assert 'application/json' in response.content_type


if __name__ == '__main__':
    pytest.main([__file__])
