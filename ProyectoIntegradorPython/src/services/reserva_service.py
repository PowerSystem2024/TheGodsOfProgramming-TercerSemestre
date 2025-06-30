from models.reserva import Reserva
from models.usuario import Usuario
from datetime import datetime

class ReservaService:
    @staticmethod
    def crear_reserva(usuario: Usuario, fecha: datetime, estado: str) -> Reserva:
        reserva = Reserva(usuario=usuario, fecha=fecha, estado=estado)
        reserva.save()
        return reserva

    @staticmethod
    def obtener_reservas_por_usuario(usuario: Usuario) -> list[Reserva]:
        return list(Reserva.objects(usuario=usuario))

    @staticmethod
    def listar_reservas() -> list[Reserva]:
        return list(Reserva.objects())