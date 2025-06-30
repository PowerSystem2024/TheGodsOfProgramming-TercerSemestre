let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;

function iniciarJuego() {
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    let botonPunio = document.getElementById('boton-punio');
    botonPunio.addEventListener('click', ataquePunio);
    let botonPatada = document.getElementById('boton-patada');
    botonPatada.addEventListener('click', ataquePatada);
    let botonBarrida = document.getElementById('boton-barrida');
    botonBarrida.addEventListener('click', ataqueBarrida);

    let botonReiniciar = document.getElementById('boton-reiniciar');
    botonReiniciar.addEventListener('click', reiniciarJuego);
}

function seleccionarPersonajeJugador() {
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');
    let spanPersonajeJugador = document.getElementById('personaje-jugador');

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuko';
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara';
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang';
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph';
    } else {
        alert('Selecciona un personaje');
        return;
    }

    seleccinarPersonajeEnemigo();
    ocultarSeccion('seleccionar-personaje');
    mostrarSeccion('seleccionar-ataque');
}

function seleccinarPersonajeEnemigo() {
    let personajeAleatorio = aleatorio(1, 4);
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');

    if (personajeAleatorio == 1) {
        spanPersonajeEnemigo.innerHTML = 'Zuko';
    } else if (personajeAleatorio == 2) {
        spanPersonajeEnemigo.innerHTML = 'Katara';
    } else if (personajeAleatorio == 3) {
        spanPersonajeEnemigo.innerHTML = 'Aang';
    } else {
        spanPersonajeEnemigo.innerHTML = 'Toph';
    }
}

function ataquePunio() {
    ataqueJugador = 'PUÑO ✊';
    ataqueAleatorioEnemigo();
}

function ataquePatada() {
    ataqueJugador = 'PATADA 🦶';
    ataqueAleatorioEnemigo();
}

function ataqueBarrida() {
    ataqueJugador = 'BARRIDA 👣';
    ataqueAleatorioEnemigo();
}

function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3);

    if (ataqueAleatorio == 1) {
        ataqueEnemigo = 'PUÑO ✊';
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = 'PATADA 🦶';
    } else {
        ataqueEnemigo = 'BARRIDA 👣';
    }

    combate();
}

function combate() {
    let spanVidasJugador = document.getElementById('vidas-jugador');
    let spanVidasEnemigo = document.getElementById('vidas-enemigo');
    let resultado = document.getElementById('resultado');
    let ataqueJugadorDiv = document.getElementById('ataque-del-jugador');
    let ataqueEnemigoDiv = document.getElementById('ataque-del-enemigo');

    ataqueJugadorDiv.innerHTML = `Tú atacaste con: ${ataqueJugador}`;
    ataqueEnemigoDiv.innerHTML = `El enemigo atacó con: ${ataqueEnemigo}`;

    if (ataqueJugador === ataqueEnemigo) {
        resultado.innerHTML = 'EMPATE 🤝';
    } else if (
        (ataqueJugador === 'PUÑO ✊' && ataqueEnemigo === 'BARRIDA 👣') ||
        (ataqueJugador === 'PATADA 🦶' && ataqueEnemigo === 'PUÑO ✊') ||
        (ataqueJugador === 'BARRIDA 👣' && ataqueEnemigo === 'PATADA 🦶')
    ) {
        resultado.innerHTML = 'GANASTE 🎉';
        vidasEnemigo--;
        spanVidasEnemigo.innerHTML = vidasEnemigo;
    } else {
        resultado.innerHTML = 'PERDISTE 😢';
        vidasJugador--;
        spanVidasJugador.innerHTML = vidasJugador;
    }

    revisarVidas();
}

function revisarVidas() {
    if (vidasEnemigo === 0) {
        crearMensajeFinal('¡Felicidades! Has ganado el juego 🏆');
    } else if (vidasJugador === 0) {
        crearMensajeFinal('Lo siento, has perdido el juego 💔');
    }
}

function crearMensajeFinal(resultado) {
    let mensaje = document.getElementById('resultado');
    mensaje.innerHTML = resultado;

    ocultarSeccion('seleccionar-ataque');
    mostrarSeccion('mensajes');
    mostrarSeccion('reiniciar');
}

function reiniciarJuego() {
    location.reload();
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function ocultarSeccion(id) {
    document.getElementById(id).classList.add('hidden');
}

function mostrarSeccion(id) {
    document.getElementById(id).classList.remove('hidden');
}

window.addEventListener('load', iniciarJuego);