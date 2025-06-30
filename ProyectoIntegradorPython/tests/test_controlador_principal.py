"""
Tests para el controlador principal
"""
import unittest
from unittest.mock import patch, MagicMock

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from controllers.controlador_principal import ControladorPrincipal


class TestControladorPrincipal(unittest.TestCase):
    """
    Tests para el controlador principal
    """
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.controlador = ControladorPrincipal()
    
    @patch('controllers.controlador_principal.conectar')
    @patch('controllers.controlador_principal.DatosBasicosService')
    @patch('controllers.controlador_principal.AnuncioService')
    def test_inicializar_sistema_exitoso(self, mock_anuncio_service, mock_datos_service, mock_conectar):
        """Test para inicialización exitosa del sistema"""
        # Arrange
        mock_conectar.return_value = True
        mock_datos_service.inicializar_medios_comunicacion.return_value = [MagicMock()]
        mock_datos_service.inicializar_tipos_modulos.return_value = [MagicMock()]
        mock_datos_service.inicializar_frecuencias_publicacion.return_value = [MagicMock()]
        mock_anuncio_service.obtener_todos_los_anuncios.return_value = [MagicMock()]
        
        # Act
        resultado = self.controlador.inicializar_sistema()
        
        # Assert
        self.assertTrue(resultado)
        mock_conectar.assert_called_once()
    
    @patch('controllers.controlador_principal.conectar')
    def test_inicializar_sistema_fallo_conexion(self, mock_conectar):
        """Test para fallo en conexión durante inicialización"""
        # Arrange
        mock_conectar.return_value = False
        
        # Act
        resultado = self.controlador.inicializar_sistema()
        
        # Assert
        self.assertFalse(resultado)
    
    def test_procesar_opcion_invalida(self):
        """Test para procesar opción inválida"""
        # Este test verifica que no se lance excepción con opción inválida
        with patch.object(self.controlador.ui, 'mostrar_mensaje_error') as mock_error:
            self.controlador._procesar_opcion(99)
            mock_error.assert_called_once()


if __name__ == '__main__':
    unittest.main()
