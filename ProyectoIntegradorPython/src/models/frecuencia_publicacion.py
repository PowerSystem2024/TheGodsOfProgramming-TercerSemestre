"""
Representa una frecuencia de publicación para un anuncio
"""

class FrecuenciaPublicacion:
    def __init__(self, nombre):
        """
        Constructor de la clase FrecuenciaPublicacion.
        
        Args:
            nombre (str): El nombre de la frecuencia de publicación.
        """
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
