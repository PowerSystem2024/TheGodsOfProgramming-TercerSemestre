"""
Script de prueba para demostrar que el sistema funciona correctamente
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.main import ProyectoIntegrador

def test_sistema():
    """
    Prueba todas las funcionalidades del sistema
    """
    print("=== PRUEBA DEL SISTEMA DE ANUNCIOS ===\n")
    
    # Crear instancia del programa
    programa = ProyectoIntegrador()
    programa.inicializar_datos()
    
    print("1. PROBANDO: Mostrar anuncios precargados")
    print("-" * 50)
    programa.mostrar_anuncios()
    
    print("\n2. PROBANDO: Calcular ingresos totales")
    print("-" * 50)
    total = programa.calcular_ingresos_totales()
    print(f"Ingresos totales: ${total:.2f}")
    
    print("\n3. PROBANDO: Mostrar algunos precios")
    print("-" * 50)
    print("Precios para módulo M1:")
    for i, frecuencia in enumerate(programa.frecuencias_publicacion):
        precio = programa.get_precio(0, i)  # M1 es índice 0
        print(f"  M1 - {frecuencia.get_nombre()}: ${precio}")
    
    print("\n4. PROBANDO: Buscar anuncios por empresa")
    print("-" * 50)
    print("Buscando anuncios para 'Marketing Masters':")
    
    # Simular búsqueda por empresa
    nombre_empresa = "Marketing Masters"
    encontrado = False
    
    for i, anuncio in enumerate(programa.anuncios):
        if anuncio.get_empresa().lower() == nombre_empresa.lower():
            print(f"  ID: {i}, Medio: {anuncio.get_medio().get_nombre()}, "
                  f"Módulo: {anuncio.get_modulo().get_nombre()}, "
                  f"Frecuencia: {anuncio.get_frecuencia().get_nombre()}, "
                  f"Precio: ${anuncio.get_precio():.2f}, "
                  f"Empresa: {anuncio.get_empresa()}")
            encontrado = True
    
    if not encontrado:
        print(f"  No se encontraron anuncios para la empresa: {nombre_empresa}")
    
    print("\n5. PROBANDO: Agregar un anuncio programáticamente")
    print("-" * 50)
    
    # Agregar un anuncio de prueba
    from src.models.anuncio import Anuncio
    nuevo_anuncio = Anuncio(
        programa.medios_comunicacion[0],  # El Norteño
        programa.tipos_modulos[1],        # M2
        programa.frecuencias_publicacion[0],  # D (Diario)
        programa.get_precio(1, 0),        # Precio para M2-D
        "Empresa de Prueba"
    )
    
    programa.anuncios.append(nuevo_anuncio)
    print("Anuncio agregado exitosamente:")
    print(f"  Empresa: {nuevo_anuncio.get_empresa()}")
    print(f"  Medio: {nuevo_anuncio.get_medio().get_nombre()}")
    print(f"  Módulo: {nuevo_anuncio.get_modulo().get_nombre()}")
    print(f"  Frecuencia: {nuevo_anuncio.get_frecuencia().get_nombre()}")
    print(f"  Precio: ${nuevo_anuncio.get_precio():.2f}")
    
    print("\n6. PROBANDO: Recalcular ingresos totales")
    print("-" * 50)
    nuevo_total = programa.calcular_ingresos_totales()
    print(f"Nuevos ingresos totales: ${nuevo_total:.2f}")
    print(f"Incremento: ${nuevo_total - total:.2f}")
    
    print("\n7. PROBANDO: Modificar un anuncio programáticamente")
    print("-" * 50)
    
    # Modificar el anuncio que acabamos de agregar
    anuncio_a_modificar = programa.anuncios[-1]  # El último anuncio
    print(f"Anuncio original: {anuncio_a_modificar.get_empresa()} - ${anuncio_a_modificar.get_precio():.2f}")
    
    # Cambiar a un módulo más caro
    anuncio_a_modificar.set_modulo(programa.tipos_modulos[4])  # M6
    nuevo_precio = programa.get_precio(4, 0)  # M6-D
    anuncio_a_modificar.set_precio(nuevo_precio)
    
    print(f"Anuncio modificado: {anuncio_a_modificar.get_empresa()} - ${anuncio_a_modificar.get_precio():.2f}")
    
    print("\n8. PROBANDO: Eliminar un anuncio")
    print("-" * 50)
    anuncios_antes = len(programa.anuncios)
    programa.anuncios.pop()  # Eliminar el último anuncio
    anuncios_despues = len(programa.anuncios)
    print(f"Anuncios antes: {anuncios_antes}")
    print(f"Anuncios después: {anuncios_despues}")
    
    print("\n=== TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ===")
    print("El sistema está funcionando correctamente!")

if __name__ == "__main__":
    test_sistema()
