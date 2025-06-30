"""
API REST con documentación Swagger para el sistema de anuncios
"""

from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields, Namespace
from src.controllers.controlador_principal import ControladorPrincipal
import logging

logger = logging.getLogger(__name__)

# Crear blueprint para la API
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Configurar Flask-RESTX
api = Api(
    api_bp,
    version='1.0',
    title='Sistema de Anuncios API',
    description='API REST para la gestión de anuncios publicitarios',
    doc='/docs/',  # URL para la documentación Swagger
    authorizations={
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Agregar: Bearer <token>'
        }
    }
)

# Definir namespaces
anuncios_ns = Namespace('anuncios', description='Operaciones con anuncios')
configuracion_ns = Namespace('configuracion', description='Configuración del sistema')
reportes_ns = Namespace('reportes', description='Reportes y análisis')

api.add_namespace(anuncios_ns)
api.add_namespace(configuracion_ns)
api.add_namespace(reportes_ns)

# Modelos para Swagger Documentation
anuncio_model = api.model('Anuncio', {
    'id': fields.String(required=True, description='ID único del anuncio'),
    'empresa': fields.String(required=True, description='Nombre de la empresa'),
    'precio': fields.Float(required=True, description='Precio del anuncio'),
    'medio': fields.String(required=True, description='Medio de comunicación'),
    'modulo': fields.String(required=True, description='Tipo de módulo'),
    'frecuencia': fields.String(required=True, description='Frecuencia de publicación'),
    'fecha_creacion': fields.DateTime(description='Fecha de creación'),
    'activo': fields.Boolean(description='Estado del anuncio')
})

anuncio_input = api.model('AnuncioInput', {
    'empresa': fields.String(required=True, description='Nombre de la empresa'),
    'precio': fields.Float(required=True, description='Precio del anuncio'),
    'medio_comunicacion_id': fields.String(required=True, description='ID del medio de comunicación'),
    'tipo_modulo_id': fields.String(required=True, description='ID del tipo de módulo'),
    'frecuencia_publicacion_id': fields.String(required=True, description='ID de la frecuencia de publicación')
})

busqueda_model = api.model('BusquedaAnuncios', {
    'termino': fields.String(description='Término de búsqueda'),
    'medio_comunicacion_id': fields.String(description='ID del medio de comunicación'),
    'tipo_modulo_id': fields.String(description='ID del tipo de módulo'),
    'precio_min': fields.Float(description='Precio mínimo'),
    'precio_max': fields.Float(description='Precio máximo')
})

medio_model = api.model('MedioComunicacion', {
    'id': fields.String(required=True, description='ID único'),
    'nombre': fields.String(required=True, description='Nombre del medio'),
    'descripcion': fields.String(description='Descripción del medio')
})

response_model = api.model('ApiResponse', {
    'exitoso': fields.Boolean(required=True, description='Indica si la operación fue exitosa'),
    'mensaje': fields.String(required=True, description='Mensaje de respuesta'),
    'datos': fields.Raw(description='Datos de respuesta')
})

# Inicializar controlador global
try:
    controlador = ControladorPrincipal()
    logger.info("Controlador API inicializado correctamente")
except Exception as e:
    logger.error(f"Error al inicializar controlador API: {e}")
    controlador = None

def verificar_controlador():
    """Verifica que el controlador esté disponible"""
    if controlador is None:
        return False, {"exitoso": False, "mensaje": "Sistema no disponible. Verifica la conexión a MongoDB."}
    return True, None

# ENDPOINTS DE ANUNCIOS
@anuncios_ns.route('/')
class AnunciosList(Resource):
    @anuncios_ns.doc('listar_anuncios')
    @anuncios_ns.marshal_list_with(anuncio_model)
    def get(self):
        """Obtiene todos los anuncios activos"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            anuncios = controlador.anuncio_service.listar_anuncios()
            anuncios_data = []
            
            for anuncio in anuncios:
                anuncio_data = {
                    'id': str(anuncio.id),
                    'empresa': anuncio.empresa,
                    'precio': anuncio.precio,
                    'medio': anuncio.medio.nombre if anuncio.medio else 'N/A',
                    'modulo': anuncio.modulo.nombre if anuncio.modulo else 'N/A',
                    'frecuencia': anuncio.frecuencia.nombre if anuncio.frecuencia else 'N/A',
                    'fecha_creacion': anuncio.fecha_creacion.isoformat() if anuncio.fecha_creacion else None,
                    'activo': anuncio.activo
                }
                anuncios_data.append(anuncio_data)
            
            return anuncios_data, 200
            
        except Exception as e:
            logger.error(f"Error al listar anuncios: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

    @anuncios_ns.doc('crear_anuncio')
    @anuncios_ns.expect(anuncio_input)
    @anuncios_ns.marshal_with(response_model)
    def post(self):
        """Crea un nuevo anuncio"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            datos = request.json
            if not datos:
                return {"exitoso": False, "mensaje": "Datos JSON requeridos"}, 400
            
            # Validar campos requeridos
            campos_requeridos = ['empresa', 'precio', 'medio_comunicacion_id', 'tipo_modulo_id', 'frecuencia_publicacion_id']
            for campo in campos_requeridos:
                if campo not in datos:
                    return {"exitoso": False, "mensaje": f"Campo requerido: {campo}"}, 400
            
            # Crear anuncio usando el método básico del servicio
            resultado = controlador.anuncio_service.crear_anuncio_web(datos)
            
            if resultado['exitoso']:
                return {"exitoso": True, "mensaje": "Anuncio creado exitosamente", "datos": {"id": str(resultado.get('anuncio', {}).get('id', ''))}}, 201
            else:
                return {"exitoso": False, "mensaje": resultado['mensaje']}, 400
                
        except Exception as e:
            logger.error(f"Error al crear anuncio: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

@anuncios_ns.route('/<string:anuncio_id>')
class AnuncioDetail(Resource):
    @anuncios_ns.doc('obtener_anuncio')
    @anuncios_ns.marshal_with(anuncio_model)
    def get(self, anuncio_id):
        """Obtiene un anuncio específico por ID"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            anuncio = controlador.anuncio_service.obtener_anuncio_por_id(anuncio_id)
            if not anuncio:
                return {"exitoso": False, "mensaje": "Anuncio no encontrado"}, 404
            
            anuncio_data = {
                'id': str(anuncio.id),
                'empresa': anuncio.empresa,
                'precio': anuncio.precio,
                'medio': anuncio.medio.nombre if anuncio.medio else 'N/A',
                'modulo': anuncio.modulo.nombre if anuncio.modulo else 'N/A',
                'frecuencia': anuncio.frecuencia.nombre if anuncio.frecuencia else 'N/A',
                'fecha_creacion': anuncio.fecha_creacion.isoformat() if anuncio.fecha_creacion else None,
                'activo': anuncio.activo
            }
            
            return anuncio_data, 200
            
        except Exception as e:
            logger.error(f"Error al obtener anuncio {anuncio_id}: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

    @anuncios_ns.doc('eliminar_anuncio')
    @anuncios_ns.marshal_with(response_model)
    def delete(self, anuncio_id):
        """Elimina un anuncio (marca como inactivo)"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            resultado = controlador.anuncio_service.eliminar_anuncio_web(anuncio_id)
            
            if resultado['exitoso']:
                return {"exitoso": True, "mensaje": "Anuncio eliminado exitosamente"}, 200
            else:
                return {"exitoso": False, "mensaje": resultado['mensaje']}, 404
                
        except Exception as e:
            logger.error(f"Error al eliminar anuncio {anuncio_id}: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

@anuncios_ns.route('/buscar')
class AnunciosBusqueda(Resource):
    @anuncios_ns.doc('buscar_anuncios')
    @anuncios_ns.expect(busqueda_model)
    @anuncios_ns.marshal_list_with(anuncio_model)
    def post(self):
        """Busca anuncios según criterios específicos"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            criterios = request.json if request.json else {}
            anuncios = controlador.anuncio_service.buscar_anuncios(criterios)
            
            anuncios_data = []
            for anuncio in anuncios:
                anuncio_data = {
                    'id': str(anuncio.id),
                    'empresa': anuncio.empresa,
                    'precio': anuncio.precio,
                    'medio': anuncio.medio.nombre if anuncio.medio else 'N/A',
                    'modulo': anuncio.modulo.nombre if anuncio.modulo else 'N/A',
                    'frecuencia': anuncio.frecuencia.nombre if anuncio.frecuencia else 'N/A',
                    'fecha_creacion': anuncio.fecha_creacion.isoformat() if anuncio.fecha_creacion else None,
                    'activo': anuncio.activo
                }
                anuncios_data.append(anuncio_data)
            
            return anuncios_data, 200
            
        except Exception as e:
            logger.error(f"Error al buscar anuncios: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

# ENDPOINTS DE CONFIGURACIÓN
@configuracion_ns.route('/medios')
class MediosList(Resource):
    @configuracion_ns.doc('listar_medios')
    @configuracion_ns.marshal_list_with(medio_model)
    def get(self):
        """Obtiene todos los medios de comunicación"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            medios_data = []
            
            for medio in medios:
                medio_data = {
                    'id': str(medio.id),
                    'nombre': medio.nombre,
                    'descripcion': getattr(medio, 'descripcion', '')
                }
                medios_data.append(medio_data)
            
            return medios_data, 200
            
        except Exception as e:
            logger.error(f"Error al listar medios: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

@configuracion_ns.route('/tipos')
class TiposList(Resource):
    @configuracion_ns.doc('listar_tipos')
    def get(self):
        """Obtiene todos los tipos de módulo"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            tipos_data = []
            
            for tipo in tipos:
                tipo_data = {
                    'id': str(tipo.id),
                    'nombre': tipo.nombre,
                    'descripcion': getattr(tipo, 'descripcion', '')
                }
                tipos_data.append(tipo_data)
            
            return tipos_data, 200
            
        except Exception as e:
            logger.error(f"Error al listar tipos: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

@configuracion_ns.route('/frecuencias')
class FrecuenciasList(Resource):
    @configuracion_ns.doc('listar_frecuencias')
    def get(self):
        """Obtiene todas las frecuencias de publicación"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            frecuencias = controlador.datos_basicos_service.listar_frecuencias_publicacion()
            frecuencias_data = []
            
            for frecuencia in frecuencias:
                frecuencia_data = {
                    'id': str(frecuencia.id),
                    'nombre': frecuencia.nombre,
                    'descripcion': getattr(frecuencia, 'descripcion', '')
                }
                frecuencias_data.append(frecuencia_data)
            
            return frecuencias_data, 200
            
        except Exception as e:
            logger.error(f"Error al listar frecuencias: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

# ENDPOINTS DE REPORTES
@reportes_ns.route('/matriz-precios')
class MatrizPrecios(Resource):
    @reportes_ns.doc('matriz_precios')
    def get(self):
        """Genera matriz de análisis de precios"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            matriz = controlador.anuncio_service.generar_matriz_precios()
            return {"exitoso": True, "datos": matriz}, 200
            
        except Exception as e:
            logger.error(f"Error al generar matriz de precios: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500

@reportes_ns.route('/estadisticas')
class Estadisticas(Resource):
    @reportes_ns.doc('estadisticas_generales')
    def get(self):
        """Obtiene estadísticas generales del sistema"""
        disponible, error = verificar_controlador()
        if not disponible:
            return error, 503
        
        try:
            anuncios = controlador.anuncio_service.listar_anuncios()
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            frecuencias = controlador.datos_basicos_service.listar_frecuencias_publicacion()
            
            estadisticas = {
                'total_anuncios': len(anuncios),
                'total_medios': len(medios),
                'total_tipos': len(tipos),
                'total_frecuencias': len(frecuencias),
                'precio_promedio': sum(a.precio for a in anuncios) / len(anuncios) if anuncios else 0,
                'precio_minimo': min(a.precio for a in anuncios) if anuncios else 0,
                'precio_maximo': max(a.precio for a in anuncios) if anuncios else 0
            }
            
            return {"exitoso": True, "datos": estadisticas}, 200
            
        except Exception as e:
            logger.error(f"Error al obtener estadísticas: {e}")
            return {"exitoso": False, "mensaje": f"Error interno: {str(e)}"}, 500
