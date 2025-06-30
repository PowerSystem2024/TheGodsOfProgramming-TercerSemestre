"""
Representa un medio de comunicación donde se pueden publicar anuncios
"""
import mongoengine as me

class MedioComunicacion(me.Document):
    """
    Modelo de datos para medios de comunicación usando MongoDB
    """
    nombre = me.StringField(required=True, unique=True, max_length=100)
    
    # Configuración de la colección
    meta = {
        'collection': 'medios_comunicacion',
        'indexes': ['nombre']
    }
    
    def __init__(self, nombre=None, *args, **kwargs):
        """
        Constructor de la clase MedioComunicacion.
        
        Args:
            nombre (str): El nombre del medio de comunicación.
        """
        super().__init__(*args, **kwargs)
        if nombre:
            self.nombre = nombre

    def get_nombre(self):
        """
        Obtiene el nombre del medio de comunicación.
        
        Returns:
            str: El nombre del medio de comunicación.
        """
        return self.nombre

    def set_nombre(self, nombre):
        """
        Establece el nombre del medio de comunicación.
        
        Args:
            nombre (str): El nuevo nombre del medio de comunicación.
        """
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"MedioComunicacion(nombre='{self.nombre}')"
