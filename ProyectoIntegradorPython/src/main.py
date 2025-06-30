from db.conexion import conectar
from services.usuario_service import UsuarioService
from services.reserva_service import ReservaService
from datetime import datetime

def main():
    conectar()

    # Crear usuario
    usuario = UsuarioService.crear_usuario(nombre="Ana", email="ana@ejemplo.com")
    print(f"Usuario creado: {usuario}")

    # Crear reserva para ese usuario
    reserva = ReservaService.crear_reserva(usuario=usuario, fecha=datetime.now(), estado="confirmada")
    print(f"Reserva creada: {reserva}")

    # Listar reservas del usuario
    reservas = ReservaService.obtener_reservas_por_usuario(usuario)
    print(f"Reservas de {usuario.nombre}: {reservas}")

if __name__ == "__main__":
    main()