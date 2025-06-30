"""
Controlador principal del sistema de gestión de anuncios publicitarios
Versión simplificada para aplicación web únicamente
"""
from typing import List
import logging

from src.db.conexion import conectar, desconectar
from src.services.datos_basicos_service import DatosBasicosService
from src.services.anuncio_service import AnuncioService
from src.models.medio_comunicacion import MedioComunicacion
from src.models.tipo_modulo import TipoModulo
from src.models.frecuencia_publicacion import FrecuenciaPublicacion


class ControladorPrincipal:
    """
    Controlador principal que coordina las operaciones del sistema.
    Simplificado para uso web únicamente.
    """
    
    def __init__(self):
        """Inicializa el controlador"""
        self.logger = logging.getLogger(__name__)
        self.datos_basicos_service = DatosBasicosService()
        self.anuncio_service = AnuncioService()
        
        # Referencias a datos básicos
        self.medios_comunicacion: List[MedioComunicacion] = []
        self.tipos_modulos: List[TipoModulo] = []
        self.frecuencias_publicacion: List[FrecuenciaPublicacion] = []
        
        # Inicializar conexión automáticamente para web
        try:
            conectar()
            self._cargar_datos_basicos()
        except Exception as e:
            self.logger.warning(f"Error al conectar automáticamente: {e}")
        
    def inicializar_sistema(self) -> bool:
        """
        Inicializa el sistema conectando a la base de datos y cargando datos básicos
        
        Returns:
            bool: True si la inicialización fue exitosa, False en caso contrario
        """
        try:
            # Conectar a MongoDB
            if not conectar():
                self.logger.error("No se pudo conectar a MongoDB")
                return False
                
            self.logger.info("Inicializando datos desde MongoDB...")
            
            # Cargar datos básicos
            self._cargar_datos_basicos()
            
            # Inicializar datos de prueba si es necesario
            self.datos_basicos_service.inicializar_datos_basicos()
            
            self.logger.info(
                f"Sistema inicializado: {len(self.medios_comunicacion)} medios, "
                f"{len(self.tipos_modulos)} tipos, {len(self.frecuencias_publicacion)} frecuencias"
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error al inicializar sistema: {e}")
            return False
    
    def _cargar_datos_basicos(self) -> None:
        """Carga los datos básicos desde la base de datos"""
        try:
            self.medios_comunicacion = self.datos_basicos_service.obtener_medios()
            self.tipos_modulos = self.datos_basicos_service.obtener_tipos()
            self.frecuencias_publicacion = self.datos_basicos_service.obtener_frecuencias()
        except Exception as e:
            self.logger.error(f"Error al cargar datos básicos: {e}")
    
    def obtener_anuncio_service(self) -> AnuncioService:
        """Obtiene el servicio de anuncios"""
        return self.anuncio_service
    
    def obtener_datos_basicos_service(self) -> DatosBasicosService:
        """Obtiene el servicio de datos básicos"""
        return self.datos_basicos_service
    
    def obtener_medios(self) -> List[MedioComunicacion]:
        """Obtiene la lista de medios de comunicación"""
        return self.medios_comunicacion
    
    def obtener_tipos(self) -> List[TipoModulo]:
        """Obtiene la lista de tipos de módulo"""
        return self.tipos_modulos
    
    def obtener_frecuencias(self) -> List[FrecuenciaPublicacion]:
        """Obtiene la lista de frecuencias de publicación"""
        return self.frecuencias_publicacion
