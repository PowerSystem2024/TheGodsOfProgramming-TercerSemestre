package ar.com.thegodsofprogramming.foreach;

public class TestForEach {
    public static void main(String[] args) {
        int[] edades = {5, 6, 8, 9};
        for (int edad : edades) {
            System.out.println("Edad: " + edad);
        }

        String[] nombres = {"Ana", "Juan", "Pedro"};
        for (String nombre : nombres) {
            System.out.println("Nombre: " + nombre);
        }
    }
}