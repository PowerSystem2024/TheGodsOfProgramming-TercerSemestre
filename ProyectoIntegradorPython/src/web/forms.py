"""
Formularios web para la aplicación Flask
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length, Optional
from wtforms.widgets import TextArea

class AnuncioForm(FlaskForm):
    """Formulario para crear/editar anuncios"""
    empresa = StringField('Empresa', validators=[DataRequired(), Length(min=2, max=200)])
    
    # Campos que se llenarán dinámicamente
    medio_comunicacion = SelectField('Medio de Comunicación', choices=[], validators=[DataRequired()])
    tipo_modulo = SelectField('Tipo de Módulo', choices=[], validators=[DataRequired()])
    frecuencia_publicacion = SelectField('Frecuencia de Publicación', choices=[], validators=[DataRequired()])
    
    submit = SubmitField('Guardar Anuncio')

class BusquedaForm(FlaskForm):
    """Formulario para búsqueda de anuncios"""
    termino = StringField('Término de Búsqueda', validators=[Optional(), Length(max=200)])
    medio_comunicacion = SelectField('Medio de Comunicación', choices=[('', 'Todos')], validators=[Optional()])
    tipo_modulo = SelectField('Tipo de Módulo', choices=[('', 'Todos')], validators=[Optional()])
    precio_min = FloatField('Precio Mínimo', validators=[Optional(), NumberRange(min=0)])
    precio_max = FloatField('Precio Máximo', validators=[Optional(), NumberRange(min=0)])
    
    submit = SubmitField('Buscar')

class MedioComunicacionForm(FlaskForm):
    """Formulario para gestionar medios de comunicación"""
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=100)])
    descripcion = TextAreaField('Descripción', validators=[Optional(), Length(max=500)])
    activo = SelectField('Estado', choices=[('True', 'Activo'), ('False', 'Inactivo')], validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class TipoModuloForm(FlaskForm):
    """Formulario para gestionar tipos de módulo"""
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=100)])
    descripcion = TextAreaField('Descripción', validators=[Optional(), Length(max=500)])
    activo = SelectField('Estado', choices=[('True', 'Activo'), ('False', 'Inactivo')], validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class FrecuenciaPublicacionForm(FlaskForm):
    """Formulario para gestionar frecuencias de publicación"""
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=100)])
    descripcion = TextAreaField('Descripción', validators=[Optional(), Length(max=500)])
    activo = SelectField('Estado', choices=[('True', 'Activo'), ('False', 'Inactivo')], validators=[DataRequired()])
    
    submit = SubmitField('Guardar')
