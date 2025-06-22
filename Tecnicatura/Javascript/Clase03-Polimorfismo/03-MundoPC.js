/**
 * Tarea:
 * Gracias al polimorfismo, podemos crear una clase Orden que pueda recibir objetos 
 * de tipo Computadora, y que pueda mostrar la información de cada computadora,
 *  sin importar qué tipo de dispositivos de entrada o salida tenga cada una.
 */
// Clase abstracta base para dispositivos que no se puede instanciar directamente
class Dispositivo {
    constructor(marca) {
    if (new.target === Dispositivo) {
        throw new Error("No se puede instanciar una clase abstracta como Dispositivo");
    }
    this._marca = marca;
    }

    get marca() {
    return this._marca;
    }

    set marca(marca) {
    this._marca = marca;
    }

    describir() {
    throw new Error("El método describir() debe ser implementado por la clase hija");
    }

    toString() {
    return this.describir();
    }
}

// Clase abstracta para dispositivos de entrada
class DispositivoEntrada extends Dispositivo {
    constructor(tipoEntrada, marca) {
    super(marca);
    this._tipoEntrada = tipoEntrada;
    }

    get tipoEntrada() {
    return this._tipoEntrada;
    }

    set tipoEntrada(tipoEntrada) {
    this._tipoEntrada = tipoEntrada;
    }
}

// Raton
class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idRaton = ++Raton.contadorRatones;
    }

    get idRaton() {
    return this._idRaton;
    }

    describir() {
    return `Raton [ID: ${this._idRaton}, Marca: ${this.marca}, Tipo: ${this.tipoEntrada}]`;
    }
}

// Teclado
class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idTeclado = ++Teclado.contadorTeclados;
    }

    get idTeclado() {
    return this._idTeclado;
    }

    describir() {
    return `Teclado [ID: ${this._idTeclado}, Marca: ${this.marca}, Tipo: ${this.tipoEntrada}]`;
    }
}

// Monitor
class Monitor extends Dispositivo {
    static contadorMonitores = 0;

    constructor(marca, tamaño) {
    super(marca);
    this._idMonitor = ++Monitor.contadorMonitores;
    this._tamaño = tamaño;
    }

    get idMonitor() {
    return this._idMonitor;
    }

    get tamaño() {
    return this._tamaño;
    }

    set tamaño(tamaño) {
    this._tamaño = tamaño;
    }

    describir() {
    return `Monitor [ID: ${this._idMonitor}, Marca: ${this.marca}, Tamaño: ${this.tamaño}]`;
    }
}

// Computadora
class Computadora extends Dispositivo {
    static contadorComputadoras = 0;

    constructor(nombre, monitor, teclado, raton) {
    super("Computadora");
    this._idComputadora = ++Computadora.contadorComputadoras;
    this._nombre = nombre;
    this._monitor = monitor;
    this._teclado = teclado;
    this._raton = raton;
    }

    get idComputadora() {
    return this._idComputadora;
    }

    describir() {
    return `\nComputadora [ID: ${this._idComputadora}, Nombre: ${this._nombre}]\n${this._monitor.describir()}\n${this._teclado.describir()}\n${this._raton.describir()}`;
    }
}

// Orden
class Orden {
    static contadorOrdenes = 0;

    constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    this._computadoras = [];
    }

    agregarComputadora(computadora) {
    if (!(computadora instanceof Computadora)) {
        throw new Error("Solo se pueden agregar objetos de tipo Computadora");
    }
    this._computadoras.push(computadora);
    }

    mostrarOrden() {
    let computadorasStr = '';
    for (let computadora of this._computadoras) {
        computadorasStr += computadora.describir() + '\n';
    }
    console.log(`Orden [ID: ${this._idOrden}]\n${computadorasStr}`);
    }
}

// Código de prueba
let monitor1 = new Monitor('BenQ', '29 pulgadas');
let teclado1 = new Teclado('Bluetooth', 'Apple');
let raton1 = new Raton('Bluetooth', 'Microsoft');
let computadora1 = new Computadora('Gamer', monitor1, teclado1, raton1);

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.mostrarOrden();

let monitor2 = new Monitor('HP', '22 pulgadas');
let teclado2 = new Teclado('USB', 'HyperX');

let computadora2 = new Computadora('Oficina', monitor2, teclado2, raton2);

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.mostrarOrden();

let monitor3 = new Monitor('ViewSonic', '34 pulgadas');
let teclado3 = new Teclado('Inalámbrico', 'Dell');
let raton3 = new Raton('Inalámbrico', 'Logitech');

let computadora3 = new Computadora('Gamer', monitor3, teclado3, raton3);

let orden3 = new Orden();
orden3.agregarComputadora(computadora3);
orden3.mostrarOrden();

let computadora4 = new Computadora('Servidor', monitor1, teclado2, raton3);

let orden4 = new Orden();
orden4.agregarComputadora(computadora4);
orden4.mostrarOrden();