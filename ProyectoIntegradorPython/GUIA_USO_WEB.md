# Guía de Uso - Sistema Web de Gestión de Anuncios Publicitarios

## Introducción

Esta guía describe cómo usar la nueva interfaz web del Sistema de Gestión de Anuncios Publicitarios desarrollado con Flask. El sistema mantiene toda la funcionalidad del sistema de consola original pero ahora con una interfaz web moderna y fácil de usar.

## Instalación y Ejecución

### Requisitos Previos
- Python 3.8 o superior
- MongoDB 4.0 o superior (ejecutándose)
- Navegador web moderno

### Instalación
1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar variables de entorno**:
   ```bash
   # Copiar archivo de configuración
   copy .env.example .env
   
   # Editar .env según tu configuración
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

4. **Acceder a la aplicación**:
   Abrir navegador en `http://localhost:5000`

## Funcionalidades Web

### 🏠 Página Principal
- **URL**: `/`
- **Descripción**: Vista general del sistema con estadísticas
- **Características**:
  - Contador de anuncios totales
  - Lista de anuncios recientes
  - Accesos rápidos a funciones principales
  - Información del sistema

### 📢 Gestión de Anuncios

#### Listar Anuncios
- **URL**: `/anuncios`
- **Características**:
  - Vista de tabla con todos los anuncios
  - Búsqueda avanzada con filtros
  - Filtros por medio, tipo de módulo, precio
  - Acciones rápidas (ver, editar, eliminar)

#### Crear Anuncio
- **URL**: `/anuncios/nuevo`
- **Formulario incluye**:
  - Código único del anuncio
  - Nombre del producto
  - Eslogan (opcional)  
  - Descripción detallada (opcional)
  - Precio
  - Medio de comunicación
  - Tipo de módulo
  - Frecuencia de publicación

#### Ver Detalle de Anuncio
- **URL**: `/anuncios/<id>`
- **Características**:
  - Vista completa del anuncio
  - Información de configuración
  - Fechas de creación y modificación
  - Acciones rápidas (editar, eliminar)

#### Editar Anuncio
- **URL**: `/anuncios/<id>/editar`
- **Características**:
  - Formulario pre-rellenado con datos actuales
  - Validación de campos
  - Confirmación de cambios

#### Eliminar Anuncio
- **Acción**: Botón en listas y detalle
- **Características**:
  - Modal de confirmación
  - Eliminación segura
  - Mensaje de confirmación

### 📊 Matriz de Precios
- **URL**: `/matriz-precios`
- **Características**:
  - Análisis de precios por medio y tipo de módulo
  - Estadísticas (promedio, mínimo, máximo)
  - Vista organizada por medio de comunicación
  - Información estadística general

### ⚙️ Configuración del Sistema

#### Página Principal de Configuración
- **URL**: `/configuracion`
- **Acceso a**:
  - Gestión de medios de comunicación
  - Gestión de tipos de módulo
  - Gestión de frecuencias de publicación

#### Medios de Comunicación
- **URL**: `/configuracion/medios`
- **Funciones**:
  - Listar todos los medios
  - Ver detalles de cada medio
  - Estado activo/inactivo

#### Tipos de Módulo
- **URL**: `/configuracion/tipos`
- **Funciones**:
  - Listar todos los tipos
  - Ver configuración de módulos
  - Gestión de estados

#### Frecuencias de Publicación
- **URL**: `/configuracion/frecuencias`
- **Funciones**:
  - Listar todas las frecuencias
  - Ver descripciones
  - Gestión de estados

## Características de la Interfaz Web

### 🎨 Diseño Moderno
- **Bootstrap 5**: Interfaz responsiva y moderna
- **Iconos**: Bootstrap Icons para mejor UX
- **Colores**: Esquema de colores profesional
- **Responsivo**: Funciona en móviles, tablets y desktop

### 🔍 Búsqueda Avanzada
- **Filtros múltiples**:
  - Por término de búsqueda (código o producto)
  - Por medio de comunicación
  - Por tipo de módulo
  - Por rango de precios
- **Resultados en tiempo real**
- **Limpieza fácil de filtros**

### 💡 Experiencia de Usuario
- **Mensajes flash**: Confirmaciones y errores claros
- **Validación de formularios**: Validación en tiempo real
- **Tooltips**: Ayuda contextual
- **Modales de confirmación**: Para acciones importantes
- **Navegación intuitiva**: Menús organizados

### 📱 Responsive Design
- **Móviles**: Interfaz optimizada para pantallas pequeñas
- **Tablets**: Diseño adaptativo
- **Desktop**: Aprovecha el espacio disponible
- **Navegación**: Menú hamburguesa en móviles

## Flujos de Trabajo Típicos

### Crear un Nuevo Anuncio
1. Ir a "Anuncios" → "Crear Nuevo"
2. Completar el formulario:
   - Código único
   - Información del producto
   - Configuración de publicación
3. Guardar y revisar
4. Confirmar creación

### Buscar Anuncios
1. Ir a "Anuncios" → "Ver Todos"
2. Usar filtros de búsqueda:
   - Escribir término de búsqueda
   - Seleccionar filtros
   - Hacer clic en "Buscar"
3. Revisar resultados
4. Acceder a acciones específicas

### Generar Matriz de Precios
1. Ir a "Matriz de Precios"
2. Revisar análisis por medio
3. Analizar estadísticas
4. Usar datos para toma de decisiones

### Configurar Datos Básicos
1. Ir a "Configuración"
2. Seleccionar tipo de datos (medios, tipos, frecuencias)
3. Revisar configuración actual
4. Realizar cambios si es necesario

## Ventajas de la Versión Web

### ✅ Mejoras sobre la Versión de Consola
- **Accesibilidad**: Desde cualquier navegador
- **Interfaz visual**: Más intuitiva y fácil de usar
- **Productividad**: Operaciones más rápidas
- **Colaboración**: Múltiples usuarios simultáneos
- **Responsive**: Funciona en cualquier device

### 🔧 Características Técnicas
- **Flask**: Framework web robusto
- **MongoDB**: Base de datos NoSQL escalable
- **Bootstrap**: UI framework moderno
- **Validación**: Formularios con validación completa
- **Logging**: Sistema de logs detallado
- **Configuración**: Gestión de configuración flexible

## Solución de Problemas

### Problemas Comunes

#### La aplicación no inicia
- Verificar que MongoDB esté ejecutándose
- Verificar que las dependencias estén instaladas
- Revisar el archivo `.env`

#### Error de conexión a base de datos
- Verificar configuración de MongoDB en `.env`
- Verificar que el puerto sea correcto
- Verificar permisos de base de datos

#### Formularios no se envían
- Verificar validación de campos
- Verificar conexión a internet
- Revisar logs de la aplicación

### Logs y Debugging
- **Archivo de logs**: `logs/sistema.log`
- **Nivel de debug**: Configurar `FLASK_DEBUG=True` en `.env`
- **Logs en consola**: Ejecutar con `python app.py`

## Migración desde la Versión de Consola

### Compatibilidad
- **Base de datos**: Utiliza la misma base de datos MongoDB
- **Datos**: Todos los datos existentes son compatibles
- **Configuración**: Migración automática de configuración

### Coexistencia
- **Ambas versiones**: Pueden ejecutarse simultáneamente
- **Datos compartidos**: Ambas versiones usan la misma BD
- **Configuración**: Configuración compartida

## Personalización

### Configuración Avanzada
- **Puerto**: Cambiar `FLASK_PORT` en `.env`
- **Host**: Cambiar `FLASK_HOST` en `.env`
- **Debug**: Activar/desactivar `FLASK_DEBUG`
- **Logging**: Configurar nivel en `LOG_LEVEL`

### Extensiones Futuras
- **API REST**: Endpoints para integración
- **Autenticación**: Sistema de usuarios
- **Reportes**: Exportación de datos
- **Dashboard**: Gráficos y métricas

## Conclusión

La versión web del Sistema de Gestión de Anuncios Publicitarios ofrece una experiencia moderna y eficiente, manteniendo toda la funcionalidad del sistema original pero con una interfaz mucho más accesible y fácil de usar.

Para soporte técnico o consultas, revisar la documentación técnica en `README.md` o contactar al equipo de desarrollo.

---

**Desarrollado por The Gods of Programming**  
**Versión Web**: 2.0.0  
**Fecha**: Diciembre 2024
