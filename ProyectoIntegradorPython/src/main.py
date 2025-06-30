"""
Proyecto Integrador - Sistema de Gestión de Anuncios Publicitarios
Adaptación a Python del proyecto original en Java
"""

from models.medio_comunicacion import MedioComunicacion
from models.tipo_modulo import TipoModulo
from models.frecuencia_publicacion import FrecuenciaPublicacion
from models.anuncio import Anuncio

class ProyectoIntegrador:
    def __init__(self):
        # Listas para almacenar los datos del sistema
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
        Inicializa los datos del programa (medios, módulos, frecuencias y anuncios de prueba).
        """
        # Inicializar medios de comunicación
        self.medios_comunicacion = [
            MedioComunicacion("El Norteño"),
            MedioComunicacion("Del Sur"),
            MedioComunicacion("Patagónico"),
            MedioComunicacion("Del Centro"),
            MedioComunicacion("El Cuyano"),
            MedioComunicacion("Del Litoral")
        ]

        # Inicializar tipos de módulos
        self.tipos_modulos = [
            TipoModulo("M1"),
            TipoModulo("M2"),
            TipoModulo("M3"),
            TipoModulo("M4"),
            TipoModulo("M6"),
            TipoModulo("M8"),
            TipoModulo("M12"),
            TipoModulo("M16")
        ]

        # Inicializar frecuencias de publicación
        self.frecuencias_publicacion = [
            FrecuenciaPublicacion("D"),
            FrecuenciaPublicacion("LAV"),
            FrecuenciaPublicacion("SD"),
            FrecuenciaPublicacion("1S"),
            FrecuenciaPublicacion("2S"),
            FrecuenciaPublicacion("3S"),
            FrecuenciaPublicacion("1.15"),
            FrecuenciaPublicacion("1.30")
        ]

        # Cargar anuncios de prueba
        self.anuncios = [
            Anuncio(self.medios_comunicacion[0], self.tipos_modulos[3], self.frecuencias_publicacion[1], 2500.0, "Tech Solutions Inc."),
            Anuncio(self.medios_comunicacion[1], self.tipos_modulos[1], self.frecuencias_publicacion[0], 1800.0, "Innovate Corp."),
            Anuncio(self.medios_comunicacion[2], self.tipos_modulos[5], self.frecuencias_publicacion[6], 4300.0, "Global Industries Ltd."),
            Anuncio(self.medios_comunicacion[3], self.tipos_modulos[0], self.frecuencias_publicacion[2], 500.0, "Creative Designs Studio"),
            Anuncio(self.medios_comunicacion[4], self.tipos_modulos[2], self.frecuencias_publicacion[4], 1300.0, "Marketing Masters"),
            Anuncio(self.medios_comunicacion[5], self.tipos_modulos[7], self.frecuencias_publicacion[7], 1000.0, "Digital Dynamics"),
            Anuncio(self.medios_comunicacion[0], self.tipos_modulos[4], self.frecuencias_publicacion[3], 200.0, "Code Wizards"),
            Anuncio(self.medios_comunicacion[1], self.tipos_modulos[6], self.frecuencias_publicacion[5], 900.0, "Future Vision"),
            Anuncio(self.medios_comunicacion[2], self.tipos_modulos[0], self.frecuencias_publicacion[0], 2100.0, "Open Source Solutions"),
            Anuncio(self.medios_comunicacion[3], self.tipos_modulos[2], self.frecuencias_publicacion[1], 2100.0, "Web Dev Experts"),
            Anuncio(self.medios_comunicacion[4], self.tipos_modulos[1], self.frecuencias_publicacion[4], 2100.0, "Marketing Masters")
        ]

    def mostrar_menu(self):
        """
        Muestra el menú principal del programa.
        """
        print("****************************************")
        print("********** Menú Principal **********")
        print("****************************************")
        print("1. Mostrar precios")
        print("2. Agregar anuncio")
        print("3. Eliminar anuncio")
        print("4. Mostrar anuncios")
        print("5. Buscar anuncio por empresa")
        print("6. Modificar anuncio")
        print("7. Calcular ingresos totales de los anuncios cargados")
        print("0. Salir")
        print("****************************************")

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
                print("Entrada inválida. Ingrese un número.")

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
        print("Precios de los espacios publicitarios:")
        for i in range(len(self.tipos_modulos)):
            for j in range(len(self.frecuencias_publicacion)):
                precio = self.get_precio(i, j)
                print(f"{self.tipos_modulos[i].get_nombre()} - {self.frecuencias_publicacion[j].get_nombre()}: ${precio}")

    def agregar_anuncio(self):
        """
        Agrega un nuevo anuncio al sistema.
        Solicita al usuario los datos del anuncio (medio, módulo, frecuencia, empresa).
        """
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
                    print("Selección inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

        print("Seleccione el tipo de módulo:")
        for i, modulo in enumerate(self.tipos_modulos):
            print(f"{i + 1}. {modulo.get_nombre()}")
        
        while True:
            try:
                tipo_modulo_index = int(input("Ingrese su selección: ")) - 1
                if 0 <= tipo_modulo_index < len(self.tipos_modulos):
                    tipo_modulo_seleccionado = self.tipos_modulos[tipo_modulo_index]
                    break
                else:
                    print("Selección inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

        print("Seleccione la frecuencia de publicación:")
        for i, frecuencia in enumerate(self.frecuencias_publicacion):
            print(f"{i + 1}. {frecuencia.get_nombre()}")
        
        while True:
            try:
                frecuencia_index = int(input("Ingrese su selección: ")) - 1
                if 0 <= frecuencia_index < len(self.frecuencias_publicacion):
                    frecuencia_seleccionada = self.frecuencias_publicacion[frecuencia_index]
                    break
                else:
                    print("Selección inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

        nombre_empresa = input("Ingresar nombre empresa: ")
        
        # Calcular precio total
        precio = self.get_precio(tipo_modulo_index, frecuencia_index)
        
        # Agregar el anuncio
        nuevo_anuncio = Anuncio(medio_seleccionado, tipo_modulo_seleccionado, frecuencia_seleccionada, precio, nombre_empresa)
        self.anuncios.append(nuevo_anuncio)
        
        print("Anuncio agregado exitosamente.")

    def eliminar_anuncio(self):
        """
        Elimina un anuncio del sistema.
        Solicita al usuario el ID del anuncio a eliminar.
        """
        if not self.anuncios:
            print("No hay anuncios para eliminar.")
            return
            
        self.mostrar_anuncios()
        
        while True:
            try:
                anuncio_id = int(input("Ingrese el ID del anuncio a eliminar: "))
                if 0 <= anuncio_id < len(self.anuncios):
                    self.anuncios.pop(anuncio_id)
                    print("Anuncio eliminado exitosamente.")
                    break
                else:
                    print("ID de anuncio inválido.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")

    def mostrar_anuncios(self):
        """
        Muestra la lista de anuncios creados.
        """
        if not self.anuncios:
            print("No hay anuncios registrados.")
            return
            
        print("Lista de anuncios:")
        for i, anuncio in enumerate(self.anuncios):
            print(f"ID: {i}, Medio: {anuncio.get_medio().get_nombre()}, "
                  f"Módulo: {anuncio.get_modulo().get_nombre()}, "
                  f"Frecuencia: {anuncio.get_frecuencia().get_nombre()}, "
                  f"Precio: ${anuncio.get_precio():.2f}, "
                  f"Nombre de la empresa: {anuncio.get_empresa()}")

    def calcular_ingresos_totales(self):
        """
        Calcula los ingresos totales de los anuncios cargados.
        
        Returns:
            float: El total de ingresos de todos los anuncios.
        """
        total_ingresos = sum(anuncio.get_precio() for anuncio in self.anuncios)
        return total_ingresos

    def buscar_anuncio_por_empresa(self):
        """
        Busca anuncios por el nombre de la empresa.
        """
        nombre_empresa = input("Ingrese el nombre de la empresa a buscar: ")
        encontrado = False
        
        for i, anuncio in enumerate(self.anuncios):
            if anuncio.get_empresa().lower() == nombre_empresa.lower():
                print(f"ID: {i}, Medio: {anuncio.get_medio().get_nombre()}, "
                      f"Módulo: {anuncio.get_modulo().get_nombre()}, "
                      f"Frecuencia: {anuncio.get_frecuencia().get_nombre()}, "
                      f"Precio: ${anuncio.get_precio():.2f}, "
                      f"Empresa: {anuncio.get_empresa()}")
                encontrado = True
        
        if not encontrado:
            print(f"No se encontraron anuncios para la empresa: {nombre_empresa}")

    def modificar_anuncio(self):
        """
        Modifica un anuncio existente.
        Solicita al usuario el ID del anuncio a modificar y los nuevos datos.
        """
        if not self.anuncios:
            print("No hay anuncios para modificar.")
            return
            
        self.mostrar_anuncios()
        
        while True:
            try:
                anuncio_id = int(input("Ingrese el ID del anuncio a modificar: "))
                if 0 <= anuncio_id < len(self.anuncios):
                    break
                else:
                    print("ID inválido o anuncio no encontrado.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
        
        anuncio = self.anuncios[anuncio_id]
        
        # Modificar nombre de empresa
        nuevo_nombre_empresa = input("Ingrese el nuevo nombre de la empresa (o presione Enter para dejar igual): ")
        if nuevo_nombre_empresa.strip():
            anuncio.set_empresa(nuevo_nombre_empresa)
        
        # Modificar medio de comunicación
        print("Seleccione el nuevo medio de comunicación (o 0 para dejar igual):")
        for i, medio in enumerate(self.medios_comunicacion):
            print(f"{i + 1}. {medio.get_nombre()}")
        
        try:
            medio_opcion = int(input("Ingrese su selección: "))
            if 1 <= medio_opcion <= len(self.medios_comunicacion):
                anuncio.set_medio(self.medios_comunicacion[medio_opcion - 1])
        except ValueError:
            pass
        
        # Modificar tipo de módulo
        print("Seleccione el nuevo tipo de módulo (o 0 para dejar igual):")
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
        print("Seleccione la nueva frecuencia de publicación (o 0 para dejar igual):")
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
        
        print("Anuncio modificado exitosamente.")

    def mostrar_ingresos_totales(self):
        """
        Muestra el total de ingresos de los anuncios cargados.
        """
        total = self.calcular_ingresos_totales()
        print(f"El ingreso total de todos los anuncios cargados en el sistema es: ${total:.2f}")

    def ejecutar(self):
        """
        Método principal del programa.
        Ejecuta el bucle principal del menú.
        """
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
            elif opcion == 0:
                print("Saliendo...")
                break
            else:
                print("Opción incorrecta")
            
            print()  # Línea en blanco para separar las operaciones

def main():
    """
    Función principal que inicia el programa.
    """
    programa = ProyectoIntegrador()
    programa.ejecutar()

if __name__ == "__main__":
    main()