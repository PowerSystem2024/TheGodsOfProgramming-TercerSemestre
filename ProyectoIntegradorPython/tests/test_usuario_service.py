import pytest
from services.usuario_service import UsuarioService
from models.usuario import Usuario

def test_crear_usuario():
    usuario = UsuarioService.crear_usuario("Carlos", "carlos@ejemplo.com")
    assert usuario.nombre == "Carlos"
    assert usuario.email == "carlos@ejemplo.com"
    assert usuario.activo
    # Limpieza
    usuario.delete()

def test_obtener_usuario_por_email():
    u = UsuarioService.crear_usuario("Elena", "elena@ejemplo.com")
    usuario = UsuarioService.obtener_usuario_por_email("elena@ejemplo.com")
    assert usuario is not None
    assert usuario.nombre == "Elena"
    # Limpieza
    usuario.delete()

def test_listar_usuarios():
    u1 = UsuarioService.crear_usuario("A", "a@mail.com")
    u2 = UsuarioService.crear_usuario("B", "b@mail.com")
    usuarios = UsuarioService.listar_usuarios()
    emails = [u.email for u in usuarios]
    assert "a@mail.com" in emails and "b@mail.com" in emails
    # Limpieza
    u1.delete()
    u2.delete()