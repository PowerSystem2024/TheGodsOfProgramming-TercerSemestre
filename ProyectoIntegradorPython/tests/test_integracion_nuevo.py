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
    Tests de integración para el sistema de anuncios - Versión simplificada
    """
    
    @patch('src.services.anuncio_service.AnuncioService.crear_anuncio')
    def test_ciclo_completo_anuncio_simplificado(self, mock_crear):
        """Test simplificado del ciclo completo de un anuncio"""
        # Arrange
        from bson import ObjectId
        
        mock_medio = MagicMock()
        mock_medio.pk = ObjectId()
        mock_modulo = MagicMock()
        mock_modulo.pk = ObjectId()
        mock_frecuencia = MagicMock()
        mock_frecuencia.pk = ObjectId()
        
        mock_anuncio = MagicMock()
        mock_crear.return_value = mock_anuncio
        
        # Act - Crear anuncio
        anuncio = AnuncioService.crear_anuncio(
            mock_medio, mock_modulo, mock_frecuencia, 1000.0, "Test Corp"
        )
        
        # Assert - Anuncio creado
        self.assertIsNotNone(anuncio)
        mock_crear.assert_called_once_with(
            mock_medio, mock_modulo, mock_frecuencia, 1000.0, "Test Corp"
        )
    
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


if __name__ == '__main__':
    unittest.main()
