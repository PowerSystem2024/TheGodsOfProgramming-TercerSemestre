"""
Proyecto Integrador - Sistema de Gestión de Anuncios Publicitarios
Adaptación a Python del proyecto original en Java con persistencia en MongoDB
"""

from db.conexion import conectar, desconectar
from services.datos_basicos_service import DatosBasicosService
from services.anuncio_service import AnuncioService
from models.anuncio import Anuncio

class ProyectoIntegrador:
    def __init__(self):
        # Listas para trabajar en memoria (cargadas desde MongoDB)
        self.medios_comunicacion = []
        self.tipos_modulos = []
        self.frecuencias_publicacion = []
        self.anuncios = []
        
        # Matriz de precios según módulo y frecuencia
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

    def inicializar_datos(self):
        """
        Inicializa los datos del programa cargándolos desde MongoDB.
        Si no existen, los crea.
        """
        print("🔄 Inicializando datos desde MongoDB...")
        
        # Inicializar datos básicos en MongoDB
        self.medios_comunicacion = DatosBasicosService.inicializar_medios_comunicacion()
        self.tipos_modulos = DatosBasicosService.inicializar_tipos_modulos()
        self.frecuencias_publicacion = DatosBasicosService.inicializar_frecuencias_publicacion()
        
        # Inicializar anuncios de prueba si no existen
        AnuncioService.inicializar_anuncios_prueba(
            self.medios_comunicacion, 
            self.tipos_modulos, 
            self.frecuencias_publicacion
        )
        
        # Cargar anuncios activos
        self.cargar_anuncios_desde_db()
        
        print(f"✅ Datos inicializados: {len(self.medios_comunicacion)} medios, "
              f"{len(self.tipos_modulos)} módulos, {len(self.frecuencias_publicacion)} frecuencias, "
              f"{len(self.anuncios)} anuncios")

    def cargar_anuncios_desde_db(self):
        """
        Carga todos los anuncios activos desde la base de datos
        """
        self.anuncios = AnuncioService.obtener_todos_los_anuncios()

    def mostrar_menu(self):
        """
        Muestra el menú principal del programa.
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

    def obtener_opcion(self):
        """
        Obtiene una opción numérica del usuario.
        Valida que la entrada sea un número entero.
        
        Returns:
            int: La opción seleccionada por el usuario.
        """
        while True:
            try:
                opcion = int(input("Ingrese su opción: "))
                return opcion
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def get_precio(self, modulo, frecuencia):
        """
        Obtiene el precio de un espacio publicitario según el módulo y la frecuencia.
        
        Args:
            modulo (int): Índice del módulo
            frecuencia (int): Índice de la frecuencia
            
        Returns:
            float: El precio del espacio publicitario
        """
        return self.PRECIOS[modulo][frecuencia]

    def mostrar_precios(self):
        """
        Muestra los precios de los espacios publicitarios.
        """
        print("\n📊 PRECIOS DE ESPACIOS PUBLICITARIOS")
        print("-" * 50)
        for i in range(len(self.tipos_modulos)):
            for j in range(len(self.frecuencias_publicacion)):
                precio = self.get_precio(i, j)
                print(f"{self.tipos_modulos[i].get_nombre()} - {self.frecuencias_publicacion[j].get_nombre()}: ${precio:,.2f}")

    def agregar_anuncio(self):
        """
        Agrega un nuevo anuncio al sistema y lo guarda en MongoDB.
        """
        print("\n➕ AGREGAR NUEVO ANUNCIO")
        print("-" * 30)
        
        print("Seleccione el medio de comunicación:")
        for i, medio in enumerate(self.medios_comunicacion):
            print(f"{i + 1}. {medio.get_nombre()}")
        
        while True:
            try:
                medio_index = int(input("Ingrese su selección: ")) - 1
                if 0 <= medio_index < len(self.medios_comunicacion):
                    medio_seleccionado = self.medios_comunicacion[medio_index]
                    break
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

        print("\nSeleccione el tipo de módulo:")
        for i, modulo in enumerate(self.tipos_modulos):
            print(f"{i + 1}. {modulo.get_nombre()}")
        
        while True:
            try:
                tipo_modulo_index = int(input("Ingrese su selección: ")) - 1
                if 0 <= tipo_modulo_index < len(self.tipos_modulos):
                    tipo_modulo_seleccionado = self.tipos_modulos[tipo_modulo_index]
                    break
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

        print("\nSeleccione la frecuencia de publicación:")
        for i, frecuencia in enumerate(self.frecuencias_publicacion):
            print(f"{i + 1}. {frecuencia.get_nombre()}")
        
        while True:
            try:
                frecuencia_index = int(input("Ingrese su selección: ")) - 1
                if 0 <= frecuencia_index < len(self.frecuencias_publicacion):
                    frecuencia_seleccionada = self.frecuencias_publicacion[frecuencia_index]
                    break
                else:
                    print("❌ Selección inválida. Intente nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

        nombre_empresa = input("\nIngresar nombre empresa: ").strip()
        if not nombre_empresa:
            print("❌ El nombre de la empresa no puede estar vacío.")
            return
        
        # Calcular precio total
        precio = self.get_precio(tipo_modulo_index, frecuencia_index)
        
        try:
            # Crear el anuncio en MongoDB
            nuevo_anuncio = AnuncioService.crear_anuncio(
                medio_seleccionado, 
                tipo_modulo_seleccionado, 
                frecuencia_seleccionada, 
                precio, 
                nombre_empresa
            )
            
            # Recargar anuncios desde la BD
            self.cargar_anuncios_desde_db()
            
            print(f"✅ Anuncio agregado exitosamente: {nombre_empresa} - ${precio:,.2f}")
            
        except Exception as e:
            print(f"❌ Error al crear el anuncio: {e}")

    def eliminar_anuncio(self):
        """
        Elimina un anuncio del sistema.
        """
        if not self.anuncios:
            print("❌ No hay anuncios para eliminar.")
            return
            
        print("\n❌ ELIMINAR ANUNCIO")
        print("-" * 20)
        self.mostrar_anuncios()
        
        while True:
            try:
                anuncio_index = int(input("\nIngrese el número del anuncio a eliminar: ")) - 1
                if 0 <= anuncio_index < len(self.anuncios):
                    anuncio_seleccionado = self.anuncios[anuncio_index]
                    
                    # Confirmar eliminación
                    confirmacion = input(f"¿Está seguro de eliminar el anuncio de '{anuncio_seleccionado.get_empresa()}'? (s/n): ")
                    if confirmacion.lower() == 's':
                        # Eliminar de MongoDB
                        if AnuncioService.eliminar_anuncio(str(anuncio_seleccionado.id)):
                            # Recargar anuncios desde la BD
                            self.cargar_anuncios_desde_db()
                            print("✅ Anuncio eliminado exitosamente.")
                        else:
                            print("❌ Error al eliminar el anuncio.")
                    else:
                        print("🚫 Eliminación cancelada.")
                    break
                else:
                    print("❌ Número de anuncio inválido.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")

    def mostrar_anuncios(self):
        """
        Muestra la lista de anuncios creados.
        """
        if not self.anuncios:
            print("📋 No hay anuncios registrados.")
            return
            
        print("\n📋 LISTA DE ANUNCIOS")
        print("-" * 80)
        for i, anuncio in enumerate(self.anuncios):
            print(f"{i + 1:2}. {anuncio.get_empresa():<25} | "
                  f"{anuncio.get_medio().get_nombre():<15} | "
                  f"{anuncio.get_modulo().get_nombre():<4} | "
                  f"{anuncio.get_frecuencia().get_nombre():<4} | "
                  f"${anuncio.get_precio():>8,.2f}")

    def calcular_ingresos_totales(self):
        """
        Calcula los ingresos totales directamente desde MongoDB.
        
        Returns:
            float: El total de ingresos de todos los anuncios.
        """
        return AnuncioService.calcular_ingresos_totales()

    def buscar_anuncio_por_empresa(self):
        """
        Busca anuncios por el nombre de la empresa usando MongoDB.
        """
        nombre_empresa = input("\n🔍 Ingrese el nombre de la empresa a buscar: ").strip()
        if not nombre_empresa:
            print("❌ El nombre de la empresa no puede estar vacío.")
            return
        
        # Buscar en MongoDB
        anuncios_encontrados = AnuncioService.buscar_anuncios_por_empresa(nombre_empresa)
        
        if anuncios_encontrados:
            print(f"\n✅ Se encontraron {len(anuncios_encontrados)} anuncio(s) para '{nombre_empresa}':")
            print("-" * 80)
            for i, anuncio in enumerate(anuncios_encontrados):
                print(f"{i + 1}. {anuncio.get_empresa():<25} | "
                      f"{anuncio.get_medio().get_nombre():<15} | "
                      f"{anuncio.get_modulo().get_nombre():<4} | "
                      f"{anuncio.get_frecuencia().get_nombre():<4} | "
                      f"${anuncio.get_precio():>8,.2f}")
        else:
            print(f"❌ No se encontraron anuncios para la empresa: {nombre_empresa}")

    def modificar_anuncio(self):
        """
        Modifica un anuncio existente.
        """
        if not self.anuncios:
            print("❌ No hay anuncios para modificar.")
            return
            
        print("\n✏️  MODIFICAR ANUNCIO")
        print("-" * 20)
        self.mostrar_anuncios()
        
        while True:
            try:
                anuncio_index = int(input("\nIngrese el número del anuncio a modificar: ")) - 1
                if 0 <= anuncio_index < len(self.anuncios):
                    break
                else:
                    print("❌ Número inválido o anuncio no encontrado.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")
        
        anuncio = self.anuncios[anuncio_index]
        
        # Modificar nombre de empresa
        print(f"\nEmpresa actual: {anuncio.get_empresa()}")
        nuevo_nombre_empresa = input("Nuevo nombre de empresa (Enter para mantener): ").strip()
        if nuevo_nombre_empresa:
            anuncio.set_empresa(nuevo_nombre_empresa)
        
        # Modificar medio de comunicación
        print(f"\nMedio actual: {anuncio.get_medio().get_nombre()}")
        print("Seleccione el nuevo medio de comunicación (0 para mantener):")
        for i, medio in enumerate(self.medios_comunicacion):
            print(f"{i + 1}. {medio.get_nombre()}")
        
        try:
            medio_opcion = int(input("Ingrese su selección: "))
            if 1 <= medio_opcion <= len(self.medios_comunicacion):
                anuncio.set_medio(self.medios_comunicacion[medio_opcion - 1])
        except ValueError:
            pass
        
        # Modificar tipo de módulo
        print(f"\nMódulo actual: {anuncio.get_modulo().get_nombre()}")
        print("Seleccione el nuevo tipo de módulo (0 para mantener):")
        for i, modulo in enumerate(self.tipos_modulos):
            print(f"{i + 1}. {modulo.get_nombre()}")
        
        modulo_opcion = 0
        try:
            modulo_opcion = int(input("Ingrese su selección: "))
            if 1 <= modulo_opcion <= len(self.tipos_modulos):
                anuncio.set_modulo(self.tipos_modulos[modulo_opcion - 1])
        except ValueError:
            pass
        
        # Modificar frecuencia de publicación
        print(f"\nFrecuencia actual: {anuncio.get_frecuencia().get_nombre()}")
        print("Seleccione la nueva frecuencia de publicación (0 para mantener):")
        for i, frecuencia in enumerate(self.frecuencias_publicacion):
            print(f"{i + 1}. {frecuencia.get_nombre()}")
        
        frecuencia_opcion = 0
        try:
            frecuencia_opcion = int(input("Ingrese su selección: "))
            if 1 <= frecuencia_opcion <= len(self.frecuencias_publicacion):
                anuncio.set_frecuencia(self.frecuencias_publicacion[frecuencia_opcion - 1])
        except ValueError:
            pass
        
        # Actualizar precio si se cambió el módulo o frecuencia
        modulo_index = modulo_opcion - 1 if modulo_opcion != 0 else self.tipos_modulos.index(anuncio.get_modulo())
        frecuencia_index = frecuencia_opcion - 1 if frecuencia_opcion != 0 else self.frecuencias_publicacion.index(anuncio.get_frecuencia())
        nuevo_precio = self.get_precio(modulo_index, frecuencia_index)
        anuncio.set_precio(nuevo_precio)
        
        try:
            # Actualizar en MongoDB
            AnuncioService.actualizar_anuncio(anuncio)
            
            # Recargar anuncios desde la BD
            self.cargar_anuncios_desde_db()
            
            print("✅ Anuncio modificado exitosamente.")
            
        except Exception as e:
            print(f"❌ Error al actualizar el anuncio: {e}")

    def mostrar_ingresos_totales(self):
        """
        Muestra el total de ingresos de los anuncios cargados.
        """
        total = self.calcular_ingresos_totales()
        print(f"\n💰 INGRESOS TOTALES")
        print("-" * 30)
        print(f"Total de ingresos: ${total:,.2f}")
        print(f"Número de anuncios activos: {len(self.anuncios)}")

    def recargar_datos(self):
        """
        Recarga todos los datos desde MongoDB
        """
        print("\n🔄 Recargando datos desde MongoDB...")
        self.medios_comunicacion = DatosBasicosService.obtener_todos_los_medios()
        self.tipos_modulos = DatosBasicosService.obtener_todos_los_modulos()
        self.frecuencias_publicacion = DatosBasicosService.obtener_todas_las_frecuencias()
        self.cargar_anuncios_desde_db()
        print("✅ Datos recargados exitosamente.")

    def ejecutar(self):
        """
        Método principal del programa.
        Ejecuta el bucle principal del menú.
        """
        # Conectar a MongoDB
        if not conectar():
            print("❌ No se pudo conectar a MongoDB. Saliendo...")
            return
        
        try:
            self.inicializar_datos()
            
            while True:
                self.mostrar_menu()
                opcion = self.obtener_opcion()
                
                if opcion == 1:
                    self.mostrar_precios()
                elif opcion == 2:
                    self.agregar_anuncio()
                elif opcion == 3:
                    self.eliminar_anuncio()
                elif opcion == 4:
                    self.mostrar_anuncios()
                elif opcion == 5:
                    self.buscar_anuncio_por_empresa()
                elif opcion == 6:
                    self.modificar_anuncio()
                elif opcion == 7:
                    self.mostrar_ingresos_totales()
                elif opcion == 8:
                    self.recargar_datos()
                elif opcion == 0:
                    print("🚪 Saliendo...")
                    break
                else:
                    print("❌ Opción incorrecta")
                
                input("\n⏸️  Presione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n🛑 Programa interrumpido por el usuario")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
        finally:
            # Desconectar de MongoDB
            desconectar()

def main():
    """
    Función principal que inicia el programa.
    """
    print("🚀 Iniciando Sistema de Gestión de Anuncios Publicitarios...")
    programa = ProyectoIntegrador()
    programa.ejecutar()

if __name__ == "__main__":
    main()