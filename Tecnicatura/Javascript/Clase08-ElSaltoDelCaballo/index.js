let N = 8;
let movX = [2, 1, -1, -2, -2, -1, 1, 2];
let movY = [1, 2, 2, 1, -1, -2, -2, -1];
let tablero = [];
let animando = false;
let continuarAnimacion = true;

const contenedor = document.getElementById("tablero");
const btnReiniciar = document.getElementById("btnReiniciar");
const inputN = document.getElementById("inputN");

function crearTablero() {
  contenedor.innerHTML = "";
  contenedor.style.setProperty('--n', N);
  contenedor.style.gridTemplateColumns = `repeat(${N}, 48px)`;
  contenedor.style.gridTemplateRows = `repeat(${N}, 48px)`;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const casilla = document.createElement("div");
      casilla.classList.add("casilla");
      if ((i + j) % 2 !== 0) {
        casilla.classList.add("negra");
      }
      casilla.id = `c-${i}-${j}`;
      contenedor.appendChild(casilla);
    }
  }
}

function esValido(x, y) {
  return x >= 0 && y >= 0 && x < N && y < N && tablero[x][y] === -1;
}

function pintarTablero() {
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const celda = document.getElementById(`c-${i}-${j}`);
      if (!celda) continue;
      celda.classList.remove("caballo", "visitada");
      // Si la celda fue visitada, muestra el número de salto
      if (tablero[i][j] !== -1) {
        celda.innerHTML = `<span class="salto-num">${tablero[i][j]}</span>`;
        celda.classList.add("visitada");
      } else {
        celda.innerHTML = "";
      }
    }
  }
  // Encuentra la posición actual del caballo (el número más alto)
  let maxSalto = -1, xCab = -1, yCab = -1;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (tablero[i][j] > maxSalto) {
        maxSalto = tablero[i][j];
        xCab = i;
        yCab = j;
      }
    }
  }
  if (xCab !== -1 && yCab !== -1) {
    const celdaCaballo = document.getElementById(`c-${xCab}-${yCab}`);
    celdaCaballo.innerHTML = `<span class="caballo-emoji">🐴</span><span class="salto-num">${maxSalto}</span>`;
    celdaCaballo.classList.add("caballo");
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function tourCaballo(x, y, salto) {
  if (!continuarAnimacion) return false;
  tablero[x][y] = salto;
  pintarTablero();

  const celda = document.getElementById(`c-${x}-${y}`);
  celda.classList.add("caballo");

  await sleep(250);
  if (!continuarAnimacion) return false;

  if (salto === N * N - 1) {
    return true;
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

  if (!continuarAnimacion) return false;
  tablero[x][y] = -1;
  pintarTablero();
  await sleep(100);
  return false;
}

contenedor.addEventListener("click", async (e) => {
  if (animando) return;
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

btnReiniciar.addEventListener("click", () => {
  continuarAnimacion = false;
  animando = false;
  N = parseInt(inputN.value);
  tablero = Array.from({ length: N }, () => Array(N).fill(-1));
  crearTablero();
  pintarTablero();
});

inputN.addEventListener("change", () => {
  btnReiniciar.click();
});

// Inicializar
N = parseInt(inputN.value);
tablero = Array.from({ length: N }, () => Array(N).fill(-1));
crearTablero();
pintarTablero();