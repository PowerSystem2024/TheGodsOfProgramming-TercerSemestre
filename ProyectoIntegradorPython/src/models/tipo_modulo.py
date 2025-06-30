"""
Representa un tipo de módulo para un anuncio
"""

class TipoModulo:
    def __init__(self, nombre):
        """
        Constructor de la clase TipoModulo.
        
        Args:
            nombre (str): El nombre del tipo de módulo.
        """
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
