import mongoengine as me
from datetime import datetime

class Reserva(me.Document):
    usuario = me.ReferenceField(Usuario, required=True)
    fecha = me.DateTimeField(default=datetime.utcnow)
    estado = me.StringField(required=True)