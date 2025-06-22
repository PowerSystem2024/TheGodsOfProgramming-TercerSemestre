class Empleado {
    constructor(nombre, sueldo) {
        this._nombre = nombre;
        this._sueldo = sueldo;
    }
    obtenerDetalles() {
        return `Empleado: ${this._nombre}, Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento) {
        super(nombre, sueldo);
        this._departamento = departamento;
    }
    //Agregamos la sobreescritura
    obtenerDetalles() {
        return `Gerente: ${super.obtenerDetalles()} 
        depto:${this._departamento}`;
    }
}

function imprimir( tipo ){ // recibe una variable
    console.log( tipo.obtenerDetalles() );// Esta llamando al método de la clase padre o hija según el objeto que se le pase
    // Verifica el tipo de objeto y muestra información adicional si es un Gerente
    if( tipo instanceof Gerente){
        console.log('Es un objeto de tipo Gerente');
        console.log( tipo._departamento );
    }
    else if( tipo instanceof Empleado){
        console.log('Es de tipo empleado');
        console.log(tipo._departamento); // Esto no funcionará porque Empleado no tiene _departamento
    }
    else if( tipo instanceof Object){ //El orden de las condiciones es importante
        // Esto se ejecutará si el objeto no es ni Empleado ni Gerente, pero
        // es un objeto de JavaScript (lo cual es cierto para cualquier objeto).
        // Por ejemplo, si se pasa un objeto literal o una instancia de otra clase.
        console.log('Es de tipo Object'); // clase padre de todas las clases
    }
}

let gerente1 = new Gerente('Ricardo', 5000, 'Sistemas');
console.log(gerente1); //Objeto de la clase hija

let empleado1 = new Empleado('Andres', 4000);
console.log(empleado1); //Objeto de la clase padre

imprimir( empleado1 ); //Esta llamando al método de la clase padre
imprimir( gerente1 ); //Esta llamando al método de la clase hija
// El método imprimir recibe un objeto de tipo Empleado o Gerente y muestra sus detalles
// Además, verifica el tipo de objeto y muestra información adicional si es un Gerente.
// Esto demuestra el concepto de polimorfismo, donde el mismo método puede comportarse de manera diferente según el tipo de objeto que se le pase.