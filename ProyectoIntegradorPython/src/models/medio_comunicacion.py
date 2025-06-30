"""
Representa un medio de comunicación donde se pueden publicar anuncios
"""

class MedioComunicacion:
    def __init__(self, nombre):
        """
        Constructor de la clase MedioComunicacion.
        
        Args:
            nombre (str): El nombre del medio de comunicación.
        """
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
