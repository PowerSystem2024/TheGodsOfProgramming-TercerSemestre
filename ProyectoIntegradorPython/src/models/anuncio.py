"""
Representa un anuncio publicitario
"""

from .medio_comunicacion import MedioComunicacion
from .tipo_modulo import TipoModulo
from .frecuencia_publicacion import FrecuenciaPublicacion

class Anuncio:
    def __init__(self, medio, modulo, frecuencia, precio, empresa):
        """
        Constructor de la clase Anuncio.
        
        Args:
            medio (MedioComunicacion): El medio de comunicación del anuncio.
            modulo (TipoModulo): El tipo de módulo del anuncio.
            frecuencia (FrecuenciaPublicacion): La frecuencia de publicación del anuncio.
            precio (float): El precio del anuncio.
            empresa (str): El nombre de la empresa del anuncio.
        """
        self.medio = medio
        self.modulo = modulo
        self.frecuencia = frecuencia
        self.precio = precio
        self.empresa = empresa

    def get_medio(self):
        """
        Obtiene el medio de comunicación del anuncio.
        
        Returns:
            MedioComunicacion: El medio de comunicación del anuncio.
        """
        return self.medio

    def set_medio(self, medio):
        """
        Establece el medio de comunicación del anuncio.
        
        Args:
            medio (MedioComunicacion): El nuevo medio de comunicación del anuncio.
        """
        self.medio = medio

    def get_modulo(self):
        """
        Obtiene el tipo de módulo del anuncio.
        
        Returns:
            TipoModulo: El tipo de módulo del anuncio.
        """
        return self.modulo

    def set_modulo(self, modulo):
        """
        Establece el tipo de módulo del anuncio.
        
        Args:
            modulo (TipoModulo): El nuevo tipo de módulo del anuncio.
        """
        self.modulo = modulo

    def get_frecuencia(self):
        """
        Obtiene la frecuencia de publicación del anuncio.
        
        Returns:
            FrecuenciaPublicacion: La frecuencia de publicación del anuncio.
        """
        return self.frecuencia

    def set_frecuencia(self, frecuencia):
        """
        Establece la frecuencia de publicación del anuncio.
        
        Args:
            frecuencia (FrecuenciaPublicacion): La nueva frecuencia de publicación del anuncio.
        """
        self.frecuencia = frecuencia

    def get_precio(self):
        """
        Obtiene el precio del anuncio.
        
        Returns:
            float: El precio del anuncio.
        """
        return self.precio

    def set_precio(self, precio):
        """
        Establece el precio del anuncio.
        
        Args:
            precio (float): El nuevo precio del anuncio.
        """
        self.precio = precio

    def get_empresa(self):
        """
        Obtiene el nombre de la empresa del anuncio.
        
        Returns:
            str: El nombre de la empresa del anuncio.
        """
        return self.empresa

    def set_empresa(self, empresa):
        """
        Establece el nombre de la empresa del anuncio.
        
        Args:
            empresa (str): El nuevo nombre de la empresa del anuncio.
        """
        self.empresa = empresa

    def __str__(self):
        return f"Anuncio: {self.empresa} - {self.medio.nombre} - {self.modulo.nombre} - {self.frecuencia.nombre} - ${self.precio}"
