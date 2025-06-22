const sectionSeleccionarPersonaje = document.getElementById('seleccionar-personaje');
const botonPersonajeJugador = document.getElementById('boton_personaje');

const sectionSeleccionarAtaque = document.getElementById('seleccionar-ataque');
const botonFuego = document.getElementById('boton-fuego');
const botonAgua = document.getElementById('boton-agua');
const botonTierra = document.getElementById('boton-tierra');
const botonAire = document.getElementById('boton-aire');

const sectionMensajes = document.getElementById('mensajes');

const spanVidasJugador = document.getElementById('vidas-jugador');
const spanVidasEnemigo = document.getElementById('vidas-enemigo');

const sectionReiniciar = document.getElementById('reiniciar');
const botonReiniciar = document.getElementById('boton-reiniciar');

let personajeJugador;
let personajeEnemigo;
let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;

function iniciarJuego() {
    sectionSeleccionarAtaque.style.display = 'none';
    sectionReiniciar.style.display = 'none';

    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
    botonFuego.addEventListener('click', ataqueFuego);
    botonAgua.addEventListener('click', ataqueAgua);
    botonTierra.addEventListener('click', ataqueTierra);
    botonAire.addEventListener('click', ataqueAire);
    botonReiniciar.addEventListener('click', reiniciarJuego);
}

function seleccionarPersonajeJugador() {
    const inputRadiosPersonaje = document.querySelectorAll('input[name="personaje"]');
    let personajeSeleccionado = null;

    for (let i = 0; i < inputRadiosPersonaje.length; i++) {
        if (inputRadiosPersonaje[i].checked) {
            personajeSeleccionado = inputRadiosPersonaje[i];
            break;
        }
    }

    if (personajeSeleccionado) {
        personajeJugador = personajeSeleccionado.id;
        alert("Seleccionaste a " + personajeJugador.toUpperCase());
        sectionSeleccionarPersonaje.style.display = 'none';
        sectionSeleccionarAtaque.style.display = 'flex';
        seleccionarPersonajeEnemigo();
    } else {
        alert("Por favor selecciona un personaje");
    }
}

function seleccionarPersonajeEnemigo() {
    let aleatorio = Math.floor(Math.random() * 4);
    const personajes = ["Zuko", "Katara", "Aang", "Toph"];
    personajeEnemigo = personajes[aleatorio];
}

function ataqueFuego() {
    ataqueJugador = "FUEGO";
    ataqueAleatorioEnemigo();
}

function ataqueAgua() {
    ataqueJugador = "AGUA";
    ataqueAleatorioEnemigo();
}

function ataqueTierra() {
    ataqueJugador = "TIERRA";
    ataqueAleatorioEnemigo();
}

function ataqueAire() {
    ataqueJugador = "AIRE";
    ataqueAleatorioEnemigo();
}

function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = Math.floor(Math.random() * 4);
    if (ataqueAleatorio == 0) ataqueEnemigo = "FUEGO";
    else if (ataqueAleatorio == 1) ataqueEnemigo = "AGUA";
    else if (ataqueAleatorio == 2) ataqueEnemigo = "TIERRA";
    else ataqueEnemigo = "AIRE";
    combate();
}

function combate() {
    if (ataqueJugador == ataqueEnemigo) {
        crearMensaje("AMBOS ATACARON CON " + ataqueJugador + " - EMPATE");
    } else if (
        (ataqueJugador == "FUEGO" && ataqueEnemigo == "TIERRA") ||
        (ataqueJugador == "AGUA" && ataqueEnemigo == "FUEGO") ||
        (ataqueJugador == "TIERRA" && ataqueEnemigo == "AGUA") ||
        (ataqueJugador == "AIRE" && ataqueEnemigo == "TIERRA")
    ) {
        crearMensaje(personajeJugador.toUpperCase() + " ATACÓ CON " + ataqueJugador + " Y " + personajeEnemigo.toUpperCase() + " ATACÓ CON " + ataqueEnemigo + " - GANASTE LA RONDA!");
        vidasEnemigo--;
        spanVidasEnemigo.innerHTML = vidasEnemigo;
    } else {
        crearMensaje(personajeJugador.toUpperCase() + " ATACÓ CON " + ataqueJugador + " Y " + personajeEnemigo.toUpperCase() + " ATACÓ CON " + ataqueEnemigo + " - PERDISTE LA RONDA");
        vidasJugador--;
        spanVidasJugador.innerHTML = vidasJugador;
    }
    revisarVidas();
}

function revisarVidas() {
    if (vidasEnemigo == 0) {
        crearMensajeFinal("FELICITACIONES! DERROTASTE A " + personajeEnemigo.toUpperCase() + " Y GANASTE EL JUEGO! 🎉");
    } else if (vidasJugador == 0) {
        crearMensajeFinal("OH NO! " + personajeEnemigo.toUpperCase() + " TE DERROTÓ. PERDISTE EL JUEGO 😭");
    }
}

function crearMensaje(resultadoCombate) {
    let nuevoParrafo = document.createElement('p');
    nuevoParrafo.innerHTML = resultadoCombate;
    sectionMensajes.appendChild(nuevoParrafo);
}

function crearMensajeFinal(resultadoFinal) {
    let nuevoParrafo = document.createElement('p');
    nuevoParrafo.innerHTML = resultadoFinal;
    sectionMensajes.appendChild(nuevoParrafo);

    botonFuego.disabled = true;
    botonAgua.disabled = true;
    botonTierra.disabled = true;
    botonAire.disabled = true;

    sectionReiniciar.style.display = 'block';
}

function reiniciarJuego() {
    location.reload();
}

window.addEventListener('load', iniciarJuego);