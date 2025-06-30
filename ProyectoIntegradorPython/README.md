# Proyecto Integrador - Python

Este repositorio corresponde a la migración del Proyecto Integrador de Java a Python, usando MongoDB como base de datos y mongoengine como ODM.

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