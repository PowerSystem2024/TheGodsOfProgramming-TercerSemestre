# Guía de Uso - Sistema de Gestión de Anuncios Publicitarios

## 🚀 Requisitos Previos

### Instalación de MongoDB
1. **Descargar MongoDB**
   - Ve a [mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
   - Descarga la versión para tu sistema operativo
   - Instala siguiendo las instrucciones oficiales

2. **Iniciar MongoDB**
   - **Windows**: El servicio se inicia automáticamente o usa `net start MongoDB`
   - **Linux/Mac**: `sudo systemctl start mongod` o `brew services start mongodb-community`

3. **Verificar que MongoDB está ejecutándose**
   - Abre una terminal y ejecuta: `mongo` o `mongosh`
   - Deberías ver la conexión exitosa

### Instalación del Proyecto
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd ProyectoIntegradorPython

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🧪 Verificación de la Instalación

Antes de usar el programa, ejecuta:
```bash
python test_conexion.py
```

Si todo está correcto, verás:
```
✅ Todas las pruebas pasaron. El sistema está listo para usar con MongoDB.
```

## 🎯 Cómo ejecutar el programa

### Opción 1: Ejecutar directamente
```bash
python src/main.py
```

### Opción 2: Instalación como paquete
```bash
pip install -e .
anuncios
```

### Opción 3: Demostración automática
```bash
python demo_mongodb.py
```
Esta opción ejecuta una demostración completa de todas las funcionalidades.

## Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```
==================================================
🏢 SISTEMA DE GESTIÓN DE ANUNCIOS PUBLICITARIOS
==================================================
1. 📊 Mostrar precios
2. ➕ Agregar anuncio
3. ❌ Eliminar anuncio
4. 📋 Mostrar anuncios
5. 🔍 Buscar anuncio por empresa
6. ✏️  Modificar anuncio
7. 💰 Calcular ingresos totales
8. 🔄 Recargar datos desde BD
0. 🚪 Salir
==================================================
```

## 🗃️ Persistencia de Datos

**Importante**: Este sistema utiliza MongoDB para almacenar todos los datos de forma permanente:

- **Primera ejecución**: Se crean automáticamente los datos básicos y 11 anuncios de prueba
- **Ejecuciones posteriores**: Los datos se cargan desde la base de datos
- **Todos los cambios** (crear, modificar, eliminar) se guardan automáticamente en MongoDB
- **Base de datos**: `proyecto_anuncios_publicitarios`
- **Colecciones**: `medios_comunicacion`, `tipos_modulos`, `frecuencias_publicacion`, `anuncios`

## Funcionalidades Detalladas

### 1. 📊 Mostrar precios
- Muestra la matriz completa de precios
- Combina todos los tipos de módulos con todas las frecuencias
- Útil para consultar tarifas antes de crear anuncios
- **Datos cargados desde MongoDB**

### 2. ➕ Agregar anuncio
- Selecciona el medio de comunicación (cargado desde BD)
- Selecciona el tipo de módulo (cargado desde BD)
- Selecciona la frecuencia de publicación (cargado desde BD)
- Ingresa el nombre de la empresa
- El precio se calcula automáticamente
- **Se guarda permanentemente en MongoDB**

### 3. ❌ Eliminar anuncio
- Muestra todos los anuncios activos desde la BD
- Selecciona el anuncio por ID
- **Eliminación lógica**: Se marca como inactivo en MongoDB
- Los datos se conservan para auditoría

### 8. 🔄 Recargar datos desde BD
- **Nueva funcionalidad**: Recarga todos los datos desde MongoDB
- Útil si otros usuarios han hecho cambios
- Actualiza medios, módulos, frecuencias y anuncios
- Solicita el ID del anuncio a eliminar
- Confirma la eliminación

### 4. Mostrar anuncios
- Lista todos los anuncios con formato:
  - ID, Medio, Módulo, Frecuencia, Precio, Empresa

### 5. Buscar anuncio por empresa
- Ingresa el nombre de la empresa (no es case-sensitive)
- Muestra todos los anuncios de esa empresa
- Indica si no se encuentra ningún anuncio

### 6. Modificar anuncio
- Muestra la lista de anuncios
- Solicita el ID del anuncio a modificar
- Permite cambiar cada campo individualmente
- Presiona Enter para mantener el valor actual
- El precio se recalcula automáticamente

### 7. Calcular ingresos totales
- Suma todos los precios de los anuncios cargados
- Muestra el total formateado en pesos

## Datos Precargados

El sistema viene con 11 anuncios de prueba:
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

## Validaciones
- El programa valida que las entradas numéricas sean correctas
- Si introduces un valor no válido, te pedirá ingresar nuevamente
- Los índices fuera de rango son manejados apropiadamente
- La búsqueda por empresa no es sensible a mayúsculas/minúsculas

## Consejos de Uso
- Los IDs de anuncios empiezan desde 0
- Al modificar un anuncio, puedes presionar Enter para mantener el valor actual
- La búsqueda por empresa encuentra coincidencias exactas (ignorando mayúsculas)
- El programa mantiene todos los anuncios en memoria durante la ejecución
