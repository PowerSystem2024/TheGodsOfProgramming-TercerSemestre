let numDiscos = 3;
let torres = [[], [], []];
let movimientos = 0;
let torreSeleccionada = null;

// Función para mostrar el modal de victoria
function showModal(message) {
  document.getElementById('modalMessage').textContent = message;
  document.getElementById('victoryModal').classList.add('show');
}

// Función para ocultar el modal y reiniciar el juego
function hideModal() {
  document.getElementById('victoryModal').classList.remove('show');
  iniciarJuego(); // Reinicia el juego al cerrar el modal
}

function iniciarJuego() {
  clearAllTimeouts();
  numDiscos = parseInt(document.getElementById('numDiscos').value);
  reiniciar();
  torreSeleccionada = null;
  quitarResaltado();
}

function reiniciar() {
  torres = [[], [], []];
  movimientos = 0;
  torreSeleccionada = null;
  quitarResaltado();
  for (let i = numDiscos; i >= 1; i--) {
    torres[0].push(i);
  }
  dibujarTorres();
}

function dibujarTorres() {
  for (let i = 0; i < 3; i++) {
    const torreDiv = document.getElementById(`torre${String.fromCharCode(65 + i)}`);
    torreDiv.innerHTML = '';
    const base = document.createElement('div');
    base.classList.add('base');
    torreDiv.appendChild(base);
    for (let j = 0; j < torres[i].length; j++) {
      const disco = document.createElement('div');
      disco.classList.add('disco');
      disco.style.setProperty('--tamaño', torres[i][j]);
      disco.textContent = torres[i][j];
      torreDiv.appendChild(disco);
    }
    torreDiv.style.outline = (torreSeleccionada === i) ? '3px solid #ffcc00' : ''; /* Resaltado dorado */
  }
}

function quitarResaltado() {
  for (let i = 0; i < 3; i++) {
    document.getElementById(`torre${String.fromCharCode(65 + i)}`).style.outline = '';
  }
}

function moverDisco(origen, destino) {
  if(origen === destino || origen === null || destino === null) return;
  if (torres[origen].length === 0) return;
  const disco = torres[origen].pop();
  if (torres[destino].length > 0 && torres[destino][torres[destino].length - 1] < disco) {
    torres[origen].push(disco); // Vuelve a poner el disco si la jugada es inválida
    return;
  }
  torres[destino].push(disco);
  movimientos++;
  dibujarTorres();
  if (torres[2].length === numDiscos) {
    setTimeout(() => showModal(`¡Ganaste en ${movimientos} movimientos!`), 100);
  }
}

function clickTorre(idx) {
  if (torreSeleccionada === null) {
    if (torres[idx].length === 0) return;
    torreSeleccionada = idx;
    dibujarTorres();
  } else if (torreSeleccionada === idx) {
    torreSeleccionada = null;
    dibujarTorres();
  } else {
    moverDisco(torreSeleccionada, idx);
    torreSeleccionada = null;
    dibujarTorres();
  }
}

let animationTimeouts = [];
let animationStep = 0;
const ANIMATION_SPEED = 1000; // 1 segundo por movimiento

function resolver() {
  reiniciar();
  clearAllTimeouts();
  animationStep = 0;
  hanoiRecursivoAnimado(numDiscos, 0, 1, 2);
}

function hanoiRecursivoAnimado(n, origen, auxiliar, destino) {
  if (n === 1) {
    const timeoutId = setTimeout(() => moverDisco(origen, destino), ANIMATION_SPEED * animationStep);
    animationTimeouts.push(timeoutId);
    animationStep++;
  } else {
    hanoiRecursivoAnimado(n - 1, origen, destino, auxiliar);
    const timeoutId = setTimeout(() => moverDisco(origen, destino), ANIMATION_SPEED * animationStep);
    animationTimeouts.push(timeoutId);
    animationStep++;
    hanoiRecursivoAnimado(n - 1, auxiliar, origen, destino);
  }
}

function clearAllTimeouts() {
  animationTimeouts.forEach(id => clearTimeout(id));
  animationTimeouts = [];
}

iniciarJuego();

document.getElementById('torreA').onclick = () => clickTorre(0);
document.getElementById('torreB').onclick = () => clickTorre(1);
document.getElementById('torreC').onclick = () => clickTorre(2);