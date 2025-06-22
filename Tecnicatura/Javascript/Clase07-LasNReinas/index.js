 // --- Lógica de N Reinas adaptada a dos funciones principales ---

function iniciarJuego() {
    const n = parseInt(document.getElementById('numReinas').value);
    dibujarTablero(n, []);
}

function resolver() {
    const n = parseInt(document.getElementById('numReinas').value);
    const solucion = [];
    resolverNReinas(n, 0, solucion);
    dibujarTablero(n, solucion);
}

// Dibuja el tablero y coloca las reinas según el array solucion
function dibujarTablero(n, solucion) {
    const tablero = document.getElementById('tablero');
    tablero.style.setProperty('--n', n);
    tablero.innerHTML = '';
    for (let fila = 0; fila < n; fila++) {
    for (let col = 0; col < n; col++) {
        const celda = document.createElement('div');
        celda.className = 'celda' + ((fila + col) % 2 === 0 ? '' : ' negra');
        if (solucion[fila] === col) {
        celda.innerHTML = '<span class="reina">&#9819;</span>'; // Reina unicode
        }
        tablero.appendChild(celda);
    }
    }
}

// Algoritmo recursivo para resolver N Reinas (guarda la primera solución)
function resolverNReinas(n, fila, solucion) {
    if (fila === n) return true;
    for (let col = 0; col < n; col++) {
    if (esSeguro(fila, col, solucion)) {
        solucion[fila] = col;
        if (resolverNReinas(n, fila + 1, solucion)) return true;
    }
    }
    solucion[fila] = undefined;
    return false;
}

function esSeguro(fila, col, solucion) {
    for (let i = 0; i < fila; i++) {
    if (
        solucion[i] === col ||
        solucion[i] - i === col - fila ||
        solucion[i] + i === col + fila
    ) {
        return false;
    }
    }
    return true;
}

// Inicializa el tablero al cargar
window.onload = iniciarJuego;