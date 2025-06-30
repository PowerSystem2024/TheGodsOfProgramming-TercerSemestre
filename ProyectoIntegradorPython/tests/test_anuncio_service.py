"""
Tests para el servicio de anuncios
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.anuncio_service import AnuncioService


class TestAnuncioService(unittest.TestCase):
    """
    Tests para el servicio de anuncios
    """
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.mock_medio = MagicMock()
        self.mock_medio.nombre = "El Norteño"
        self.mock_medio.id = "mock_medio_id"
        
        self.mock_modulo = MagicMock()
        self.mock_modulo.nombre = "M1"
        self.mock_modulo.id = "mock_modulo_id"
        
        self.mock_frecuencia = MagicMock()
        self.mock_frecuencia.nombre = "D"
        self.mock_frecuencia.id = "mock_frecuencia_id"
    
    @patch('models.anuncio.Anuncio.save')
    def test_crear_anuncio(self, mock_save):
        """Test para crear un anuncio"""
        # Arrange
        empresa = "Test Corp"
        precio = 1000.0
        
        # Act
        resultado = AnuncioService.crear_anuncio(
            self.mock_medio, self.mock_modulo, self.mock_frecuencia, precio, empresa
        )
        
        # Assert
        self.assertIsNotNone(resultado)
        mock_save.assert_called_once()
    
    @patch('models.anuncio.Anuncio.objects')
    def test_obtener_todos_los_anuncios(self, mock_objects):
        """Test para obtener todos los anuncios"""
        # Arrange
        mock_anuncios = [MagicMock(), MagicMock()]
        mock_objects.return_value.all.return_value = mock_anuncios
        
        # Act
        resultado = AnuncioService.obtener_todos_los_anuncios()
        
        # Assert
        self.assertEqual(len(resultado), 2)
        mock_objects.assert_called_once_with(activo=True)
    
    @patch('models.anuncio.Anuncio.objects')
    def test_buscar_anuncios_por_empresa(self, mock_objects):
        """Test para buscar anuncios por empresa"""
        # Arrange
        empresa = "Test Corp"
        mock_anuncios = [MagicMock()]
        mock_objects.return_value.all.return_value = mock_anuncios
        
        # Act
        resultado = AnuncioService.buscar_anuncios_por_empresa(empresa)
        
        # Assert
        self.assertEqual(len(resultado), 1)
        mock_objects.assert_called_once()
    
    @patch('models.anuncio.Anuncio.objects')
    def test_calcular_ingresos_totales(self, mock_objects):
        """Test para calcular ingresos totales"""
        # Arrange
        mock_anuncio1 = MagicMock()
        mock_anuncio1.precio = 1000.0
        mock_anuncio2 = MagicMock()
        mock_anuncio2.precio = 2000.0
        mock_objects.return_value.all.return_value = [mock_anuncio1, mock_anuncio2]
        
        # Act
        resultado = AnuncioService.calcular_ingresos_totales()
        
        # Assert
        self.assertEqual(resultado, 3000.0)


if __name__ == '__main__':
    unittest.main()
