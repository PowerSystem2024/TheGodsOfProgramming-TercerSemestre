function miFuncion(){
    console.log("Saludos desde mi función")
}

miFuncion();

let myFuncion = function (){
    console.log("Saludos desde la función anónima");
}

// Función flecha
let miFuncionFlecha= () => {
    console.log("Saludos desde la función flecha");
}

// Funciones flecha sin parámetros
miFuncionFlecha();
// Función flecha sin parámetros otra forma
const saludar =()=> console.log("Saludos desde esta función flecha");

saludar();

// Otro ejemplo
const saludar2= ()=> {
    return 'Saludos desde la función flecha dos';
}

console.log(saludar2());

// Forma abreviada de una función flecha
const saludar3 = () => "Saludos desde esta función flecha tres";
console.log(saludar3());

//Funciones que reciben parámetros
const funcionParametros = (mensaje)=> console.log(mensaje);

funcionParametros("Saludos desde esta función con parámetros"); ;

//Función tradicional que recibe un parámetro
const funcionParametrosClasica =function(mensaje){
    console.log(mensaje);
}
funcionParametrosClasica("Saludos desde esta función clásica");

// Función flecha que recibe un parámetro
// Si la función flecha tiene un solo parámetro, no es necesario usar paréntesis
const funcionConParametros= mensaje=> console.log(mensaje);
funcionConParametros("otra forma de trabajar con la función flecha");

//Función flecha con varios parámetros
//Si la función flecha tiene más de un parámetro, se deben usar paréntesis
const funcionConParametros2= (op1, op2) => {
    let resultado = op1 + op2;
    return resultado
}
console.log(funcionConParametros2(3,5));