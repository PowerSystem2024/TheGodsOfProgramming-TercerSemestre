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
├── tests/                          # Pruebas del sistema (opcional)
│   ├── __init__.py
│   ├── conftest.py
│   └── test_integracion.py
├── test_sistema.py                 # Script de pruebas completas
├── GUIA_USO.md                     # Guía detallada de uso
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

El sistema viene precargado con 11 anuncios de prueba de diferentes empresas para facilitar las pruebas y demostración de funcionalidades:

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

## Pruebas del Sistema

### Ejecutar todas las funcionalidades de prueba:
```bash
python test_sistema.py
```

Este script ejecuta automáticamente todas las funcionalidades del sistema y muestra los resultados.

### Pruebas unitarias:
```bash
python -m pytest tests/
```

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