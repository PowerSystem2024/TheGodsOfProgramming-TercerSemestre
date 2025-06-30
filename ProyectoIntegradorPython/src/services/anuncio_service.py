"""
Servicio para gestionar los anuncios publicitarios
"""
from models.anuncio import Anuncio
from models.medio_comunicacion import MedioComunicacion
from models.tipo_modulo import TipoModulo
from models.frecuencia_publicacion import FrecuenciaPublicacion

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
    
    @staticmethod
    def obtener_todos_los_anuncios():
        """
        Obtiene todos los anuncios activos de la base de datos
        
        Returns:
            list: Lista de anuncios
        """
        return list(Anuncio.objects(activo=True).all())
    
    @staticmethod
    def buscar_anuncios_por_empresa(nombre_empresa):
        """
        Busca anuncios por nombre de empresa (case-insensitive)
        
        Args:
            nombre_empresa (str): El nombre de la empresa a buscar
            
        Returns:
            list: Lista de anuncios encontrados
        """
        # Búsqueda case-insensitive usando regex
        return list(Anuncio.objects(
            empresa__iregex=f"^{nombre_empresa}$",
            activo=True
        ).all())
    
    @staticmethod
    def obtener_anuncio_por_id(anuncio_id):
        """
        Obtiene un anuncio por su ID
        
        Args:
            anuncio_id (str): El ID del anuncio
            
        Returns:
            Anuncio: El anuncio encontrado o None
        """
        try:
            return Anuncio.objects(id=anuncio_id, activo=True).first()
        except:
            return None
    
    @staticmethod
    def actualizar_anuncio(anuncio):
        """
        Actualiza un anuncio en la base de datos
        
        Args:
            anuncio (Anuncio): El anuncio a actualizar
            
        Returns:
            Anuncio: El anuncio actualizado
        """
        anuncio.save()
        return anuncio
    
    @staticmethod
    def actualizar_anuncio_por_id(anuncio_id, **kwargs):
        """
        Actualiza un anuncio por su ID con parámetros específicos
        
        Args:
            anuncio_id (str): ID del anuncio a actualizar
            **kwargs: Campos a actualizar (empresa, precio, etc.)
            
        Returns:
            Anuncio: El anuncio actualizado o None si no se encontró
        """
        try:
            anuncio = Anuncio.objects(id=anuncio_id, activo=True).first()
            if anuncio:
                for campo, valor in kwargs.items():
                    if hasattr(anuncio, campo):
                        setattr(anuncio, campo, valor)
                anuncio.save()
                return anuncio
            return None
        except Exception as e:
            print(f"❌ Error al actualizar anuncio: {e}")
            return None
    
    @staticmethod
    def eliminar_anuncio(anuncio_id):
        """
        Elimina un anuncio (marcado como inactivo)
        
        Args:
            anuncio_id (str): El ID del anuncio a eliminar
            
        Returns:
            bool: True si se eliminó exitosamente
        """
        try:
            anuncio = Anuncio.objects(id=anuncio_id).first()
            if anuncio:
                anuncio.activo = False
                anuncio.save()
                return True
            return False
        except:
            return False
    
    @staticmethod
    def calcular_ingresos_totales():
        """
        Calcula el total de ingresos de todos los anuncios activos
        
        Returns:
            float: Total de ingresos
        """
        anuncios = Anuncio.objects(activo=True).all()
        return sum(anuncio.precio for anuncio in anuncios)
    
    @staticmethod
    def inicializar_anuncios_prueba(medios, modulos, frecuencias):
        """
        Crea anuncios de prueba si la base de datos está vacía
        
        Args:
            medios (list): Lista de medios de comunicación
            modulos (list): Lista de tipos de módulos
            frecuencias (list): Lista de frecuencias de publicación
        """
        # Verificar si ya existen anuncios
        if Anuncio.objects(activo=True).count() > 0:
            print("✅ Ya existen anuncios en la base de datos")
            return
        
        # Datos de anuncios de prueba
        anuncios_prueba = [
            (medios[0], modulos[3], frecuencias[1], 2500.0, "Tech Solutions Inc."),
            (medios[1], modulos[1], frecuencias[0], 1800.0, "Innovate Corp."),
            (medios[2], modulos[5], frecuencias[6], 4300.0, "Global Industries Ltd."),
            (medios[3], modulos[0], frecuencias[2], 500.0, "Creative Designs Studio"),
            (medios[4], modulos[2], frecuencias[4], 1300.0, "Marketing Masters"),
            (medios[5], modulos[7], frecuencias[7], 1000.0, "Digital Dynamics"),
            (medios[0], modulos[4], frecuencias[3], 200.0, "Code Wizards"),
            (medios[1], modulos[6], frecuencias[5], 900.0, "Future Vision"),
            (medios[2], modulos[0], frecuencias[0], 2100.0, "Open Source Solutions"),
            (medios[3], modulos[2], frecuencias[1], 2100.0, "Web Dev Experts"),
            (medios[4], modulos[1], frecuencias[4], 2100.0, "Marketing Masters")
        ]
        
        anuncios_creados = []
        for medio, modulo, frecuencia, precio, empresa in anuncios_prueba:
            anuncio = AnuncioService.crear_anuncio(medio, modulo, frecuencia, precio, empresa)
            anuncios_creados.append(anuncio)
            print(f"✅ Anuncio creado: {empresa} - ${precio}")
        
        print(f"✅ {len(anuncios_creados)} anuncios de prueba creados")
        return anuncios_creados
