"""
Representa un tipo de módulo para un anuncio
"""
import mongoengine as me

class TipoModulo(me.Document):
    """
    Modelo de datos para tipos de módulos usando MongoDB
    """
    nombre = me.StringField(required=True, unique=True, max_length=50)
    
    # Configuración de la colección
    meta = {
        'collection': 'tipos_modulos',
        'indexes': ['nombre']
    }
    
    def __init__(self, nombre=None, *args, **kwargs):
        """
        Constructor de la clase TipoModulo.
        
        Args:
            nombre (str): El nombre del tipo de módulo.
        """
        super().__init__(*args, **kwargs)
        if nombre:
            self.nombre = nombre

    def get_nombre(self):
        """
        Obtiene el nombre del tipo de módulo.
        
        Returns:
            str: El nombre del tipo de módulo.
        """
        return self.nombre

    def set_nombre(self, nombre):
        """
        Establece el nombre del tipo de módulo.
        
        Args:
            nombre (str): El nuevo nombre del tipo de módulo.
        """
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"TipoModulo(nombre='{self.nombre}')"
