# Proyecto Integrador - Sistema de Gestión de Anuncios Publicitarios

## 🌐 **NUEVO: Versión Web con Flask**

Este proyecto ahora incluye una **interfaz web moderna** desarrollada con Flask, además de la versión original de consola. Ambas versiones comparten la misma base de datos MongoDB y funcionalidades.

### 🚀 **Inicio Rápido - Versión Web**

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Verificar sistema (automático)
python init_web.py

# 3. Iniciar aplicación web
python app.py

# 4. Abrir navegador en: http://localhost:5000
```

### 📱 **Características de la Versión Web**
- **🎨 Interfaz moderna**: Bootstrap 5 + diseño responsive
- **📊 Dashboard interactivo**: Estadísticas y vista general
- **🔍 Búsqueda avanzada**: Filtros múltiples en tiempo real
- **📝 Formularios validados**: Creación/edición con validación
- **📈 Matriz de precios visual**: Análisis gráfico de datos
- **⚙️ Configuración web**: Gestión de datos básicos
- **📱 Responsive**: Funciona en móviles, tablets y desktop

---

# Sistema Original de Consola

Este proyecto es una adaptación a Python del sistema de gestión de anuncios publicitarios originalmente desarrollado en Java. El sistema permite gestionar anuncios publicitarios para diferentes medios de comunicación, con distintos tipos de módulos y frecuencias de publicación.

**🎯 Características principales:**
- **Interfaz Web Moderna**: Aplicación web desarrollada con Flask
- **Interfaz de Consola**: Opción de uso por consola (versión legacy)
- **Persistencia en MongoDB**: Todos los datos se almacenan en una base de datos MongoDB
- **CRUD completo**: Crear, leer, actualizar y eliminar anuncios
- **Búsquedas avanzadas**: Buscar por empresa, calcular ingresos totales
- **Matriz de precios**: Análisis visual de precios por medio y tipo
- **Responsive Design**: Funciona en móviles, tablets y desktop
- **Datos de prueba preconfigurados**: Sistema listo para usar

## Funcionalidades

El sistema ofrece las siguientes funcionalidades:

### Via Web (Recomendado)
1. **Dashboard**: Vista general con estadísticas
2. **Gestión de Anuncios**: CRUD completo con interfaz moderna
3. **Búsqueda Avanzada**: Filtros por medio, tipo, precio
4. **Matriz de Precios**: Análisis visual de precios
5. **Configuración**: Gestión de medios, tipos y frecuencias

### Via Consola (Legacy)
1. **Mostrar precios**: Visualiza la matriz de precios según el tipo de módulo y frecuencia de publicación
2. **Agregar anuncio**: Permite crear un nuevo anuncio seleccionando medio, módulo, frecuencia y empresa
3. **Eliminar anuncio**: Elimina un anuncio existente por su ID
4. **Mostrar anuncios**: Lista todos los anuncios registrados en el sistema
5. **Buscar anuncio por empresa**: Busca y muestra anuncios de una empresa específica
6. **Modificar anuncio**: Permite editar los datos de un anuncio existente
7. **Calcular ingresos totales**: Muestra el total de ingresos de todos los anuncios

## Estructura del Proyecto

```
ProyectoIntegradorPython/
│
├── src/
│   ├── main.py                     # Archivo principal con la lógica del programa
│   ├── db/                         # Configuración de base de datos
│   │   └── conexion.py            # Conexión a MongoDB
│   ├── models/                     # Modelos de datos (MongoDB)
│   │   ├── anuncio.py             # Modelo Anuncio
│   │   ├── frecuencia_publicacion.py  # Modelo FrecuenciaPublicacion
│   │   ├── medio_comunicacion.py   # Modelo MedioComunicacion
│   │   └── tipo_modulo.py         # Modelo TipoModulo
│   └── services/                   # Servicios de negocio
│       ├── __init__.py
│       ├── anuncio_service.py     # Servicio para gestión de anuncios
│       └── datos_basicos_service.py # Servicio para datos básicos
├── tests/                          # Pruebas del sistema
│   ├── __init__.py
│   ├── conftest.py
│   └── test_integracion.py
├── test_conexion.py                # Script de prueba de conexión MongoDB
├── test_sistema.py                 # Script de pruebas completas
├── GUIA_USO.md                     # Guía detallada de uso
├── README.md
├── requirements.txt
└── setup.py
```

## Modelos de Datos (MongoDB)

El sistema utiliza **MongoDB** como base de datos NoSQL para almacenar todos los datos de forma persistente. Los modelos están implementados usando **MongoEngine** como ODM (Object Document Mapper).

### MedioComunicacion
Colección que almacena los diferentes medios de comunicación:
- El Norteño, Del Sur, Patagónico, Del Centro, El Cuyano, Del Litoral
- **Campos**: `nombre`, `fecha_creacion`, `activo`

### TipoModulo
Colección que define los diferentes tamaños de módulos publicitarios:
- M1, M2, M3, M4, M6, M8, M12, M16
- **Campos**: `nombre`, `fecha_creacion`, `activo`

### FrecuenciaPublicacion
Colección que especifica las frecuencias de publicación:
- D (Diario), LAV (Lunes a Viernes), SD (Sábado y Domingo), 1S, 2S, 3S, 1.15, 1.30
- **Campos**: `nombre`, `descripcion`, `fecha_creacion`, `activo`

### Anuncio
Colección principal que representa un anuncio publicitario:
- **Campos**: `medio` (referencia), `modulo` (referencia), `frecuencia` (referencia), `precio`, `empresa`, `fecha_creacion`, `activo`
- **Índices**: Por empresa, fecha_creacion, activo, y compuesto por medio-modulo-frecuencia

## Matriz de Precios

El sistema utiliza una matriz de precios predefinida que determina el costo de cada anuncio según la combinación de módulo y frecuencia de publicación. Los precios van desde $100 hasta $11,000.

## Instalación y Ejecución

### Requisitos Previos
- **Python 3.6 o superior**
- **MongoDB 4.0 o superior** (debe estar ejecutándose)
- **Conexión a Internet** (para instalar dependencias)

### Instalación
1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd ProyectoIntegradorPython
   ```

2. **Instalar MongoDB**
   - Descarga e instala MongoDB desde [mongodb.com](https://www.mongodb.com/try/download/community)
   - Asegúrate de que el servicio MongoDB esté ejecutándose

3. **Configurar entorno virtual de Python**
   ```bash
   python -m venv .venv
   # En Windows
   .venv\Scripts\activate
   # En Linux/Mac
   source .venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

### Verificar Instalación
Ejecuta el script de prueba para verificar que todo está configurado correctamente:
```bash
python test_conexion.py
```

### Ejecución
Para ejecutar el programa:
```bash
python src/main.py
```

O usando el comando de consola definido en setup.py:
```bash
pip install -e .
anuncios
```

### Configuración de MongoDB
Por defecto, el sistema se conecta a:
- **Host**: localhost:27017
- **Base de datos**: proyecto_anuncios_publicitarios

Para cambiar la configuración, edita el archivo `src/db/conexion.py`.

## Datos de Prueba

El sistema viene con **datos de prueba automáticos** que se crean en MongoDB la primera vez que ejecutas la aplicación:

### Datos Básicos Precargados:
- **6 medios de comunicación**
- **8 tipos de módulos** (M1 a M16)
- **8 frecuencias de publicación**

### Anuncios de Prueba:
El sistema crea automáticamente 11 anuncios de prueba:

- Tech Solutions Inc. ($2,500.00)
- Innovate Corp. ($1,800.00)
- Global Industries Ltd. ($4,300.00)
- Creative Designs Studio ($500.00)
- Marketing Masters ($1,300.00)
- Digital Dynamics ($1,000.00)
- Code Wizards ($200.00)
- Future Vision ($900.00)
- Open Source Solutions ($2,100.00)
- Web Dev Experts ($2,100.00)
- Marketing Masters ($2,100.00)

**Total de ingresos precargados: $18,800.00**

### Persistencia de Datos
- Los datos se almacenan permanentemente en MongoDB
- Los datos de prueba solo se crean una vez
- Puedes limpiar la base de datos eliminando la BD `proyecto_anuncios_publicitarios`

## Pruebas del Sistema

### Verificar conexión a MongoDB:
```bash
python test_conexion.py
```

### Ejecutar todas las funcionalidades de prueba:
```bash
python test_sistema.py
```

Este script ejecuta automáticamente todas las funcionalidades del sistema y muestra los resultados.

### Pruebas unitarias:
```bash
python -m pytest tests/
```

### Solución de Problemas
Si obtienes errores de conexión:
1. Verifica que MongoDB esté ejecutándose
2. Verifica la configuración en `src/db/conexion.py`
3. Verifica que las dependencias estén instaladas: `pip install -r requirements.txt`

## Características del Código

- **Arquitectura MongoDB**: Utiliza MongoDB como base de datos NoSQL
- **MongoEngine ODM**: Object Document Mapper para Python
- **Orientado a Objetos**: Utiliza clases para modelar los diferentes componentes
- **Patrón de Servicios**: Separación de lógica de negocio en servicios
- **Validación de Entrada**: Incluye validación para entradas del usuario y datos
- **Interfaz Interactiva**: Menú de consola fácil de usar
- **Gestión de Errores**: Manejo robusto de errores para base de datos y entrada de usuario
- **Índices de Base de Datos**: Optimización de consultas con índices MongoDB
- **Documentación**: Código documentado con docstrings en español
- **Logging**: Sistema de mensajes informativos para el usuario

## Diferencias con la Versión Java

Esta versión en Python con MongoDB ofrece ventajas significativas sobre el original en Java:

### Funcionalidades Nuevas:
- **Persistencia permanente**: Los datos se mantienen entre ejecuciones
- **Base de datos NoSQL**: Flexibilidad de MongoDB para futuras extensiones
- **Servicios especializados**: Separación clara de responsabilidades
- **Inicialización automática**: Creación automática de datos de prueba
- **Validación de datos**: Validación a nivel de base de datos y aplicación

### Adaptaciones de Java a Python:
- Uso de MongoEngine en lugar de JPA/Hibernate
- Manejo de excepciones específico de Python y MongoDB
- Sintaxis y convenciones de Python
- Uso de decoradores y métodos mágicos de Python

## Medios de Comunicación Disponibles
1. El Norteño
2. Del Sur
3. Patagónico
4. Del Centro
5. El Cuyano
6. Del Litoral

## Tipos de Módulos Disponibles
1. M1 (más pequeño)
2. M2
3. M3
4. M4
5. M6
6. M8
7. M12
8. M16 (más grande)

## Frecuencias de Publicación Disponibles
1. D (Diario)
2. LAV (Lunes a Viernes)
3. SD (Sábado y Domingo)
4. 1S (Una vez por semana)
5. 2S (Dos veces por semana)
6. 3S (Tres veces por semana)
7. 1.15 (Cada 15 días)
8. 1.30 (Una vez al mes)

## Créditos

Desarrollado por: TheGodsOfProgramming
Adaptación de Java a Python del sistema de gestión de anuncios publicitarios.