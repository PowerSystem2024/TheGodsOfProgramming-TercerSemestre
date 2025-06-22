'use strict'

try {
    let x = 10
    miFuncion() // Llamada a una función que no existe
    throw 'Error de prueba'
} catch (error) {
    console.log(error)
    console.log(typeof error)
} finally {
    console.log('Termina revisión de errores')
}

console.log('Continuamos...')

let resultado = 'Hola'

try {
    y = 5   // Variable no declarada esto generará un error de referencia
    if (isNaN(resultado)) {
        throw 'No es un número'
    } else if (resultado === '') {
        throw 'Es una cadena vacía'
    } else if (resultado >= 0) {
        throw 'Es un número positivo'
    } else if (resultado < 0) {
        throw 'Es un número negativo'
    }
} catch (error) {
    console.log(error)
    console.log(error.name)
    console.log(error.message)
} finally {
    console.log('Termina revisión de errores 2')
}