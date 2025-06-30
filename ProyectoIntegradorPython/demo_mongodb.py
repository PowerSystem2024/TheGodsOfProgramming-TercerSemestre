"""
Script de demostración completa del Sistema de Gestión de Anuncios Publicitarios
con persistencia en MongoDB
"""
import sys
import os
import time

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from db.conexion import conectar, desconectar
from services.datos_basicos_service import DatosBasicosService
from services.anuncio_service import AnuncioService
from models.anuncio import Anuncio

def mostrar_titulo(titulo):
    """Muestra un título con formato"""
    print("\n" + "="*60)
    print(f"🎯 {titulo}")
    print("="*60)

def pausa():
    """Pausa para permitir leer la salida"""
    time.sleep(2)

def demo_completa():
    """Ejecuta una demostración completa del sistema"""
    print("🚀 DEMOSTRACIÓN DEL SISTEMA DE GESTIÓN DE ANUNCIOS")
    print("📊 Sistema con persistencia en MongoDB")
    
    # Conectar a MongoDB
    if not conectar():
        print("❌ No se pudo conectar a MongoDB. Asegúrate de que esté ejecutándose.")
        return False
    
    try:
        # 1. Inicializar datos básicos
        mostrar_titulo("INICIALIZACIÓN DE DATOS BÁSICOS")
        medios = DatosBasicosService.inicializar_medios_comunicacion()
        modulos = DatosBasicosService.inicializar_tipos_modulos()
        frecuencias = DatosBasicosService.inicializar_frecuencias_publicacion()
        
        print(f"✅ {len(medios)} medios de comunicación inicializados")
        print(f"✅ {len(modulos)} tipos de módulos inicializados")
        print(f"✅ {len(frecuencias)} frecuencias de publicación inicializadas")
        pausa()
        
        # 2. Inicializar anuncios de prueba
        mostrar_titulo("INICIALIZACIÓN DE ANUNCIOS DE PRUEBA")
        AnuncioService.inicializar_anuncios_prueba(medios, modulos, frecuencias)
        anuncios = AnuncioService.obtener_todos_los_anuncios()
        print(f"✅ {len(anuncios)} anuncios de prueba creados")
        pausa()
        
        # 3. Mostrar todos los anuncios
        mostrar_titulo("LISTADO DE ANUNCIOS ACTUALES")
        for i, anuncio in enumerate(anuncios, 1):
            print(f"{i:2d}. {anuncio.empresa} - {anuncio.medio.nombre} - "
                  f"{anuncio.modulo.nombre} - {anuncio.frecuencia.nombre} - ${anuncio.precio:,.2f}")
        pausa()
        
        # 4. Calcular ingresos totales
        mostrar_titulo("CÁLCULO DE INGRESOS TOTALES")
        total_ingresos = sum(anuncio.precio for anuncio in anuncios if anuncio.activo)
        print(f"💰 Ingresos totales: ${total_ingresos:,.2f}")
        pausa()
        
        # 5. Buscar anuncios por empresa
        mostrar_titulo("BÚSQUEDA POR EMPRESA")
        empresa_buscar = "Marketing Masters"
        anuncios_empresa = AnuncioService.buscar_anuncios_por_empresa(empresa_buscar)
        print(f"🔍 Anuncios de '{empresa_buscar}':")
        for anuncio in anuncios_empresa:
            print(f"   - {anuncio.medio.nombre} - {anuncio.modulo.nombre} - "
                  f"{anuncio.frecuencia.nombre} - ${anuncio.precio:,.2f}")
        pausa()
        
        # 6. Crear un nuevo anuncio
        mostrar_titulo("CREACIÓN DE NUEVO ANUNCIO")
        
        nuevo_anuncio = AnuncioService.crear_anuncio(
            medio=medios[0],  # El Norteño
            modulo=modulos[2],  # M3
            frecuencia=frecuencias[0],  # D (Diario)
            empresa='Empresa Demo',
            precio=2100.0
        )
        
        if nuevo_anuncio:
            print(f"✅ Nuevo anuncio creado: {nuevo_anuncio.empresa} - ${nuevo_anuncio.precio:,.2f}")
        pausa()
        
        # 7. Actualizar total de anuncios
        anuncios_actualizados = AnuncioService.obtener_todos_los_anuncios()
        print(f"📊 Total de anuncios después de la creación: {len(anuncios_actualizados)}")
        pausa()
        
        # 8. Modificar el anuncio recién creado
        mostrar_titulo("MODIFICACIÓN DE ANUNCIO")
        if nuevo_anuncio:
            anuncio_actualizado = AnuncioService.actualizar_anuncio_por_id(
                nuevo_anuncio.id,
                empresa="Empresa Demo Actualizada",
                precio=2500.0
            )
            if anuncio_actualizado:
                print("✅ Anuncio modificado exitosamente")
                print(f"   Nuevo nombre: {anuncio_actualizado.empresa}")
                print(f"   Nuevo precio: ${anuncio_actualizado.precio:,.2f}")
            else:
                print("❌ Error al modificar el anuncio")
        pausa()
        
        # 9. Mostrar estadísticas finales
        mostrar_titulo("ESTADÍSTICAS FINALES")
        anuncios_finales = AnuncioService.obtener_todos_los_anuncios()
        total_final = sum(anuncio.precio for anuncio in anuncios_finales if anuncio.activo)
        
        print(f"📊 Total de anuncios: {len(anuncios_finales)}")
        print(f"💰 Ingresos totales finales: ${total_final:,.2f}")
        
        # Contar por medio
        medios_conteo = {}
        for anuncio in anuncios_finales:
            if anuncio.activo:
                medio = anuncio.medio.nombre
                medios_conteo[medio] = medios_conteo.get(medio, 0) + 1
        
        print("\n📈 Distribución por medio:")
        for medio, cantidad in medios_conteo.items():
            print(f"   {medio}: {cantidad} anuncios")
        
        pausa()
        
        # 10. Demostrar eliminación lógica
        mostrar_titulo("ELIMINACIÓN LÓGICA DE ANUNCIO")
        if nuevo_anuncio:
            AnuncioService.eliminar_anuncio(nuevo_anuncio.id)
            print(f"✅ Anuncio de '{nuevo_anuncio.empresa}' eliminado (eliminación lógica)")
            
            # Verificar que ya no aparece en listados activos
            anuncios_activos = AnuncioService.obtener_todos_los_anuncios()
            print(f"📊 Anuncios activos después de eliminación: {len(anuncios_activos)}")
        
        mostrar_titulo("DEMOSTRACIÓN COMPLETADA")
        print("✅ Todas las funcionalidades han sido demostradas exitosamente")
        print("📊 Los datos han sido persistidos en MongoDB")
        print("🔄 Puedes ejecutar el sistema principal para interactuar manualmente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante la demostración: {e}")
        return False
    
    finally:
        # Desconectar de MongoDB
        desconectar()

def main():
    """Función principal"""
    print("🎯 Sistema de Gestión de Anuncios Publicitarios - Demostración MongoDB")
    print("⏳ Iniciando demostración completa...")
    
    if demo_completa():
        print("\n🎉 ¡Demostración completada exitosamente!")
        print("💡 Para usar el sistema interactivamente, ejecuta: python src/main.py")
    else:
        print("\n❌ La demostración falló")
        print("🔧 Verifica que MongoDB esté ejecutándose y las dependencias instaladas")

if __name__ == "__main__":
    main()
