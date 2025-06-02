const N = 8;
const movX = [2, 1, -1, -2, -2, -1, 1, 2];
const movY = [1, 2, 2, 1, -1, -2, -2, -1];

let tablero = Array.from({ length: N }, () => Array(N).fill(-1));
const contenedor = document.getElementById("tablero");
const btnReiniciar = document.getElementById("btnReiniciar");

let caballoPos = null;
let animando = false;
let continuarAnimacion = true;

// Crear visualmente el tablero
function crearTablero() {
  contenedor.innerHTML = "";
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const casilla = document.createElement("div");
      casilla.classList.add("casilla");
      casilla.classList.add((i + j) % 2 === 0 ? "blanca" : "negra");
      casilla.id = `c-${i}-${j}`;
      contenedor.appendChild(casilla);
    }
  }
}

// Validar movimiento válido y no visitado
function esValido(x, y) {
  return x >= 0 && y >= 0 && x < N && y < N && tablero[x][y] === -1;
}

// Función para actualizar visualmente la posición del caballo y los saltos
function pintarTablero() {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const celda = document.getElementById(`c-${i}-${j}`);
      celda.textContent = tablero[i][j] === -1 ? "" : tablero[i][j];
      celda.classList.remove("caballo");
      if (tablero[i][j] !== -1) {
        celda.style.backgroundColor = (i + j) % 2 === 0 ? "#c3e6cb" : "#7ac47a"; // colores suaves para visitadas
      } else {
        celda.style.backgroundColor = (i + j) % 2 === 0 ? "#eee" : "#444";
        celda.style.color = (i + j) % 2 === 0 ? "black" : "white";
      }
    }
  }
}

// Para animar, hacemos pausa
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Algoritmo backtracking con animación (async)
async function tourCaballo(x, y, salto) {
  if (!continuarAnimacion) return false;  // abortar si se pidió parar

  tablero[x][y] = salto;
  pintarTablero();

  const celda = document.getElementById(`c-${x}-${y}`);
  celda.classList.add("caballo");
  celda.style.backgroundColor = "gold";
  celda.style.color = "black";

  await sleep(200);
  if (!continuarAnimacion) return false;  // abortar si se pidió parar

  if (salto === N * N - 1) {
    return true; // solución completa
  }

  for (let i = 0; i < 8; i++) {
    const nx = x + movX[i];
    const ny = y + movY[i];
    if (esValido(nx, ny)) {
      if (await tourCaballo(nx, ny, salto + 1)) {
        return true;
      }
    }
  }

  if (!continuarAnimacion) return false;  // abortar si se pidió parar

  // Backtracking
  tablero[x][y] = -1;
  pintarTablero();
  await sleep(100);

  return false;
}

// Manejo clic para iniciar desde la casilla clickeada
contenedor.addEventListener("click", async (e) => {
  if (animando) return; // prevenir que arranque otro mientras anima
  const target = e.target;
  if (!target.classList.contains("casilla")) return;

  const [_, xStr, yStr] = target.id.split("-");
  const x = Number(xStr);
  const y = Number(yStr);

  tablero = Array.from({ length: N }, () => Array(N).fill(-1));
  continuarAnimacion = true;
  animando = true;

  const exito = await tourCaballo(x, y, 0);
  animando = false;

  if (!exito && continuarAnimacion) {
    alert("No hay solución para esa posición inicial.");
  } else if (continuarAnimacion) {
    alert("Tour completado!");
  }
});

// Botón reiniciar
btnReiniciar.addEventListener("click", () => {
  if (!animando) {
    tablero = Array.from({ length: N }, () => Array(N).fill(-1));
    pintarTablero();
    return;
  }
  // Abortamos animación y limpiamos
  continuarAnimacion = false;
  animando = false;
  tablero = Array.from({ length: N }, () => Array(N).fill(-1));
  pintarTablero();
});

// Inicializar visualmente el tablero
crearTablero();
pintarTablero();