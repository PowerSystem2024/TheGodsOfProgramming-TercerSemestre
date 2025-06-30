"""
Tests de integración actualizados para el sistema de anuncios con MongoDB
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.anuncio_service import AnuncioService
from services.datos_basicos_service import DatosBasicosService


class TestIntegracionAnuncios(unittest.TestCase):
    """
    Tests de integración para el sistema de anuncios
    """
    
    @patch('models.anuncio.Anuncio.save')
    @patch('models.anuncio.Anuncio.objects')
    def test_ciclo_completo_anuncio(self, mock_objects, mock_save):
        """Test del ciclo completo de un anuncio"""
        # Arrange
        mock_medio = MagicMock()
        mock_modulo = MagicMock()
        mock_frecuencia = MagicMock()
        
        # Act - Crear anuncio
        anuncio = AnuncioService.crear_anuncio(
            mock_medio, mock_modulo, mock_frecuencia, 1000.0, "Test Corp"
        )
        
        # Assert - Anuncio creado
        self.assertIsNotNone(anuncio)
        mock_save.assert_called_once()
    
    @patch('models.medio_comunicacion.MedioComunicacion.save')
    @patch('models.medio_comunicacion.MedioComunicacion.objects')
    def test_inicializacion_datos_basicos(self, mock_objects, mock_save):
        """Test de inicialización de datos básicos"""
        # Arrange
        mock_objects.return_value.first.return_value = None  # No existe
        
        # Act
        medios = DatosBasicosService.inicializar_medios_comunicacion()
        
        # Assert
        self.assertIsNotNone(medios)


if __name__ == '__main__':
    unittest.main()
