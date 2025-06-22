class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
      this._tipoEntrada = tipoEntrada;
      this._marca = marca;
    }
  
    get tipoEntrada() {
      return this._tipoEntrada;
    }
  
    set tipoEntrada(value) {
      this._tipoEntrada = value;
    }
  
    get marca() {
      return this._marca;
    }
  
    set marca(value) {
      this._marca = value;
    }
}

class Raton extends DispositivoEntrada {
    static contadorRatones = 0;
  
    constructor(tipoEntrada, marca) {
      super(tipoEntrada, marca);
      this._idRaton = ++Raton.contadorRatones;
    }
  
    toString() {
      return `Raton [ID: ${this._idRaton}, Marca: ${this.marca}, Tipo: ${this.tipoEntrada}]`;
    }
}


class Teclado extends DispositivoEntrada {
    static contadorTeclado = 0;
  
    constructor(tipoEntrada, marca) {
      super(tipoEntrada, marca);
      this._idTeclado = ++Teclado.contadorTeclado;
    }
  
    toString() {
      return `Teclado [ID: ${this._idTeclado}, Marca: ${this.marca}, Tipo: ${this.tipoEntrada}]`;
    }
}
    

class Monitor {
    static contadorMonitores = 0;
  
    constructor(marca, tamaño) {
      this._idMonitor = ++Monitor.contadorMonitores;
      this._marca = marca;
      this._tamaño = tamaño;
    }
  
    get idMonitor() {
      return this._idMonitor;
    }
  
    toString() {
      return `Monitor [ID: ${this._idMonitor}, Marca: ${this._marca}, Tamaño: ${this._tamaño}]`;
    }
}


class Computadora {
    static contadorComputadoras = 0;
  
    constructor(nombre, monitor, teclado, raton) {
      this._idComputadora = ++Computadora.contadorComputadoras;
      this._nombre = nombre;
      this._monitor = monitor;
      this._teclado = teclado;
      this._raton = raton;
    }
  
    toString() {
      return `\nComputadora [ID: ${this._idComputadora}, Nombre: ${this._nombre}]\n${this._monitor.toString()}\n${this._teclado.toString()}\n${this._raton.toString()}`;
    }
}
  

class Orden {
    static contadorOrdenes = 0;
  
    constructor() {
      this._idOrden = ++Orden.contadorOrdenes;
      this._computadoras = [];
    }
  
    agregarComputadora(computadora) {
      this._computadoras.push(computadora);
    }
  
    mostrarOrden() {
      let computadorasStr = '';
      for (let computadora of this._computadoras) {
        computadorasStr += computadora.toString() + '\n';
      }
      console.log(`Orden [ID: ${this._idOrden}]\n${computadorasStr}`);
    }
}


let monitor1 = new Monitor('Philips', '32 pulgadas');
let teclado1 = new Teclado('Bluetooth', 'Microsoft');
let raton1 = new Raton('Bluetooth', 'HP');

let computadora1 = new Computadora('Diseño', monitor1, teclado1, raton1);

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.mostrarOrden();

let monitor2 = new Monitor('AOC', '21 pulgadas');
let teclado2 = new Teclado('USB', 'Logitech');
let raton2 = new Raton('USB', 'Trust');

let computadora2 = new Computadora('Oficina', monitor2, teclado2, raton2);

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.mostrarOrden();

let monitor3 = new Monitor('Dell', '27 pulgadas');
let teclado3 = new Teclado('Inalámbrico', 'Apple');
let raton3 = new Raton('Inalámbrico', 'Apple');

let computadora3 = new Computadora('Gamer', monitor3, teclado3, raton3);

let orden3 = new Orden();
orden3.agregarComputadora(computadora3);
orden3.mostrarOrden();

let computadora4 = new Computadora('Gamer', monitor1, teclado2, raton3);

let orden4 = new Orden();
orden4.agregarComputadora(computadora4);
orden4.mostrarOrden();
