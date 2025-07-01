"""
Tests de integración básicos
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.anuncio_service import AnuncioService
from services.datos_basicos_service import DatosBasicosService


class TestIntegracionBasica(unittest.TestCase):
    """
    Tests de integración básicos que no dependen de MongoEngine real
    """
    
    @patch('src.models.medio_comunicacion.MedioComunicacion.save')
    @patch('src.models.medio_comunicacion.MedioComunicacion.objects')
    def test_inicializacion_datos_basicos(self, mock_objects, mock_save):
        """Test de inicialización de datos básicos"""
        # Arrange
        mock_objects.return_value.first.return_value = None  # No existe
        
        # Act
        medios = DatosBasicosService.inicializar_medios_comunicacion()
        
        # Assert
        self.assertIsNotNone(medios)

    @patch('src.models.anuncio.Anuncio.objects')
    def test_servicio_anuncios_obtener_todos(self, mock_objects):
        """Test básico del servicio de anuncios"""
        # Arrange
        mock_anuncios = [MagicMock(), MagicMock()]
        mock_objects.return_value.all.return_value = mock_anuncios
        
        # Act
        resultado = AnuncioService.obtener_todos_los_anuncios()
        
        # Assert
        self.assertEqual(len(resultado), 2)

    def test_servicios_existen(self):
        """Test que verifica que los servicios principales existen"""
        # Verificar que las clases de servicio existen
        self.assertTrue(hasattr(AnuncioService, 'obtener_todos_los_anuncios'))
        self.assertTrue(hasattr(AnuncioService, 'obtener_anuncio_por_id'))
        self.assertTrue(hasattr(AnuncioService, 'buscar_anuncios'))
        self.assertTrue(hasattr(AnuncioService, 'generar_matriz_precios'))
        self.assertTrue(hasattr(DatosBasicosService, 'inicializar_medios_comunicacion'))


if __name__ == '__main__':
    unittest.main()
