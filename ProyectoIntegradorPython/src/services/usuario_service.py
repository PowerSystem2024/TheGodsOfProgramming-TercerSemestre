from models.usuario import Usuario

class UsuarioService:
    @staticmethod
    def crear_usuario(nombre: str, email: str, activo: bool = True) -> Usuario:
        usuario = Usuario(nombre=nombre, email=email, activo=activo)
        usuario.save()
        return usuario

    @staticmethod
    def obtener_usuario_por_email(email: str) -> Usuario | None:
        return Usuario.objects(email=email).first()

    @staticmethod
    def listar_usuarios() -> list[Usuario]:
        return list(Usuario.objects())