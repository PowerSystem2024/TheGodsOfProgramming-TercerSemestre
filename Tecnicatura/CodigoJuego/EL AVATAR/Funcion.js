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


let personajeJugador; // Guardará el ID del personaje seleccionado por el jugador
let personajeEnemigo; // Guardará el ID del personaje seleccionado por el enemigo (aleatorio)
let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;


// ====== Funciones del Juego ======

function iniciarJuego() {
    // Ocultar la sección de ataque y reiniciar al inicio
    sectionSeleccionarAtaque.style.display = 'none';
    sectionReiniciar.style.display = 'none';

    // Asignar el evento click al botón de seleccionar personaje
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    // Asignar eventos click a los botones de ataque (se habilitarán después de seleccionar personaje)
    botonFuego.addEventListener('click', ataqueFuego);
    botonAgua.addEventListener('click', ataqueAgua);
    botonTierra.addEventListener('click', ataqueTierra);
    botonAire.addEventListener('click', ataqueAire);

    // Asignar evento click al botón de reiniciar
    botonReiniciar.addEventListener('click', reiniciarJuego);
}

function seleccionarPersonajeJugador() {
    // Obtener el radio button que está marcado
    const inputRadiosPersonaje = document.querySelectorAll('input[name="personaje"]');
    let personajeSeleccionado = null;

    for (let i = 0; i < inputRadiosPersonaje.length; i++) {
        if (inputRadiosPersonaje[i].checked) {
            personajeSeleccionado = inputRadiosPersonaje[i];
            break; // Salir del bucle una vez que encontramos el seleccionado
        }
    }

    if (personajeSeleccionado) {
        personajeJugador = personajeSeleccionado.id; // Guarda el ID del personaje (Zuko, Katara, Aang, Toph)
        alert("Seleccionaste a " + personajeJugador.toUpperCase());

        // Ocultar la sección de selección de personaje y mostrar la de ataque
        sectionSeleccionarPersonaje.style.display = 'none';
        sectionSeleccionarAtaque.style.display = 'flex'; // O 'block' dependiendo de tu CSS

        seleccionarPersonajeEnemigo(); // El enemigo elige su personaje
    } else {
        alert("Por favor selecciona un personaje");
    }
}

function seleccionarPersonajeEnemigo() {
    // Generar un número aleatorio entre 0 y 3 (para 4 personajes)
    let aleatorio = Math.floor(Math.random() * 4); // 0, 1, 2, 3
    const personajes = ["Zuko", "Katara", "Aang", "Toph"];

    personajeEnemigo = personajes[aleatorio];
    // alert("El enemigo eligió a " + personajeEnemigo); // Puedes descomentar para depurar
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
    let ataqueAleatorio = Math.floor(Math.random() * 4); // 0, 1, 2, 3
    if (ataqueAleatorio == 0) {
        ataqueEnemigo = "FUEGO";
    } else if (ataqueAleatorio == 1) {
        ataqueEnemigo = "AGUA";
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = "TIERRA";
    } else {
        ataqueEnemigo = "AIRE";
    }

    combate(); // Una vez que ambos tienen un ataque, se resuelve el combate
}

function combate() {
    // Lógica para determinar el ganador de la ronda y actualizar vidas
    // Aquí puedes expandir con lógica de debilidades/fortalezas elementales

    if (ataqueJugador == ataqueEnemigo) {
        crearMensaje("AMBOS ATACARON CON " + ataqueJugador + " - EMPATE");
    } else if ((ataqueJugador == "FUEGO" && ataqueEnemigo == "TIERRA") ||
        (ataqueJugador == "AGUA" && ataqueEnemigo == "FUEGO") ||
        (ataqueJugador == "TIERRA" && ataqueEnemigo == "AGUA") ||
        (ataqueJugador == "AIRE" && ataqueEnemigo == "TIERRA")) { // Añadí Aire vs Tierra como ejemplo, puedes ajustarlo
        crearMensaje(personajeJugador.toUpperCase() + " ATACÓ CON " + ataqueJugador + " Y " + personajeEnemigo.toUpperCase() + " ATACÓ CON " + ataqueEnemigo + " - GANASTE LA RONDA!");
        vidasEnemigo--;
        spanVidasEnemigo.innerHTML = vidasEnemigo;
    } else {
        crearMensaje(personajeJugador.toUpperCase() + " ATACÓ CON " + ataqueJugador + " Y " + personajeEnemigo.toUpperCase() + " ATACÓ CON " + ataqueEnemigo + " - PERDISTE LA RONDA");
        vidasJugador--;
        spanVidasJugador.innerHTML = vidasJugador;
    }

    revisarVidas(); // Verificar si alguien se quedó sin vidas
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

    // Deshabilitar botones de ataque
    botonFuego.disabled = true;
    botonAgua.disabled = true;
    botonTierra.disabled = true;
    botonAire.disabled = true;

    // Mostrar botón de reiniciar
    sectionReiniciar.style.display = 'block';
}

function reiniciarJuego() {
    location.reload(); // Recarga la página, volviendo al estado inicial
}

// Esto inicia el juego cuando la ventana (página) termina de cargar
window.addEventListener('load', iniciarJuego);