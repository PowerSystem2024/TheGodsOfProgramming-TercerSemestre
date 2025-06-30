import mongoengine as me

def conectar():
    # Cambia según tu conexión de MongoDB Compass
    me.connect(
        db="proyectointegrador",
        host="mongodb://localhost:27017/proyectointegrador"
    )