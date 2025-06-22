package ar.com.thegodsofprogramming.argumentos;

public class ArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Ana", "Ramirez", 7, 8, 9);
    }

    private static void variosParametros(String nombre, String apellido, int... numeros) {
        System.out.println("Nombre: " + nombre + " Apellido: " + apellido);
        imprimirNumeros(numeros);
    }

    private static void imprimirNumeros(int... numeros) {
        for (int numero : numeros) {
            System.out.println("Elemento: " + numero);
        }
    }
}