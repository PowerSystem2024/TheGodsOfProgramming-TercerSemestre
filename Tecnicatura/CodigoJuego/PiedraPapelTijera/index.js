// Variables globales
let victoriasJugador = 0;
let victoriasPc = 0;
let partidasJugadas = 0;
const maxPartidas = 3;

function funcNumeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function jugar(eleccionJugador) {
    if (partidasJugadas >= maxPartidas) {
        mostrarModal("¡Ya se jugaron las 3 partidas! Reinicia para volver a jugar.");
        return;
    }

    const pc = funcNumeroAleatorio(1, 3);
    let mensaje = "";

    let eleccionTexto = ["", "piedra", "papel", "tijera"];
    mostrarModal("Elegiste " + eleccionTexto[eleccionJugador] + "\nLa computadora eligió " + eleccionTexto[pc], [
        {texto: "Continuar", accion: () => {
            cerrarModal();
            // Combate
            if (eleccionJugador === pc) {
                mensaje = "EMPATE";
            } else if (
                (eleccionJugador === 1 && pc === 3) ||
                (eleccionJugador === 2 && pc === 1) ||
                (eleccionJugador === 3 && pc === 2)
            ) {
                mensaje = "¡GANASTE!";
                victoriasJugador++;
            } else {
                mensaje = "PERDISTE";
                victoriasPc++;
            }

            partidasJugadas++;
            actualizarTanteador();

            if (partidasJugadas >= maxPartidas) {
                mensaje += "\n\nJuego terminado.\nMarcador final:\nJugador: " + victoriasJugador + "\nComputadora: " + victoriasPc;
                if (victoriasJugador > victoriasPc) {
                    mensaje += "\n¡Felicidades, ganaste la serie!";
                } else if (victoriasJugador < victoriasPc) {
                    mensaje += "\nLa computadora ganó la serie.";
                } else {
                    mensaje += "\n¡Empate en la serie!";
                }
                mostrarModal(mensaje, [
                    {texto: "Reiniciar", accion: () => { cerrarModal(); reiniciar(); }},
                    {texto: "Cerrar", accion: cerrarModal}
                ]);
            } else {
                mostrarModal(mensaje);
            }
        }}
    ]);
}

function actualizarTanteador() {
    document.getElementById("jugador").textContent = victoriasJugador;
    document.getElementById("pc").textContent = victoriasPc;
    document.getElementById("partidas").textContent = partidasJugadas;
}

function reiniciar() {
    victoriasJugador = 0;
    victoriasPc = 0;
    partidasJugadas = 0;
    actualizarTanteador();
    mostrarModal("Juego reiniciado. ¡A jugar!");
}

function mostrarModal(mensaje, botones = [{texto: "OK", accion: ()=>cerrarModal()}]) {
    const modal = document.getElementById("modal");
    document.getElementById("modal-mensaje").innerText = mensaje;
    const contenedorBotones = document.getElementById("modal-botones");
    contenedorBotones.innerHTML = "";
    botones.forEach(b => {
        const btn = document.createElement("button");
        btn.innerText = b.texto;
        btn.onclick = () => { b.accion(); };
        contenedorBotones.appendChild(btn);
    });
    modal.style.display = "flex";
}
function cerrarModal() {
    document.getElementById("modal").style.display = "none";
}