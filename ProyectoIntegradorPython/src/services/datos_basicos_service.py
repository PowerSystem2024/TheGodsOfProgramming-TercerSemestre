"""
Servicio para gestionar los datos básicos (medios, módulos, frecuencias)
"""
from src.models.medio_comunicacion import MedioComunicacion
from src.models.tipo_modulo import TipoModulo
from src.models.frecuencia_publicacion import FrecuenciaPublicacion

class DatosBasicosService:
    
    @staticmethod
    def inicializar_medios_comunicacion():
        """
        Inicializa los medios de comunicación en la base de datos si no existen
        """
        medios_nombres = [
            "El Norteño", "Del Sur", "Patagónico", 
            "Del Centro", "El Cuyano", "Del Litoral"
        ]
        
        medios_creados = []
        for nombre in medios_nombres:
            # Verificar si ya existe
            medio_existente = MedioComunicacion.objects(nombre=nombre).first()
            if not medio_existente:
                medio = MedioComunicacion(nombre=nombre)
                medio.save()
                medios_creados.append(medio)
                print(f"✅ Medio creado: {nombre}")
            else:
                medios_creados.append(medio_existente)
        
        return medios_creados
    
    @staticmethod
    def inicializar_tipos_modulos():
        """
        Inicializa los tipos de módulos en la base de datos si no existen
        """
        modulos_nombres = [
            "M1", "M2", "M3", "M4", "M6", "M8", "M12", "M16"
        ]
        
        modulos_creados = []
        for nombre in modulos_nombres:
            # Verificar si ya existe
            modulo_existente = TipoModulo.objects(nombre=nombre).first()
            if not modulo_existente:
                modulo = TipoModulo(nombre=nombre)
                modulo.save()
                modulos_creados.append(modulo)
                print(f"✅ Módulo creado: {nombre}")
            else:
                modulos_creados.append(modulo_existente)
        
        return modulos_creados
    
    @staticmethod
    def inicializar_frecuencias_publicacion():
        """
        Inicializa las frecuencias de publicación en la base de datos si no existen
        """
        frecuencias_nombres = [
            "D", "LAV", "SD", "1S", "2S", "3S", "1.15", "1.30"
        ]
        
        frecuencias_creadas = []
        for nombre in frecuencias_nombres:
            # Verificar si ya existe
            frecuencia_existente = FrecuenciaPublicacion.objects(nombre=nombre).first()
            if not frecuencia_existente:
                frecuencia = FrecuenciaPublicacion(nombre=nombre)
                frecuencia.save()
                frecuencias_creadas.append(frecuencia)
                print(f"✅ Frecuencia creada: {nombre}")
            else:
                frecuencias_creadas.append(frecuencia_existente)
        
        return frecuencias_creadas
    
    @staticmethod
    def obtener_todos_los_medios():
        """
        Obtiene todos los medios de comunicación de la base de datos
        """
        return list(MedioComunicacion.objects.all())
    
    @staticmethod
    def obtener_todos_los_modulos():
        """
        Obtiene todos los tipos de módulos de la base de datos
        """
        return list(TipoModulo.objects.all())
    
    @staticmethod
    def obtener_todas_las_frecuencias():
        """
        Obtiene todas las frecuencias de publicación de la base de datos
        """
        return list(FrecuenciaPublicacion.objects.all())
    
    @staticmethod
    def obtener_medio_comunicacion_por_id(medio_id):
        """
        Obtiene un medio de comunicación por su ID
        
        Args:
            medio_id (str): ID del medio de comunicación
            
        Returns:
            MedioComunicacion: El medio encontrado o None si no existe
        """
        try:
            return MedioComunicacion.objects(id=medio_id).first()
        except Exception:
            return None
    
    @staticmethod
    def obtener_tipo_modulo_por_id(tipo_id):
        """
        Obtiene un tipo de módulo por su ID
        
        Args:
            tipo_id (str): ID del tipo de módulo
            
        Returns:
            TipoModulo: El tipo encontrado o None si no existe
        """
        try:
            return TipoModulo.objects(id=tipo_id).first()
        except Exception:
            return None
    
    @staticmethod
    def obtener_frecuencia_publicacion_por_id(frecuencia_id):
        """
        Obtiene una frecuencia de publicación por su ID
        
        Args:
            frecuencia_id (str): ID de la frecuencia de publicación
            
        Returns:
            FrecuenciaPublicacion: La frecuencia encontrada o None si no existe
        """
        try:
            return FrecuenciaPublicacion.objects(id=frecuencia_id).first()
        except Exception:
            return None

    # Métodos alias para compatibilidad con la aplicación web
    @staticmethod
    def listar_medios_comunicacion():
        """Alias para obtener_todos_los_medios() - compatibilidad web"""
        return DatosBasicosService.obtener_todos_los_medios()
    
    @staticmethod
    def listar_tipos_modulo():
        """Alias para obtener_todos_los_modulos() - compatibilidad web"""
        return DatosBasicosService.obtener_todos_los_modulos()
    
    @staticmethod
    def listar_frecuencias_publicacion():
        """Alias para obtener_todas_las_frecuencias() - compatibilidad web"""
        return DatosBasicosService.obtener_todas_las_frecuencias()
