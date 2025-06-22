// Ejemplo de promesa simple
let tareaAsincrona = new Promise((resolve, reject) => {
    let exito = true;
    if (exito) {
        resolve('La tarea se completó exitosamente');
    } else {
        reject('Hubo un problema al completar la tarea');
    }
});

// Uso de then y catch
tareaAsincrona
    .then(resultado => console.log(resultado))
    .catch(error => console.log(error));

// Promesa con setTimeout y función flecha
let saludoPromesa = new Promise((resolve) => {
    setTimeout(() => resolve('¡Hola desde una promesa con setTimeout y función flecha!'), 2000);
});

// Llamado a la promesa
saludoPromesa.then(mensaje => console.log(mensaje));

// Función async que retorna una promesa
async function obtenerMensaje() {
    return 'Mensaje obtenido usando async y promesa';
}

// Uso de la función async
obtenerMensaje().then(mensaje => console.log(mensaje));

// Async/await con promesa y setTimeout
async function mostrarMensajeConRetraso() {
    let promesaDemorada = new Promise(resolve => {
        console.log('Comienza la espera...');
        setTimeout(() => resolve('Mensaje mostrado tras esperar 2 segundos'), 2000);
        console.log('Esperando...');
    });
    console.log(await promesaDemorada);
}

// Llamada a la función async/await
mostrarMensajeConRetraso();