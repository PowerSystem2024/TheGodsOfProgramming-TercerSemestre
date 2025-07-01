"""
Representa un anuncio publicitario
"""
import mongoengine as me
from datetime import datetime
from .medio_comunicacion import MedioComunicacion
from .tipo_modulo import TipoModulo
from .frecuencia_publicacion import FrecuenciaPublicacion

class Anuncio(me.Document):
    """
    Modelo de datos para anuncios publicitarios usando MongoDB
    """
    medio = me.ReferenceField(MedioComunicacion, required=True)
    modulo = me.ReferenceField(TipoModulo, required=True)
    frecuencia = me.ReferenceField(FrecuenciaPublicacion, required=True)
    precio = me.FloatField(required=True, min_value=0)
    empresa = me.StringField(required=True, max_length=200)
    fecha_creacion = me.DateTimeField(default=datetime.utcnow)
    activo = me.BooleanField(default=True)
    
    # Configuración de la colección
    meta = {
        'collection': 'anuncios',
        'indexes': [
            'empresa',
            'fecha_creacion',
            'activo',
            ('medio', 'modulo', 'frecuencia')  # Índice compuesto
        ]
    }
    
    def calcular_precio(self):
        """
        Calcula el precio del anuncio basado en el medio, módulo y frecuencia
        
        Returns:
            float: El precio calculado del anuncio
        """
        # Precios base por medio de comunicación
        precios_medios = {
            'Televisión': 15000.0,
            'Radio': 8000.0,
            'Diario': 5000.0,
            'Revista': 7000.0,
            'Internet': 3000.0
        }
        
        # Multiplicadores por tipo de módulo
        multiplicadores_modulo = {
            'Página Completa': 2.0,
            'Media Página': 1.0,
            'Cuarto de Página': 0.5,
            'Banner': 0.3,
            'Spot 30 segundos': 1.0,
            'Spot 60 segundos': 1.8
        }
        
        # Multiplicadores por frecuencia
        multiplicadores_frecuencia = {
            'Diaria': 1.0,
            'Semanal': 0.8,
            'Quincenal': 0.6,
            'Mensual': 0.4
        }
        
        try:
            precio_base = precios_medios.get(self.medio.nombre, 5000.0)
            mult_modulo = multiplicadores_modulo.get(self.modulo.nombre, 1.0)
            mult_frecuencia = multiplicadores_frecuencia.get(self.frecuencia.nombre, 1.0)
            
            precio_calculado = precio_base * mult_modulo * mult_frecuencia
            return round(precio_calculado, 2)
            
        except AttributeError:
            # Si hay algún problema con las referencias, devolver precio por defecto
            return 5000.0
    
    def __init__(self, medio=None, modulo=None, frecuencia=None, precio=None, empresa=None, *args, **kwargs):
        """
        Constructor de la clase Anuncio.
        
        Args:
            medio (MedioComunicacion): El medio de comunicación del anuncio.
            modulo (TipoModulo): El tipo de módulo del anuncio.
            frecuencia (FrecuenciaPublicacion): La frecuencia de publicación del anuncio.
            precio (float, optional): El precio del anuncio. Si no se proporciona, se calcula automáticamente.
            empresa (str): El nombre de la empresa del anuncio.
        """
        super().__init__(*args, **kwargs)
        if medio:
            self.medio = medio
        if modulo:
            self.modulo = modulo
        if frecuencia:
            self.frecuencia = frecuencia
        if empresa:
            self.empresa = empresa
        
        # Calcular precio automáticamente si no se proporciona
        if precio is not None:
            self.precio = precio
        elif self.medio and self.modulo and self.frecuencia:
            self.precio = self.calcular_precio()
        else:
            self.precio = 0.0  # Valor por defecto

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
        return f"Anuncio: {self.empresa} - {self.medio.nombre if self.medio else 'N/A'} - {self.modulo.nombre if self.modulo else 'N/A'} - {self.frecuencia.nombre if self.frecuencia else 'N/A'} - ${self.precio}"
    
    def __repr__(self):
        return f"Anuncio(empresa='{self.empresa}', precio={self.precio})"
