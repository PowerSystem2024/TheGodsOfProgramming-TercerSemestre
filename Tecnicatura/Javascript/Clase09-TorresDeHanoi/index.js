let numDiscos = 3;
let torres = [[], [], []];
let movimientos = 0;

let torreSeleccionada = null;

function iniciarJuego() {
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
    torreDiv.style.outline = (torreSeleccionada === i) ? '3px solid orange' : '';
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
    torres[origen].push(disco);
    return;
  }
  torres[destino].push(disco);
  movimientos++;
  dibujarTorres();
  if (torres[2].length === numDiscos) {
    setTimeout(() => alert(`¡Ganaste en ${movimientos} movimientos!`), 100);
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

function resolver() {
  reiniciar();
  hanoiRecursivo(numDiscos, 0, 1, 2);
}

function hanoiRecursivo(n, origen, auxiliar, destino) {
  if (n === 1) {
    setTimeout(() => moverDisco(origen, destino), 500 * movimientos);
  } else {
    hanoiRecursivo(n - 1, origen, destino, auxiliar);
    setTimeout(() => moverDisco(origen, destino), 500 * movimientos);
    hanoiRecursivo(n - 1, auxiliar, origen, destino);
  }
}
iniciarJuego();

document.getElementById('torreA').onclick = () => clickTorre(0);
document.getElementById('torreB').onclick = () => clickTorre(1);
document.getElementById('torreC').onclick = () => clickTorre(2);
