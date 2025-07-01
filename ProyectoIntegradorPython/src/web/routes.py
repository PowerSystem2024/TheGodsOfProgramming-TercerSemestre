"""
Rutas web para la aplicación Flask
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
from src.controllers.controlador_principal import ControladorPrincipal
from src.web.forms import AnuncioForm, BusquedaForm, MedioComunicacionForm, TipoModuloForm, FrecuenciaPublicacionForm
import logging

logger = logging.getLogger(__name__)

def register_routes(app):
    """Registra todas las rutas de la aplicación"""
    
    # Inicializar controlador una sola vez
    try:
        controlador = ControladorPrincipal()
        logger.info("Controlador inicializado correctamente")
    except Exception as e:
        logger.error(f"Error crítico al inicializar controlador: {e}")
        # Crear un controlador básico sin servicios para mostrar errores
        controlador = None
    
    def verificar_controlador():
        """Verifica que el controlador esté disponible"""
        if controlador is None:
            flash("Error: Sistema no disponible. Verifica la conexión a MongoDB.", 'error')
            return False
        return True
    
    @app.route('/')
    def index():
        """Página principal"""
        try:
            if not verificar_controlador():
                return render_template('index.html', stats={'total_anuncios': 0, 'anuncios_recientes': []})
                
            # Obtener estadísticas básicas
            anuncios = controlador.anuncio_service.listar_anuncios()
            stats = {
                'total_anuncios': len(anuncios),
                'anuncios_recientes': anuncios[:5] if anuncios else []
            }
            return render_template('index.html', stats=stats)
        except Exception as e:
            logger.error(f"Error en página principal: {e}")
            flash(f"Error al cargar la página: {str(e)}", 'error')
            return render_template('index.html', stats={'total_anuncios': 0, 'anuncios_recientes': []})
    
    @app.route('/anuncios')
    def listar_anuncios():
        """Lista todos los anuncios"""
        try:
            if not verificar_controlador():
                return render_template('anuncios/listar.html', anuncios=[], form=BusquedaForm())
                
            form = BusquedaForm()
            anuncios = controlador.anuncio_service.listar_anuncios()
            
            # Llenar opciones del formulario
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            
            form.medio_comunicacion.choices = [('', 'Todos')] + [(m.id, m.nombre) for m in medios]
            form.tipo_modulo.choices = [('', 'Todos')] + [(t.id, t.nombre) for t in tipos]
            
            return render_template('anuncios/listar.html', anuncios=anuncios, form=form)
        except Exception as e:
            logger.error(f"Error al listar anuncios: {e}")
            flash(f"Error al cargar anuncios: {str(e)}", 'error')
            return render_template('anuncios/listar.html', anuncios=[], form=BusquedaForm())
    
    @app.route('/anuncios/buscar', methods=['POST'])
    def buscar_anuncios():
        """Busca anuncios según criterios"""
        try:
            if not verificar_controlador():
                return redirect(url_for('listar_anuncios'))
                
            form = BusquedaForm()
            
            # Llenar opciones del formulario
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            
            form.medio_comunicacion.choices = [('', 'Todos')] + [(m.id, m.nombre) for m in medios]
            form.tipo_modulo.choices = [('', 'Todos')] + [(t.id, t.nombre) for t in tipos]
            
            if form.validate_on_submit():
                criterios = {}
                
                if form.termino.data:
                    criterios['termino'] = form.termino.data
                if form.medio_comunicacion.data:
                    criterios['medio_comunicacion_id'] = form.medio_comunicacion.data
                if form.tipo_modulo.data:
                    criterios['tipo_modulo_id'] = form.tipo_modulo.data
                if form.precio_min.data is not None:
                    criterios['precio_min'] = form.precio_min.data
                if form.precio_max.data is not None:
                    criterios['precio_max'] = form.precio_max.data
                
                anuncios = controlador.anuncio_service.buscar_anuncios(criterios)
                flash(f"Se encontraron {len(anuncios)} anuncio(s)", 'success')
                
                return render_template('anuncios/listar.html', anuncios=anuncios, form=form)
            
            # Si el formulario no es válido, mostrar errores
            anuncios = controlador.anuncio_service.listar_anuncios()
            return render_template('anuncios/listar.html', anuncios=anuncios, form=form)
            
        except Exception as e:
            logger.error(f"Error en búsqueda: {e}")
            flash(f"Error en la búsqueda: {str(e)}", 'error')
            return redirect(url_for('listar_anuncios'))
    
    @app.route('/anuncios/nuevo', methods=['GET', 'POST'])
    def crear_anuncio():
        """Crea un nuevo anuncio"""
        try:
            if not verificar_controlador():
                return redirect(url_for('listar_anuncios'))
                
            form = AnuncioForm()
            
            # Llenar opciones del formulario
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            frecuencias = controlador.datos_basicos_service.listar_frecuencias_publicacion()
            
            form.medio_comunicacion.choices = [(m.id, m.nombre) for m in medios]
            form.tipo_modulo.choices = [(t.id, t.nombre) for t in tipos]
            form.frecuencia_publicacion.choices = [(f.id, f.nombre) for f in frecuencias]
            
            if form.validate_on_submit():
                try:
                    # Obtener objetos de la base de datos
                    medio = controlador.datos_basicos_service.obtener_medio_comunicacion_por_id(form.medio_comunicacion.data)
                    tipo = controlador.datos_basicos_service.obtener_tipo_modulo_por_id(form.tipo_modulo.data)
                    frecuencia = controlador.datos_basicos_service.obtener_frecuencia_publicacion_por_id(form.frecuencia_publicacion.data)
                    
                    if not all([medio, tipo, frecuencia]):
                        flash('Error: Datos de referencia no válidos', 'error')
                        return render_template('anuncios/crear.html', form=form)
                    
                    # Crear anuncio con precio automático
                    anuncio = controlador.anuncio_service.crear_anuncio_simple(
                        medio=medio,
                        modulo=tipo,
                        frecuencia=frecuencia,
                        empresa=form.empresa.data
                    )
                    
                    flash(f'Anuncio creado exitosamente con precio automático: ${anuncio.precio:,.2f}', 'success')
                    return redirect(url_for('listar_anuncios'))
                    
                except Exception as e:
                    logger.error(f"Error al crear anuncio: {e}")
                    flash(f"Error al crear anuncio: {str(e)}", 'error')
            
            return render_template('anuncios/crear.html', form=form)
            
        except Exception as e:
            logger.error(f"Error al crear anuncio: {e}")
            flash(f"Error al crear anuncio: {str(e)}", 'error')
            return redirect(url_for('listar_anuncios'))
    
    @app.route('/anuncios/<anuncio_id>')
    def ver_anuncio(anuncio_id):
        """Muestra detalles de un anuncio"""
        try:
            if not verificar_controlador():
                return redirect(url_for('listar_anuncios'))
                
            anuncio = controlador.anuncio_service.obtener_anuncio_por_id(anuncio_id)
            if not anuncio:
                flash('Anuncio no encontrado', 'error')
                return redirect(url_for('listar_anuncios'))
            
            return render_template('anuncios/detalle.html', anuncio=anuncio)
            
        except Exception as e:
            logger.error(f"Error al ver anuncio: {e}")
            flash(f"Error al cargar anuncio: {str(e)}", 'error')
            return redirect(url_for('listar_anuncios'))
    
    @app.route('/anuncios/<anuncio_id>/editar', methods=['GET', 'POST'])
    def editar_anuncio(anuncio_id):
        """Edita un anuncio existente"""
        try:
            anuncio = controlador.anuncio_service.obtener_anuncio_por_id(anuncio_id)
            if not anuncio:
                flash('Anuncio no encontrado', 'error')
                return redirect(url_for('listar_anuncios'))
            
            form = AnuncioForm()
            
            # Llenar opciones del formulario
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            frecuencias = controlador.datos_basicos_service.listar_frecuencias_publicacion()
            
            form.medio_comunicacion.choices = [(m.id, m.nombre) for m in medios]
            form.tipo_modulo.choices = [(t.id, t.nombre) for t in tipos]
            form.frecuencia_publicacion.choices = [(f.id, f.nombre) for f in frecuencias]
            
            # Pre-llenar el formulario con datos actuales
            if request.method == 'GET':
                form.empresa.data = anuncio.empresa
                form.medio_comunicacion.data = str(anuncio.medio.id)
                form.tipo_modulo.data = str(anuncio.modulo.id)
                form.frecuencia_publicacion.data = str(anuncio.frecuencia.id)
            
            if form.validate_on_submit():
                try:
                    # Obtener objetos de la base de datos
                    medio = controlador.datos_basicos_service.obtener_medio_comunicacion_por_id(form.medio_comunicacion.data)
                    tipo = controlador.datos_basicos_service.obtener_tipo_modulo_por_id(form.tipo_modulo.data)
                    frecuencia = controlador.datos_basicos_service.obtener_frecuencia_publicacion_por_id(form.frecuencia_publicacion.data)
                    
                    if not all([medio, tipo, frecuencia]):
                        flash('Error: Datos de referencia no válidos', 'error')
                        return render_template('anuncios/editar.html', form=form, anuncio=anuncio)
                    
                    # Actualizar anuncio con recálculo de precio
                    anuncio.empresa = form.empresa.data
                    anuncio.medio = medio
                    anuncio.modulo = tipo
                    anuncio.frecuencia = frecuencia
                    anuncio.precio = anuncio.calcular_precio()  # Recalcular precio
                    anuncio.save()
                    
                    flash(f'Anuncio actualizado exitosamente. Nuevo precio: ${anuncio.precio:,.2f}', 'success')
                    return redirect(url_for('ver_anuncio', anuncio_id=anuncio_id))
                    
                except Exception as e:
                    logger.error(f"Error al actualizar anuncio: {e}")
                    flash(f"Error al actualizar anuncio: {str(e)}", 'error')
            
            return render_template('anuncios/editar.html', form=form, anuncio=anuncio)
            
        except Exception as e:
            logger.error(f"Error al editar anuncio: {e}")
            flash(f"Error al editar anuncio: {str(e)}", 'error')
            return redirect(url_for('listar_anuncios'))
    
    @app.route('/anuncios/<anuncio_id>/eliminar', methods=['POST'])
    def eliminar_anuncio(anuncio_id):
        """Elimina un anuncio"""
        try:
            resultado = controlador.anuncio_service.eliminar_anuncio_web(anuncio_id)
            
            if resultado['exitoso']:
                flash('Anuncio eliminado exitosamente', 'success')
            else:
                flash(f"Error al eliminar anuncio: {resultado['mensaje']}", 'error')
                
        except Exception as e:
            logger.error(f"Error al eliminar anuncio: {e}")
            flash(f"Error al eliminar anuncio: {str(e)}", 'error')
        
        return redirect(url_for('listar_anuncios'))
    
    @app.route('/matriz-precios')
    def matriz_precios():
        """Muestra la matriz de precios"""
        try:
            matriz = controlador.anuncio_service.generar_matriz_precios()
            return render_template('reportes/matriz_precios.html', matriz=matriz)
            
        except Exception as e:
            logger.error(f"Error en matriz de precios: {e}")
            flash(f"Error al generar matriz de precios: {str(e)}", 'error')
            return render_template('reportes/matriz_precios.html', matriz={})
    
    # Rutas para gestión de datos básicos
    @app.route('/configuracion')
    def configuracion():
        """Página de configuración"""
        return render_template('configuracion/index.html')
    
    @app.route('/configuracion/medios')
    def listar_medios():
        """Lista medios de comunicación"""
        try:
            medios = controlador.datos_basicos_service.listar_medios_comunicacion()
            return render_template('configuracion/medios.html', medios=medios)
        except Exception as e:
            logger.error(f"Error al listar medios: {e}")
            flash(f"Error al cargar medios: {str(e)}", 'error')
            return render_template('configuracion/medios.html', medios=[])
    
    @app.route('/configuracion/tipos')
    def listar_tipos():
        """Lista tipos de módulo"""
        try:
            tipos = controlador.datos_basicos_service.listar_tipos_modulo()
            return render_template('configuracion/tipos.html', tipos=tipos)
        except Exception as e:
            logger.error(f"Error al listar tipos: {e}")
            flash(f"Error al cargar tipos: {str(e)}", 'error')
            return render_template('configuracion/tipos.html', tipos=[])
    
    @app.route('/configuracion/frecuencias')
    def listar_frecuencias():
        """Lista frecuencias de publicación"""
        try:
            frecuencias = controlador.datos_basicos_service.listar_frecuencias_publicacion()
            return render_template('configuracion/frecuencias.html', frecuencias=frecuencias)
        except Exception as e:
            logger.error(f"Error al listar frecuencias: {e}")
            flash(f"Error al cargar frecuencias: {str(e)}", 'error')
            return render_template('configuracion/frecuencias.html', frecuencias=[])
    
    # Manejar errores
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500
