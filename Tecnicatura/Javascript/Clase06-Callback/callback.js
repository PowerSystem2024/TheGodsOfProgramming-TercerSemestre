/**
 * Funciones callback son funciones que se pasan como argumentos a otras funciones.
 * Se ejecutan después de que la función que las recibe ha terminado su tarea.
 */

miFuncionA();
miFuncionB();

function miFuncionA() {
    console.log('Primera función ejecutada');
}

function miFuncionB() {
    console.log('Segunda función ejecutada');
}

// Función tipo callback
let mostrar = function(mensaje) {
    console.log(mensaje);
}

function multiplicar(a, b, callback) {
    let resultado = a * b;
    callback(`El producto es: ${resultado}`);
}

multiplicar(4, 7, mostrar);

// Llamadas asíncronas con setTimeout
function saludoAsync() {
    console.log('Mensaje asíncrono tras 2 segundos');
}

setTimeout(saludoAsync, 2000);

setTimeout(function() { 
    console.log('Otro mensaje asíncrono después de 1 segundo');
}, 1000);

setTimeout(() => console.log('Mensaje asíncrono con arrow function tras 3 segundos'), 3000);

// setInterval para mostrar la hora cada segundo
let mostrarHora = () => {
    let ahora = new Date();
    console.log(`Hora actual: ${ahora.toLocaleTimeString()}`);
}

setInterval(mostrarHora, 1000);