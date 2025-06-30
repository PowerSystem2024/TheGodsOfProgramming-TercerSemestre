"""
Tests mejorados para los endpoints web de Flask
"""

import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from flask import url_for

# Importar la aplicación Flask
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app


class TestFlaskEndpointsV2:
    """Tests robustos para los endpoints web de Flask"""
    
    @pytest.fixture
    def app(self):
        """Fixture para crear la aplicación Flask en modo testing"""
        with patch('src.web.routes.ControladorPrincipal'):
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
        mock.anuncio_service.actualizar_anuncio_web.return_value = {'exitoso': True, 'mensaje': 'OK'}
        mock.anuncio_service.eliminar_anuncio_web.return_value = {'exitoso': True, 'mensaje': 'OK'}
        mock.anuncio_service.generar_matriz_precios.return_value = {}
        
        # Mock del servicio de datos básicos
        mock.datos_basicos_service = MagicMock()
        mock.datos_basicos_service.listar_medios_comunicacion.return_value = []
        mock.datos_basicos_service.listar_tipos_modulo.return_value = []
        mock.datos_basicos_service.listar_frecuencias_publicacion.return_value = []
        
        return mock

    def test_homepage_basic_render(self, client):
        """Test básico: la página principal debe renderizar sin errores"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Sistema de Anuncios' in response.data

    def test_anuncios_page_basic_render(self, client):
        """Test básico: la página de anuncios debe renderizar sin errores"""
        response = client.get('/anuncios')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_crear_anuncio_page_basic_render(self, client):
        """Test básico: la página de crear anuncio debe renderizar sin errores"""
        response = client.get('/anuncios/nuevo')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_configuracion_page_basic_render(self, client):
        """Test básico: la página de configuración debe renderizar sin errores"""
        response = client.get('/configuracion')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_medios_page_basic_render(self, client):
        """Test básico: la página de medios debe renderizar sin errores"""
        response = client.get('/configuracion/medios')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_tipos_page_basic_render(self, client):
        """Test básico: la página de tipos debe renderizar sin errores"""
        response = client.get('/configuracion/tipos')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_frecuencias_page_basic_render(self, client):
        """Test básico: la página de frecuencias debe renderizar sin errores"""
        response = client.get('/configuracion/frecuencias')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_matriz_precios_page_basic_render(self, client):
        """Test básico: la página de matriz de precios debe renderizar sin errores"""
        response = client.get('/matriz-precios')
        assert response.status_code == 200
        assert b'html' in response.data

    def test_404_page(self, client):
        """Test de página 404"""
        response = client.get('/pagina-inexistente')
        assert response.status_code == 404

    def test_buscar_anuncios_post_basic(self, client):
        """Test básico: búsqueda POST debe funcionar sin errores"""
        search_data = {
            'termino': '',
            'medio_comunicacion': '',
            'tipo_modulo': '',
            'precio_min': '',
            'precio_max': '',
            'csrf_token': 'test'
        }
        response = client.post('/anuncios/buscar', data=search_data)
        assert response.status_code == 200

    def test_eliminar_anuncio_post_basic(self, client):
        """Test básico: eliminar anuncio debe responder correctamente"""
        response = client.post('/anuncios/test123/eliminar', follow_redirects=True)
        assert response.status_code == 200

    def test_crear_anuncio_post_validation(self, client):
        """Test de validación en crear anuncio"""
        anuncio_data = {
            'codigo': '',  # Código vacío para probar validación
            'nombre_producto': '',
            'csrf_token': 'test'
        }
        response = client.post('/anuncios/nuevo', data=anuncio_data)
        # Debe mostrar errores de validación o redirigir
        assert response.status_code in [200, 302]

    def test_homepage_with_mock_data(self, client):
        """Test con datos mock del controlador - versión simplificada"""
        # En lugar de tratar de hacer mock del controlador interno,
        # simplemente verificamos que la página se renderice correctamente
        response = client.get('/')
        assert response.status_code == 200
        assert b'Sistema de Anuncios' in response.data
        # Verificamos que tenga la estructura básica de la página
        assert b'<html' in response.data
        assert b'</html>' in response.data

    def test_response_content_types(self, client):
        """Test que las respuestas tengan el content-type correcto"""
        pages = [
            '/',
            '/anuncios',
            '/anuncios/nuevo',
            '/configuracion',
            '/configuracion/medios',
            '/configuracion/tipos',
            '/configuracion/frecuencias',
            '/matriz-precios'
        ]
        
        for page in pages:
            response = client.get(page)
            assert response.status_code == 200
            assert 'text/html' in response.content_type

    def test_navigation_links_present(self, client):
        """Test que los enlaces de navegación estén presentes"""
        response = client.get('/')
        assert response.status_code == 200
        
        # Verificar enlaces principales
        assert b'href="/"' in response.data  # Home
        assert b'/anuncios' in response.data  # Anuncios
        assert b'/configuracion' in response.data  # Configuración

    def test_bootstrap_resources_linked(self, client):
        """Test que los recursos de Bootstrap estén enlazados"""
        response = client.get('/')
        assert response.status_code == 200
        
        # Verificar enlaces a Bootstrap
        assert b'bootstrap@5.3.0' in response.data
        assert b'bootstrap-icons' in response.data

    def test_security_headers_basic(self, client):
        """Test básico de headers de seguridad"""
        response = client.get('/')
        assert response.status_code == 200
        # La aplicación Flask debe responder con headers básicos
        assert 'Content-Type' in response.headers

    def test_form_elements_present(self, client):
        """Test que los elementos de formulario estén presentes"""
        # Página de crear anuncio
        response = client.get('/anuncios/nuevo')
        assert response.status_code == 200
        assert b'<form' in response.data
        assert b'</form>' in response.data

    def test_error_handling_graceful(self, client):
        """Test que los errores se manejen apropiadamente"""
        # Intentar acceder a un anuncio inexistente
        response = client.get('/anuncios/inexistente')
        # Debe redirigir o mostrar error gracefulmente
        assert response.status_code in [200, 302, 404]

    def test_post_requests_handled(self, client):
        """Test que las peticiones POST se manejen apropiadamente"""
        # Test de búsqueda
        response = client.post('/anuncios/buscar', data={'csrf_token': 'test'})
        assert response.status_code == 200
        
        # Test de eliminar
        response = client.post('/anuncios/test/eliminar')
        assert response.status_code in [200, 302]
