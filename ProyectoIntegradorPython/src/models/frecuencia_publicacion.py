"""
Representa una frecuencia de publicación para un anuncio
"""
import mongoengine as me

class FrecuenciaPublicacion(me.Document):
    """
    Modelo de datos para frecuencias de publicación usando MongoDB
    """
    nombre = me.StringField(required=True, unique=True, max_length=50)
    
    # Configuración de la colección
    meta = {
        'collection': 'frecuencias_publicacion',
        'indexes': ['nombre']
    }
    
    def __init__(self, nombre=None, *args, **kwargs):
        """
        Constructor de la clase FrecuenciaPublicacion.
        
        Args:
            nombre (str): El nombre de la frecuencia de publicación.
        """
        super().__init__(*args, **kwargs)
        if nombre:
            self.nombre = nombre

    def get_nombre(self):
        """
        Obtiene el nombre de la frecuencia de publicación.
        
        Returns:
            str: El nombre de la frecuencia de publicación.
        """
        return self.nombre

    def set_nombre(self, nombre):
        """
        Establece el nombre de la frecuencia de publicación.
        
        Args:
            nombre (str): El nuevo nombre de la frecuencia de publicación.
        """
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"FrecuenciaPublicacion(nombre='{self.nombre}')"
