from services.usuario_service import UsuarioService
from services.reserva_service import ReservaService
from models.usuario import Usuario
from models.reserva import Reserva
from datetime import datetime

def test_flujo_completo():
    # Crear usuario
    usuario = UsuarioService.crear_usuario("TestIntegracion", "integracion@ejemplo.com")
    assert usuario.id is not None

    # Crear reserva para usuario
    reserva = ReservaService.crear_reserva(usuario, datetime(2026, 1, 1), "nueva")
    assert reserva.id is not None
    assert reserva.usuario == usuario

    # Consultar reservas para usuario
    reservas = ReservaService.obtener_reservas_por_usuario(usuario)
    assert any(r.id == reserva.id for r in reservas)

    # Limpieza
    reserva.delete()
    usuario.delete()