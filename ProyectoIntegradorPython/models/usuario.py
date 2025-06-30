import mongoengine as me

class Usuario(me.Document):
    nombre = me.StringField(required=True)
    email = me.StringField(required=True, unique=True)
    activo = me.BooleanField(default=True)