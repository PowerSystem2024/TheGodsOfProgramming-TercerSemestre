# Guía de Uso - Sistema de Gestión de Anuncios Publicitarios

## Cómo ejecutar el programa

### Opción 1: Ejecutar directamente
```bash
python src/main.py
```

### Opción 2: Instalación como paquete
```bash
pip install -e .
anuncios
```

## Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```
****************************************
********** Menú Principal **********
****************************************
1. Mostrar precios
2. Agregar anuncio
3. Eliminar anuncio
4. Mostrar anuncios
5. Buscar anuncio por empresa
6. Modificar anuncio
7. Calcular ingresos totales de los anuncios cargados
0. Salir
****************************************
```

## Funcionalidades Detalladas

### 1. Mostrar precios
- Muestra la matriz completa de precios
- Combina todos los tipos de módulos con todas las frecuencias
- Útil para consultar tarifas antes de crear anuncios

### 2. Agregar anuncio
- Selecciona el medio de comunicación (1-6)
- Selecciona el tipo de módulo (1-8)
- Selecciona la frecuencia de publicación (1-8)
- Ingresa el nombre de la empresa
- El precio se calcula automáticamente

### 3. Eliminar anuncio
- Primero muestra la lista de anuncios
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
