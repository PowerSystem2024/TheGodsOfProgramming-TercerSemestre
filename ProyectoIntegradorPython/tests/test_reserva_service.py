import pytest
from services.reserva_service import ReservaService
from services.usuario_service import UsuarioService
from models.reserva import Reserva
from datetime import datetime

def test_crear_reserva():
    usuario = UsuarioService.crear_usuario("Laura", "laura@ejemplo.com")
    reserva = ReservaService.crear_reserva(usuario, datetime(2025, 1, 1), "nueva")
    assert reserva.usuario == usuario
    assert reserva.estado == "nueva"
    # Limpieza
    reserva.delete()
    usuario.delete()

def test_obtener_reservas_por_usuario():
    usuario = UsuarioService.crear_usuario("Pepe", "pepe@ejemplo.com")
    reserva = ReservaService.crear_reserva(usuario, datetime(2025, 1, 1), "pendiente")
    reservas = ReservaService.obtener_reservas_por_usuario(usuario)
    assert len(reservas) >= 1
    # Limpieza
    reserva.delete()
    usuario.delete()