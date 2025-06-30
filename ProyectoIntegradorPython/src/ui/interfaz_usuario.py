"""
Interfaz de usuario para el sistema de gestión de anuncios publicitarios
"""
from typing import List, Optional
from src.models.anuncio import Anuncio
from src.models.medio_comunicacion import MedioComunicacion
from src.models.tipo_modulo import TipoModulo
from src.models.frecuencia_publicacion import FrecuenciaPublicacion


class InterfazUsuario:
    """
    Maneja toda la interacción con el usuario
    """
    
    def __init__(self):
        self.PRECIOS = [
            [1000.0, 800.0, 500.0, 200.0, 350.0, 500.0, 150.0, 100.0],
            [1800.0, 1500.0, 900.0, 350.0, 650.0, 900.0, 250.0, 180.0],
            [2100.0, 2100.0, 1300.0, 500.0, 950.0, 1300.0, 350.0, 250.0],
            [3000.0, 2500.0, 1500.0, 600.0, 1100.0, 1500.0, 400.0, 300.0],
            [4500.0, 3800.0, 2300.0, 900.0, 1700.0, 2300.0, 600.0, 450.0],
            [6000.0, 5000.0, 3000.0, 1200.0, 2200.0, 3000.0, 800.0, 600.0],
            [8500.0, 7100.0, 4300.0, 1700.0, 3200.0, 4300.0, 1100.0, 800.0],
            [11000.0, 9200.0, 5500.0, 2200.0, 4200.0, 5500.0, 1400.0, 1000.0]
        ]

    def mostrar_menu(self) -> None:
        """
        Muestra el menú principal del programa
        """
        print("\n" + "="*50)
        print("🏢 SISTEMA DE GESTIÓN DE ANUNCIOS PUBLICITARIOS")
        print("="*50)
        print("1. 📊 Mostrar precios")
        print("2. ➕ Agregar anuncio")
        print("3. ❌ Eliminar anuncio")
        print("4. 📋 Mostrar anuncios")
        print("5. 🔍 Buscar anuncio por empresa")
        print("6. ✏️  Modificar anuncio")
        print("7. 💰 Calcular ingresos totales")
        print("8. 🔄 Recargar datos desde BD")
        print("0. 🚪 Salir")
        print("="*50)

    def obtener_opcion(self) -> int:
        """
        Obtiene una opción numérica del usuario con validación
        
        Returns:
            int: La opción seleccionada por el usuario
        """
        while True:
            try:
                opcion = int(input("Ingrese su opción: "))
                if opcion < 0 or opcion > 8:
                    print("❌ Opción inválida. Seleccione entre 0 y 8.")
                    continue
                return opcion
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")
            except KeyboardInterrupt:
                print("\n🛑 Programa interrumpido por el usuario")
                return 0

    def mostrar_precios(self, tipos_modulos: List[TipoModulo], 
                       frecuencias_publicacion: List[FrecuenciaPublicacion]) -> None:
        """
        Muestra la matriz de precios
        
        Args:
            tipos_modulos: Lista de tipos de módulos
            frecuencias_publicacion: Lista de frecuencias de publicación
        """
        print("\n📊 PRECIOS DE ESPACIOS PUBLICITARIOS")
        print("-" * 60)
        
        # Encabezado
        print(f"{'Módulo':<8}", end="")
        for freq in frecuencias_publicacion:
            print(f"{freq.get_nombre():<10}", end="")
        print()
        print("-" * 60)
        
        # Filas de precios
        for i, modulo in enumerate(tipos_modulos):
            print(f"{modulo.get_nombre():<8}", end="")
            for j in range(len(frecuencias_publicacion)):
                precio = self.PRECIOS[i][j]
                print(f"${precio:<9.0f}", end="")
            print()

    def seleccionar_medio(self, medios: List[MedioComunicacion]) -> Optional[MedioComunicacion]:
        """
        Permite al usuario seleccionar un medio de comunicación
        
        Args:
            medios: Lista de medios disponibles
            
        Returns:
            MedioComunicacion seleccionado o None si se cancela
        """
        print("\n📺 Seleccione el medio de comunicación:")
        for i, medio in enumerate(medios):
            print(f"{i + 1}. {medio.get_nombre()}")
        
        while True:
            try:
                seleccion = input("Ingrese su selección (0 para cancelar): ").strip()
                if seleccion == "0":
                    return None
                    
                medio_index = int(seleccion) - 1
                if 0 <= medio_index < len(medios):
                    return medios[medio_index]
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def seleccionar_modulo(self, modulos: List[TipoModulo]) -> Optional[TipoModulo]:
        """
        Permite al usuario seleccionar un tipo de módulo
        
        Args:
            modulos: Lista de módulos disponibles
            
        Returns:
            TipoModulo seleccionado o None si se cancela
        """
        print("\n📐 Seleccione el tipo de módulo:")
        for i, modulo in enumerate(modulos):
            print(f"{i + 1}. {modulo.get_nombre()}")
        
        while True:
            try:
                seleccion = input("Ingrese su selección (0 para cancelar): ").strip()
                if seleccion == "0":
                    return None
                    
                modulo_index = int(seleccion) - 1
                if 0 <= modulo_index < len(modulos):
                    return modulos[modulo_index]
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def seleccionar_frecuencia(self, frecuencias: List[FrecuenciaPublicacion]) -> Optional[FrecuenciaPublicacion]:
        """
        Permite al usuario seleccionar una frecuencia de publicación
        
        Args:
            frecuencias: Lista de frecuencias disponibles
            
        Returns:
            FrecuenciaPublicacion seleccionada o None si se cancela
        """
        print("\n⏰ Seleccione la frecuencia de publicación:")
        for i, frecuencia in enumerate(frecuencias):
            desc = frecuencia.get_descripcion() if hasattr(frecuencia, 'get_descripcion') else ""
            print(f"{i + 1}. {frecuencia.get_nombre()} {desc}")
        
        while True:
            try:
                seleccion = input("Ingrese su selección (0 para cancelar): ").strip()
                if seleccion == "0":
                    return None
                    
                frecuencia_index = int(seleccion) - 1
                if 0 <= frecuencia_index < len(frecuencias):
                    return frecuencias[frecuencia_index]
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def obtener_nombre_empresa(self) -> Optional[str]:
        """
        Obtiene el nombre de la empresa con validación
        
        Returns:
            str: Nombre de la empresa o None si se cancela
        """
        while True:
            nombre = input("\n🏢 Ingrese el nombre de la empresa (Enter para cancelar): ").strip()
            if not nombre:
                return None
            if len(nombre) < 2:
                print("❌ El nombre debe tener al menos 2 caracteres.")
                continue
            if len(nombre) > 100:
                print("❌ El nombre no puede tener más de 100 caracteres.")
                continue
            return nombre

    def mostrar_anuncios(self, anuncios: List[Anuncio]) -> None:
        """
        Muestra la lista de anuncios de forma organizada
        
        Args:
            anuncios: Lista de anuncios a mostrar
        """
        if not anuncios:
            print("📋 No hay anuncios registrados.")
            return
            
        print("\n📋 LISTA DE ANUNCIOS")
        print("-" * 90)
        print(f"{'#':<4} {'Empresa':<25} {'Medio':<15} {'Módulo':<8} {'Frecuencia':<12} {'Precio':<12}")
        print("-" * 90)
        
        for i, anuncio in enumerate(anuncios):
            print(f"{i + 1:<4} {anuncio.get_empresa():<25} "
                  f"{anuncio.get_medio().get_nombre():<15} "
                  f"{anuncio.get_modulo().get_nombre():<8} "
                  f"{anuncio.get_frecuencia().get_nombre():<12} "
                  f"${anuncio.get_precio():>9,.2f}")

    def seleccionar_anuncio(self, anuncios: List[Anuncio], accion: str) -> Optional[int]:
        """
        Permite al usuario seleccionar un anuncio de la lista
        
        Args:
            anuncios: Lista de anuncios disponibles
            accion: Descripción de la acción a realizar
            
        Returns:
            int: Índice del anuncio seleccionado o None si se cancela
        """
        if not anuncios:
            print(f"❌ No hay anuncios para {accion}.")
            return None
            
        print(f"\n{accion.upper()}")
        print("-" * 30)
        self.mostrar_anuncios(anuncios)
        
        while True:
            try:
                seleccion = input(f"\nIngrese el número del anuncio para {accion} (0 para cancelar): ").strip()
                if seleccion == "0":
                    return None
                    
                anuncio_index = int(seleccion) - 1
                if 0 <= anuncio_index < len(anuncios):
                    return anuncio_index
                else:
                    print("❌ Número de anuncio inválido.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def confirmar_accion(self, mensaje: str) -> bool:
        """
        Solicita confirmación del usuario para una acción
        
        Args:
            mensaje: Mensaje de confirmación
            
        Returns:
            bool: True si confirma, False si no
        """
        while True:
            respuesta = input(f"{mensaje} (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print("❌ Respuesta inválida. Ingrese 's' para sí o 'n' para no.")

    def obtener_busqueda_empresa(self) -> Optional[str]:
        """
        Obtiene el nombre de empresa para búsqueda
        
        Returns:
            str: Nombre de empresa o None si se cancela
        """
        nombre = input("\n🔍 Ingrese el nombre de la empresa a buscar (Enter para cancelar): ").strip()
        return nombre if nombre else None

    def mostrar_mensaje_exito(self, mensaje: str) -> None:
        """
        Muestra un mensaje de éxito
        
        Args:
            mensaje: Mensaje a mostrar
        """
        print(f"✅ {mensaje}")

    def mostrar_mensaje_error(self, mensaje: str) -> None:
        """
        Muestra un mensaje de error
        
        Args:
            mensaje: Mensaje a mostrar
        """
        print(f"❌ {mensaje}")

    def mostrar_mensaje_info(self, mensaje: str) -> None:
        """
        Muestra un mensaje informativo
        
        Args:
            mensaje: Mensaje a mostrar
        """
        print(f"ℹ️  {mensaje}")

    def pausa(self) -> None:
        """
        Pausa el programa esperando entrada del usuario
        """
        input("\n⏸️  Presione Enter para continuar...")

    def calcular_precio(self, modulo_index: int, frecuencia_index: int) -> float:
        """
        Calcula el precio según el módulo y frecuencia
        
        Args:
            modulo_index: Índice del módulo
            frecuencia_index: Índice de la frecuencia
            
        Returns:
            float: Precio calculado
        """
        if (0 <= modulo_index < len(self.PRECIOS) and 
            0 <= frecuencia_index < len(self.PRECIOS[0])):
            return self.PRECIOS[modulo_index][frecuencia_index]
        return 0.0

    def mostrar_estadisticas(self, total_anuncios: int, ingresos_totales: float) -> None:
        """
        Muestra estadísticas del sistema
        
        Args:
            total_anuncios: Número total de anuncios
            ingresos_totales: Total de ingresos
        """
        print(f"\n💰 ESTADÍSTICAS DEL SISTEMA")
        print("-" * 30)
        print(f"📊 Total de anuncios activos: {total_anuncios}")
        print(f"💵 Ingresos totales: ${ingresos_totales:,.2f}")
        if total_anuncios > 0:
            promedio = ingresos_totales / total_anuncios
            print(f"📈 Ingreso promedio por anuncio: ${promedio:,.2f}")
