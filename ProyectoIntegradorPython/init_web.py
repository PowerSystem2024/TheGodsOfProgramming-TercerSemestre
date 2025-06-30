#!/usr/bin/env python3
"""
Script de inicialización rápida para la aplicación web
"""

import os
import sys
import subprocess
from pathlib import Path

def verificar_mongodb():
    """Verifica si MongoDB está ejecutándose"""
    try:
        import pymongo
        client = pymongo.MongoClient('localhost', 27017, serverSelectionTimeoutMS=2000)
        client.server_info()
        print("✅ MongoDB está ejecutándose correctamente")
        return True
    except Exception as e:
        print("❌ Error: MongoDB no está ejecutándose")
        print(f"   Detalle: {e}")
        print("   Por favor, inicia MongoDB antes de continuar")
        return False

def verificar_dependencias():
    """Verifica si las dependencias están instaladas"""
    try:
        import flask
        import flask_wtf
        import wtforms
        import mongoengine
        print("✅ Todas las dependencias están instaladas")
        return True
    except ImportError as e:
        print(f"❌ Error: Falta dependencia - {e}")
        print("   Ejecuta: pip install -r requirements.txt")
        return False

def crear_archivo_env():
    """Crea el archivo .env si no existe"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists() and env_example.exists():
        try:
            import shutil
            shutil.copy(env_example, env_file)
            print("✅ Archivo .env creado desde .env.example")
        except Exception as e:
            print(f"⚠️  No se pudo crear .env: {e}")
    elif env_file.exists():
        print("✅ Archivo .env ya existe")
    else:
        print("⚠️  No se encontró archivo .env.example")

def inicializar_datos():
    """Ejecuta el script de inicialización de datos"""
    try:
        print("🔄 Inicializando datos básicos...")
        result = subprocess.run([sys.executable, 'inicializar_proyecto.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Datos básicos inicializados correctamente")
        else:
            print("⚠️  Advertencia al inicializar datos:")
            print(result.stderr)
    except Exception as e:
        print(f"⚠️  Error al inicializar datos: {e}")

def main():
    """Función principal de inicialización"""
    print("🚀 Inicializando Sistema de Gestión de Anuncios Web")
    print("=" * 50)
    
    # Verificar MongoDB
    if not verificar_mongodb():
        print("\n❌ Inicialización fallida: MongoDB no disponible")
        return False
    
    # Verificar dependencias
    if not verificar_dependencias():
        print("\n❌ Inicialización fallida: Dependencias faltantes")
        return False
    
    # Crear archivo .env
    crear_archivo_env()
    
    # Inicializar datos
    inicializar_datos()
    
    print("\n✅ ¡Inicialización completada exitosamente!")
    print("\n🌐 Para iniciar la aplicación web:")
    print("   python app.py")
    print("\n🌐 Luego abre tu navegador en:")
    print("   http://localhost:5000")
    print("\n📋 Para usar la versión de consola:")
    print("   python src/main_nuevo.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
