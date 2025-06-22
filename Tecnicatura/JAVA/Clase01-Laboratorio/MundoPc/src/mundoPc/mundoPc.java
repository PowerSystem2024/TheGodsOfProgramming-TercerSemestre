
package mundoPc;

import ar.com.system2023.mundopc.*;

public class mundoPc {
    public static void main(String[] args){
        Monitor monitorHP = new Monitor("HP", 13); 
        Teclado tecladoHP = new Teclado("Blutooth", "HP");
        Raton ratonHP = new Raton("Blutooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP,tecladoHP, ratonHP);
        
        //Creamos otros objetos de diferentes marca
        Monitor monitorGamer = new Monitor("Gamer", 13); //Importar clase
        Teclado tecladoGamer = new Teclado("Blutooth", "Gamer");
        Raton ratonGamer = new Raton("Blutooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer,tecladoGamer, ratonGamer);
        Orden orden1 = new Orden();//Inicializamos el arreglo vacio
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.mostrarOrden();
    }
}
