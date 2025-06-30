"""
Tests de integración para el sistema completo
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from controllers.controlador_principal import ControladorPrincipal
from services.anuncio_service import AnuncioService
from services.datos_basicos_service import DatosBasicosService


class TestIntegracionSistema(unittest.TestCase):
    """
    Tests de integración para el sistema completo
    """
    
    @patch('db.conexion.conectar')
    @patch('db.conexion.desconectar')
    def test_flujo_completo_agregar_anuncio(self, mock_desconectar, mock_conectar):
        """Test del flujo completo de agregar un anuncio"""
        # Arrange
        mock_conectar.return_value = True
        
        with patch.object(DatosBasicosService, 'inicializar_medios_comunicacion') as mock_medios, \
             patch.object(DatosBasicosService, 'inicializar_tipos_modulos') as mock_modulos, \
             patch.object(DatosBasicosService, 'inicializar_frecuencias_publicacion') as mock_frecuencias, \
             patch.object(AnuncioService, 'inicializar_anuncios_prueba'), \
             patch.object(AnuncioService, 'obtener_todos_los_anuncios') as mock_obtener, \
             patch.object(AnuncioService, 'crear_anuncio') as mock_crear:
            
            # Configurar mocks
            mock_medio = MagicMock()
            mock_medio.get_nombre.return_value = "El Norteño"
            mock_modulo = MagicMock()
            mock_modulo.get_nombre.return_value = "M1"
            mock_frecuencia = MagicMock()
            mock_frecuencia.get_nombre.return_value = "D"
            
            mock_medios.return_value = [mock_medio]
            mock_modulos.return_value = [mock_modulo]
            mock_frecuencias.return_value = [mock_frecuencia]
            mock_obtener.return_value = []
            
            mock_anuncio_creado = MagicMock()
            mock_crear.return_value = mock_anuncio_creado
            
            # Simular entrada del usuario
            with patch('builtins.input', side_effect=['1', '1', '1', 'Test Corp', '0']):
                controlador = ControladorPrincipal()
                
                # Act - Inicializar sistema
                resultado_init = controlador.inicializar_sistema()
                
                # Assert - Inicialización
                self.assertTrue(resultado_init)
                
                # Act - Agregar anuncio
                controlador._agregar_anuncio()
                
                # Assert - Anuncio creado
                mock_crear.assert_called_once()
    
    def test_validacion_datos_entrada(self):
        """Test de validación de datos de entrada"""
        controlador = ControladorPrincipal()
        
        # Test validación nombre empresa
        with patch('builtins.input', return_value=''):
            resultado = controlador.ui.obtener_nombre_empresa()
            self.assertIsNone(resultado)
    
    @patch('controllers.controlador_principal.conectar')
    def test_manejo_error_conexion(self, mock_conectar):
        """Test del manejo de errores de conexión"""
        # Arrange
        mock_conectar.return_value = False
        
        # Act
        controlador = ControladorPrincipal()
        resultado = controlador.inicializar_sistema()
        
        # Assert
        self.assertFalse(resultado)
        mock_conectar.assert_called_once()


if __name__ == '__main__':
    unittest.main()
