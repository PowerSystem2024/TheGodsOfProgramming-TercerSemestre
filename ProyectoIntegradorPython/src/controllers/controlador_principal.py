"""
Controlador principal del sistema de gestión de anuncios publicitarios
"""
from typing import List, Optional
import logging

from src.db.conexion import conectar, desconectar
from src.services.datos_basicos_service import DatosBasicosService
from src.services.anuncio_service import AnuncioService
from src.ui.interfaz_usuario import InterfazUsuario
from src.models.anuncio import Anuncio
from src.models.medio_comunicacion import MedioComunicacion
from src.models.tipo_modulo import TipoModulo
from src.models.frecuencia_publicacion import FrecuenciaPublicacion
from src.config.configuracion import Config


class ControladorPrincipal:
    """
    Controlador principal que coordina las operaciones del sistema
    """
    
    def __init__(self):
        self.ui = InterfazUsuario()
        self.config = Config()
        self.logger = logging.getLogger(__name__)
        
        # Inicializar servicios
        self.datos_basicos_service = DatosBasicosService()
        self.anuncio_service = AnuncioService()
        
        # Datos en memoria para operaciones rápidas
        self.medios_comunicacion: List[MedioComunicacion] = []
        self.tipos_modulos: List[TipoModulo] = []
        self.frecuencias_publicacion: List[FrecuenciaPublicacion] = []
        self.anuncios: List[Anuncio] = []
        
        # Inicializar conexión automáticamente para web
        try:
            conectar()
        except Exception as e:
            self.logger.warning(f"Error al conectar automáticamente: {e}")

    def inicializar_sistema(self) -> bool:
        """
        Inicializa el sistema conectando a la BD y cargando datos
        
        Returns:
            bool: True si la inicialización fue exitosa
        """
        try:
            # Conectar a MongoDB
            if not conectar():
                self.ui.mostrar_mensaje_error("No se pudo conectar a MongoDB")
                return False
            
            # Inicializar datos básicos
            self.ui.mostrar_mensaje_info("Inicializando datos desde MongoDB...")
            self._inicializar_datos_basicos()
            
            # Inicializar anuncios de prueba si es necesario
            self._inicializar_anuncios_prueba()
            
            # Cargar anuncios activos
            self._cargar_anuncios()
            
            self.ui.mostrar_mensaje_exito(
                f"Sistema inicializado: {len(self.medios_comunicacion)} medios, "
                f"{len(self.tipos_modulos)} módulos, {len(self.frecuencias_publicacion)} frecuencias, "
                f"{len(self.anuncios)} anuncios"
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error al inicializar sistema: {e}")
            self.ui.mostrar_mensaje_error(f"Error al inicializar sistema: {e}")
            return False

    def _inicializar_datos_basicos(self) -> None:
        """
        Inicializa los datos básicos del sistema
        """
        self.medios_comunicacion = DatosBasicosService.inicializar_medios_comunicacion()
        self.tipos_modulos = DatosBasicosService.inicializar_tipos_modulos()
        self.frecuencias_publicacion = DatosBasicosService.inicializar_frecuencias_publicacion()

    def _inicializar_anuncios_prueba(self) -> None:
        """
        Inicializa anuncios de prueba si es necesario
        """
        AnuncioService.inicializar_anuncios_prueba(
            self.medios_comunicacion,
            self.tipos_modulos,
            self.frecuencias_publicacion
        )

    def _cargar_anuncios(self) -> None:
        """
        Carga todos los anuncios activos desde la base de datos
        """
        self.anuncios = AnuncioService.obtener_todos_los_anuncios()

    def ejecutar(self) -> None:
        """
        Ejecuta el bucle principal del programa
        """
        if not self.inicializar_sistema():
            return
        
        try:
            while True:
                self.ui.mostrar_menu()
                opcion = self.ui.obtener_opcion()
                
                if opcion == 0:
                    self.ui.mostrar_mensaje_info("Saliendo del sistema...")
                    break
                
                self._procesar_opcion(opcion)
                self.ui.pausa()
                
        except KeyboardInterrupt:
            self.ui.mostrar_mensaje_info("Programa interrumpido por el usuario")
        except Exception as e:
            self.logger.error(f"Error inesperado: {e}")
            self.ui.mostrar_mensaje_error(f"Error inesperado: {e}")
        finally:
            desconectar()
            self.ui.mostrar_mensaje_info("Desconectado de la base de datos")

    def _procesar_opcion(self, opcion: int) -> None:
        """
        Procesa la opción seleccionada por el usuario
        
        Args:
            opcion: Opción seleccionada
        """
        opciones = {
            1: self._mostrar_precios,
            2: self._agregar_anuncio,
            3: self._eliminar_anuncio,
            4: self._mostrar_anuncios,
            5: self._buscar_anuncio_por_empresa,
            6: self._modificar_anuncio,
            7: self._calcular_ingresos_totales,
            8: self._recargar_datos
        }
        
        accion = opciones.get(opcion)
        if accion:
            try:
                accion()
            except Exception as e:
                self.logger.error(f"Error en opción {opcion}: {e}")
                self.ui.mostrar_mensaje_error(f"Error al procesar la acción: {e}")
        else:
            self.ui.mostrar_mensaje_error("Opción no válida")

    def _mostrar_precios(self) -> None:
        """
        Muestra la matriz de precios
        """
        self.ui.mostrar_precios(self.tipos_modulos, self.frecuencias_publicacion)

    def _agregar_anuncio(self) -> None:
        """
        Procesa la creación de un nuevo anuncio
        """
        # Seleccionar medio
        medio = self.ui.seleccionar_medio(self.medios_comunicacion)
        if not medio:
            self.ui.mostrar_mensaje_info("Operación cancelada")
            return
        
        # Seleccionar módulo
        modulo = self.ui.seleccionar_modulo(self.tipos_modulos)
        if not modulo:
            self.ui.mostrar_mensaje_info("Operación cancelada")
            return
        
        # Seleccionar frecuencia
        frecuencia = self.ui.seleccionar_frecuencia(self.frecuencias_publicacion)
        if not frecuencia:
            self.ui.mostrar_mensaje_info("Operación cancelada")
            return
        
        # Obtener nombre de empresa
        nombre_empresa = self.ui.obtener_nombre_empresa()
        if not nombre_empresa:
            self.ui.mostrar_mensaje_info("Operación cancelada")
            return
        
        # Calcular precio
        modulo_index = self.tipos_modulos.index(modulo)
        frecuencia_index = self.frecuencias_publicacion.index(frecuencia)
        precio = self.ui.calcular_precio(modulo_index, frecuencia_index)
        
        try:
            # Crear anuncio
            nuevo_anuncio = AnuncioService.crear_anuncio(
                medio, modulo, frecuencia, precio, nombre_empresa
            )
            
            if nuevo_anuncio:
                self._cargar_anuncios()  # Recargar lista
                self.ui.mostrar_mensaje_exito(
                    f"Anuncio creado: {nombre_empresa} - ${precio:,.2f}"
                )
            else:
                self.ui.mostrar_mensaje_error("No se pudo crear el anuncio")
                
        except Exception as e:
            self.logger.error(f"Error al crear anuncio: {e}")
            self.ui.mostrar_mensaje_error(f"Error al crear anuncio: {e}")

    def _eliminar_anuncio(self) -> None:
        """
        Procesa la eliminación de un anuncio
        """
        anuncio_index = self.ui.seleccionar_anuncio(self.anuncios, "eliminar")
        if anuncio_index is None:
            return
        
        anuncio = self.anuncios[anuncio_index]
        
        # Confirmar eliminación
        if not self.ui.confirmar_accion(
            f"¿Está seguro de eliminar el anuncio de '{anuncio.get_empresa()}'?"
        ):
            self.ui.mostrar_mensaje_info("Eliminación cancelada")
            return
        
        try:
            if AnuncioService.eliminar_anuncio(str(anuncio.id)):
                self._cargar_anuncios()  # Recargar lista
                self.ui.mostrar_mensaje_exito("Anuncio eliminado exitosamente")
            else:
                self.ui.mostrar_mensaje_error("No se pudo eliminar el anuncio")
                
        except Exception as e:
            self.logger.error(f"Error al eliminar anuncio: {e}")
            self.ui.mostrar_mensaje_error(f"Error al eliminar anuncio: {e}")

    def _mostrar_anuncios(self) -> None:
        """
        Muestra todos los anuncios activos
        """
        self.ui.mostrar_anuncios(self.anuncios)
        
        # Mostrar estadísticas adicionales
        if self.anuncios:
            total_ingresos = sum(anuncio.get_precio() for anuncio in self.anuncios)
            self.ui.mostrar_estadisticas(len(self.anuncios), total_ingresos)

    def _buscar_anuncio_por_empresa(self) -> None:
        """
        Busca anuncios por nombre de empresa
        """
        nombre_empresa = self.ui.obtener_busqueda_empresa()
        if not nombre_empresa:
            self.ui.mostrar_mensaje_info("Búsqueda cancelada")
            return
        
        try:
            anuncios_encontrados = AnuncioService.buscar_anuncios_por_empresa(nombre_empresa)
            
            if anuncios_encontrados:
                print(f"\n✅ Se encontraron {len(anuncios_encontrados)} anuncio(s) para '{nombre_empresa}':")
                self.ui.mostrar_anuncios(anuncios_encontrados)
                
                # Mostrar total de ingresos de esta empresa
                total_empresa = sum(anuncio.get_precio() for anuncio in anuncios_encontrados)
                print(f"\n💰 Ingresos totales de {nombre_empresa}: ${total_empresa:,.2f}")
            else:
                self.ui.mostrar_mensaje_info(f"No se encontraron anuncios para '{nombre_empresa}'")
                
        except Exception as e:
            self.logger.error(f"Error en búsqueda: {e}")
            self.ui.mostrar_mensaje_error(f"Error en la búsqueda: {e}")

    def _modificar_anuncio(self) -> None:
        """
        Procesa la modificación de un anuncio
        """
        anuncio_index = self.ui.seleccionar_anuncio(self.anuncios, "modificar")
        if anuncio_index is None:
            return
        
        anuncio = self.anuncios[anuncio_index]
        
        print(f"\n✏️  MODIFICANDO ANUNCIO: {anuncio.get_empresa()}")
        print(f"Configuración actual: {anuncio.get_medio().get_nombre()} - "
              f"{anuncio.get_modulo().get_nombre()} - {anuncio.get_frecuencia().get_nombre()} - "
              f"${anuncio.get_precio():,.2f}")
        
        # Obtener nuevo nombre de empresa
        print(f"\nEmpresa actual: {anuncio.get_empresa()}")
        nuevo_nombre = self.ui.obtener_nombre_empresa()
        if nuevo_nombre:
            anuncio.set_empresa(nuevo_nombre)
        
        # Seleccionar nuevo medio (opcional)
        print(f"\nMedio actual: {anuncio.get_medio().get_nombre()}")
        if self.ui.confirmar_accion("¿Desea cambiar el medio de comunicación?"):
            nuevo_medio = self.ui.seleccionar_medio(self.medios_comunicacion)
            if nuevo_medio:
                anuncio.set_medio(nuevo_medio)
        
        # Seleccionar nuevo módulo (opcional)
        print(f"\nMódulo actual: {anuncio.get_modulo().get_nombre()}")
        if self.ui.confirmar_accion("¿Desea cambiar el tipo de módulo?"):
            nuevo_modulo = self.ui.seleccionar_modulo(self.tipos_modulos)
            if nuevo_modulo:
                anuncio.set_modulo(nuevo_modulo)
        
        # Seleccionar nueva frecuencia (opcional)
        print(f"\nFrecuencia actual: {anuncio.get_frecuencia().get_nombre()}")
        if self.ui.confirmar_accion("¿Desea cambiar la frecuencia de publicación?"):
            nueva_frecuencia = self.ui.seleccionar_frecuencia(self.frecuencias_publicacion)
            if nueva_frecuencia:
                anuncio.set_frecuencia(nueva_frecuencia)
        
        # Recalcular precio
        try:
            modulo_index = self.tipos_modulos.index(anuncio.get_modulo())
            frecuencia_index = self.frecuencias_publicacion.index(anuncio.get_frecuencia())
            nuevo_precio = self.ui.calcular_precio(modulo_index, frecuencia_index)
            anuncio.set_precio(nuevo_precio)
            
            # Actualizar en la base de datos
            AnuncioService.actualizar_anuncio(anuncio)
            self._cargar_anuncios()  # Recargar lista
            
            self.ui.mostrar_mensaje_exito(
                f"Anuncio actualizado: {anuncio.get_empresa()} - ${nuevo_precio:,.2f}"
            )
            
        except Exception as e:
            self.logger.error(f"Error al modificar anuncio: {e}")
            self.ui.mostrar_mensaje_error(f"Error al modificar anuncio: {e}")

    def _calcular_ingresos_totales(self) -> None:
        """
        Calcula y muestra los ingresos totales del sistema
        """
        try:
            total_ingresos = AnuncioService.calcular_ingresos_totales()
            total_anuncios = len(self.anuncios)
            
            self.ui.mostrar_estadisticas(total_anuncios, total_ingresos)
            
            # Mostrar distribución por medio
            if self.anuncios:
                print(f"\n📊 DISTRIBUCIÓN POR MEDIO:")
                medios_stats = {}
                for anuncio in self.anuncios:
                    medio = anuncio.get_medio().get_nombre()
                    if medio not in medios_stats:
                        medios_stats[medio] = {'cantidad': 0, 'ingresos': 0}
                    medios_stats[medio]['cantidad'] += 1
                    medios_stats[medio]['ingresos'] += anuncio.get_precio()
                
                for medio, stats in medios_stats.items():
                    print(f"  {medio}: {stats['cantidad']} anuncios - ${stats['ingresos']:,.2f}")
            
        except Exception as e:
            self.logger.error(f"Error al calcular ingresos: {e}")
            self.ui.mostrar_mensaje_error(f"Error al calcular ingresos: {e}")

    def _recargar_datos(self) -> None:
        """
        Recarga todos los datos desde la base de datos
        """
        try:
            self.ui.mostrar_mensaje_info("Recargando datos desde MongoDB...")
            
            self.medios_comunicacion = DatosBasicosService.obtener_todos_los_medios()
            self.tipos_modulos = DatosBasicosService.obtener_todos_los_modulos()
            self.frecuencias_publicacion = DatosBasicosService.obtener_todas_las_frecuencias()
            self._cargar_anuncios()
            
            self.ui.mostrar_mensaje_exito("Datos recargados exitosamente")
            
        except Exception as e:
            self.logger.error(f"Error al recargar datos: {e}")
            self.ui.mostrar_mensaje_error(f"Error al recargar datos: {e}")
