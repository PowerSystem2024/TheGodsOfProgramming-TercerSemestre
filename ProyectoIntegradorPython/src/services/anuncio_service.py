"""
Servicio para gestionar los anuncios publicitarios
"""
from src.models.anuncio import Anuncio
from src.models.medio_comunicacion import MedioComunicacion
from src.models.tipo_modulo import TipoModulo
from src.models.frecuencia_publicacion import FrecuenciaPublicacion

class AnuncioService:
    
    @staticmethod
    def crear_anuncio(medio, modulo, frecuencia, precio, empresa):
        """
        Crea un nuevo anuncio en la base de datos
        
        Args:
            medio (MedioComunicacion): El medio de comunicación
            modulo (TipoModulo): El tipo de módulo
            frecuencia (FrecuenciaPublicacion): La frecuencia de publicación
            precio (float): El precio del anuncio
            empresa (str): El nombre de la empresa
            
        Returns:
            Anuncio: El anuncio creado
        """
        anuncio = Anuncio(
            medio=medio,
            modulo=modulo,
            frecuencia=frecuencia,
            precio=precio,
            empresa=empresa
        )
        anuncio.save()
        return anuncio
    
    # Método alias para compatibilidad con la aplicación web
    @staticmethod
    def listar_anuncios():
        """
        Alias para obtener_todos_los_anuncios() - compatibilidad web
        
        Returns:
            list: Lista de anuncios activos
        """
        return AnuncioService.obtener_todos_los_anuncios()
    
    @staticmethod
    def obtener_todos_los_anuncios():
        """
        Obtiene todos los anuncios activos de la base de datos
        
        Returns:
            list: Lista de anuncios
        """
        return list(Anuncio.objects(activo=True).all())
    
    # Método para búsqueda avanzada web
    @staticmethod
    def buscar_anuncios(criterios):
        """
        Busca anuncios según criterios múltiples (para aplicación web)
        
        Args:
            criterios (dict): Diccionario con criterios de búsqueda
            
        Returns:
            list: Lista de anuncios que cumplen los criterios
        """
        query = Anuncio.objects(activo=True)
        
        if 'termino' in criterios and criterios['termino']:
            # Búsqueda por término en empresa
            query = query.filter(empresa__icontains=criterios['termino'])
            
        if 'medio_comunicacion_id' in criterios and criterios['medio_comunicacion_id']:
            query = query.filter(medio=criterios['medio_comunicacion_id'])
            
        if 'tipo_modulo_id' in criterios and criterios['tipo_modulo_id']:
            query = query.filter(modulo=criterios['tipo_modulo_id'])
            
        if 'precio_min' in criterios and criterios['precio_min'] is not None:
            query = query.filter(precio__gte=criterios['precio_min'])
            
        if 'precio_max' in criterios and criterios['precio_max'] is not None:
            query = query.filter(precio__lte=criterios['precio_max'])
            
        return list(query.all())
    
    # Método para crear anuncio desde formulario web
    @staticmethod
    def crear_anuncio_web(datos_anuncio):
        """
        Crea un anuncio desde formulario web
        
        Args:
            datos_anuncio (dict): Datos del formulario web
            
        Returns:
            dict: Resultado de la operación
        """
        try:
            # Obtener objetos de referencias
            medio = MedioComunicacion.objects.get(id=datos_anuncio['medio_comunicacion_id'])
            modulo = TipoModulo.objects.get(id=datos_anuncio['tipo_modulo_id'])
            frecuencia = FrecuenciaPublicacion.objects.get(id=datos_anuncio['frecuencia_publicacion_id'])
            
            # Crear anuncio con datos adicionales para web
            anuncio = Anuncio(
                codigo=datos_anuncio['codigo'],
                nombre_producto=datos_anuncio['nombre_producto'],
                slogan=datos_anuncio.get('slogan', ''),
                descripcion=datos_anuncio.get('descripcion', ''),
                medio=medio,
                modulo=modulo,
                frecuencia=frecuencia,
                precio=datos_anuncio['precio'],
                empresa=datos_anuncio['codigo']  # Usar código como empresa por compatibilidad
            )
            anuncio.save()
            
            return {
                'exitoso': True,
                'anuncio': anuncio,
                'mensaje': 'Anuncio creado exitosamente'
            }
            
        except Exception as e:
            return {
                'exitoso': False,
                'mensaje': f'Error al crear anuncio: {str(e)}'
            }
    
    # Método para actualizar anuncio desde web
    @staticmethod
    def actualizar_anuncio_web(anuncio_id, datos_anuncio):
        """
        Actualiza un anuncio desde formulario web
        
        Args:
            anuncio_id (str): ID del anuncio
            datos_anuncio (dict): Datos actualizados
            
        Returns:
            dict: Resultado de la operación
        """
        try:
            anuncio = Anuncio.objects.get(id=anuncio_id, activo=True)
            
            # Actualizar campos
            anuncio.codigo = datos_anuncio['codigo']
            anuncio.nombre_producto = datos_anuncio['nombre_producto']
            anuncio.slogan = datos_anuncio.get('slogan', '')
            anuncio.descripcion = datos_anuncio.get('descripcion', '')
            anuncio.precio = datos_anuncio['precio']
            anuncio.empresa = datos_anuncio['codigo']  # Usar código como empresa
            
            # Actualizar referencias
            if 'medio_comunicacion_id' in datos_anuncio:
                anuncio.medio = MedioComunicacion.objects.get(id=datos_anuncio['medio_comunicacion_id'])
            if 'tipo_modulo_id' in datos_anuncio:
                anuncio.modulo = TipoModulo.objects.get(id=datos_anuncio['tipo_modulo_id'])
            if 'frecuencia_publicacion_id' in datos_anuncio:
                anuncio.frecuencia = FrecuenciaPublicacion.objects.get(id=datos_anuncio['frecuencia_publicacion_id'])
                
            anuncio.save()
            
            return {
                'exitoso': True,
                'anuncio': anuncio,
                'mensaje': 'Anuncio actualizado exitosamente'
            }
            
        except Anuncio.DoesNotExist:
            return {
                'exitoso': False,
                'mensaje': 'Anuncio no encontrado'
            }
        except Exception as e:
            return {
                'exitoso': False,
                'mensaje': f'Error al actualizar anuncio: {str(e)}'
            }
    
    # Método para eliminar anuncio (lógicamente)
    @staticmethod
    def eliminar_anuncio_web(anuncio_id):
        """
        Elimina un anuncio (marcado como inactivo)
        
        Args:
            anuncio_id (str): ID del anuncio
            
        Returns:
            dict: Resultado de la operación
        """
        try:
            anuncio = Anuncio.objects.get(id=anuncio_id, activo=True)
            anuncio.activo = False
            anuncio.save()
            
            return {
                'exitoso': True,
                'mensaje': 'Anuncio eliminado exitosamente'
            }
            
        except Anuncio.DoesNotExist:
            return {
                'exitoso': False,
                'mensaje': 'Anuncio no encontrado'
            }
        except Exception as e:
            return {
                'exitoso': False,
                'mensaje': f'Error al eliminar anuncio: {str(e)}'
            }
    
    # Método para generar matriz de precios
    @staticmethod
    def generar_matriz_precios():
        """
        Genera matriz de análisis de precios por medio y tipo de módulo
        
        Returns:
            dict: Matriz organizada por medio -> tipo -> estadísticas
        """
        anuncios = Anuncio.objects(activo=True).all()
        matriz = {}
        
        for anuncio in anuncios:
            if not anuncio.medio or not anuncio.modulo:
                continue
                
            medio_nombre = anuncio.medio.nombre
            modulo_nombre = anuncio.modulo.nombre
            
            if medio_nombre not in matriz:
                matriz[medio_nombre] = {}
            
            if modulo_nombre not in matriz[medio_nombre]:
                matriz[medio_nombre][modulo_nombre] = {
                    'precios': [],
                    'cantidad': 0,
                    'promedio': 0,
                    'minimo': 0,
                    'maximo': 0
                }
            
            matriz[medio_nombre][modulo_nombre]['precios'].append(anuncio.precio)
            matriz[medio_nombre][modulo_nombre]['cantidad'] += 1
        
        # Calcular estadísticas
        for medio in matriz:
            for modulo in matriz[medio]:
                precios = matriz[medio][modulo]['precios']
                if precios:
                    matriz[medio][modulo]['promedio'] = sum(precios) / len(precios)
                    matriz[medio][modulo]['minimo'] = min(precios)
                    matriz[medio][modulo]['maximo'] = max(precios)
        
        return matriz
