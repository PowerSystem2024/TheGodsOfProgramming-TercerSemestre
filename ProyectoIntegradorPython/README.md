# Proyecto Integrador - Sistema de Gestión de Anuncios Publicitarios

Este proyecto es una adaptación a Python del sistema de gestión de anuncios publicitarios originalmente desarrollado en Java. El sistema permite gestionar anuncios publicitarios para diferentes medios de comunicación, con distintos tipos de módulos y frecuencias de publicación.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades a través de un menú interactivo:

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
│   └── models/                     # Modelos de datos
│       ├── anuncio.py             # Clase Anuncio
│       ├── frecuencia_publicacion.py  # Clase FrecuenciaPublicacion
│       ├── medio_comunicacion.py   # Clase MedioComunicacion
│       └── tipo_modulo.py         # Clase TipoModulo
├── README.md
├── requirements.txt
└── setup.py
```

## Modelos de Datos

### MedioComunicacion
Representa los diferentes medios de comunicación donde se pueden publicar anuncios:
- El Norteño, Del Sur, Patagónico, Del Centro, El Cuyano, Del Litoral

### TipoModulo
Define los diferentes tamaños de módulos publicitarios:
- M1, M2, M3, M4, M6, M8, M12, M16

### FrecuenciaPublicacion
Especifica las frecuencias de publicación disponibles:
- D (Diario), LAV (Lunes a Viernes), SD (Sábado y Domingo), 1S, 2S, 3S, 1.15, 1.30

### Anuncio
Clase principal que representa un anuncio publicitario con:
- Medio de comunicación
- Tipo de módulo
- Frecuencia de publicación
- Precio (calculado automáticamente)
- Nombre de la empresa

## Matriz de Precios

El sistema utiliza una matriz de precios predefinida que determina el costo de cada anuncio según la combinación de módulo y frecuencia de publicación. Los precios van desde $100 hasta $11,000.

## Instalación y Ejecución

### Requisitos
- Python 3.6 o superior

### Instalación
1. Clona el repositorio
2. Navega al directorio del proyecto
3. Instala las dependencias (actualmente no hay dependencias externas):
   ```bash
   pip install -r requirements.txt
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

## Datos de Prueba

El sistema viene precargado con 11 anuncios de prueba de diferentes empresas para facilitar las pruebas y demostración de funcionalidades.

## Características del Código

- **Orientado a Objetos**: Utiliza clases para modelar los diferentes componentes del sistema
- **Validación de Entrada**: Incluye validación para entradas del usuario
- **Interfaz Interactiva**: Menú de consola fácil de usar
- **Gestión de Errores**: Manejo básico de errores para entradas inválidas
- **Documentación**: Código documentado con docstrings en español

## Diferencias con la Versión Java

Esta versión en Python mantiene toda la funcionalidad del original en Java, con las siguientes adaptaciones:
- Uso de listas de Python en lugar de ArrayList de Java
- Manejo de excepciones específico de Python
- Sintaxis y convenciones de Python
- Uso de métodos getter/setter para mantener compatibilidad conceptual

---

## Estructura inicial

```
ProyectoIntegradorPython/
├── src/
│   ├── main.py
│   ├── db/
│   │   └── conexion.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   └── reserva.py
│   └── services/
│       ├── __init__.py
│       ├── usuario_service.py
│       └── reserva_service.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_usuario_service.py
│   ├── test_reserva_service.py
│   └── test_integracion.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Instalación y configuración inicial

1. **Crear y activar entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

2. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Asegúrate de tener MongoDB corriendo localmente**  
   (por defecto se conecta a `mongodb://localhost:27017/proyectointegrador`).

---

## Uso de MongoDB con mongoengine

Este proyecto utiliza [mongoengine](https://mongoengine.org/) como ODM para conectarse a MongoDB. Puedes administrar la base con MongoDB Compass si lo deseas.

La cadena de conexión se encuentra en `src/db/conexion.py`. Modifícala según tus credenciales o ambiente.

---

## Ejemplo de uso básico

```python
from db.conexion import conectar
from services.usuario_service import UsuarioService
from services.reserva_service import ReservaService
from datetime import datetime

conectar()

# Crear usuario
usuario = UsuarioService.crear_usuario("Ejemplo", "ejemplo@correo.com")
print("Usuario creado:", usuario)

# Crear reserva para usuario
reserva = ReservaService.crear_reserva(usuario, datetime.now(), "pendiente")
print("Reserva creada:", reserva)

# Consultar reservas de usuario
reservas = ReservaService.obtener_reservas_por_usuario(usuario)
print("Reservas encontradas:", reservas)
```

---

## Ejecutar el programa base

```bash
python src/main.py
```

El archivo `src/main.py` incluye ejemplos de conexión y creación de datos.

---

## Pruebas unitarias y de integración

Las pruebas están en la carpeta `tests/` y usan pytest. Se conectan a una base de datos de pruebas llamada `proyectointegrador_test`.

### Ejecutar todas las pruebas

```bash
pytest tests/
```

### Ejecutar solo el test de integración

```bash
pytest tests/test_integracion.py
```

> **Nota:** Asegúrate de que MongoDB esté corriendo antes de ejecutar las pruebas.

---

## Checklist de migración

- [x] Estructura base Python y configuración
- [x] Modelos/dominio migrados a mongoengine
- [x] Servicios y lógica de negocio migrados
- [x] Conexión y acceso a MongoDB (MongoDB Compass compatible)
- [x] Pruebas unitarias de modelos y servicios
- [x] Pruebas de integración del flujo principal
- [x] Documentación y ejemplos de uso

---

## ¿Qué sigue?

- Agregar endpoints REST (Flask, FastAPI) si se requiere API.
- Mejorar validaciones, autenticación, manejo de errores.
- Despliegue y automatización (CI/CD).

---

## Créditos

Equipo de migración: 5 integrantes.