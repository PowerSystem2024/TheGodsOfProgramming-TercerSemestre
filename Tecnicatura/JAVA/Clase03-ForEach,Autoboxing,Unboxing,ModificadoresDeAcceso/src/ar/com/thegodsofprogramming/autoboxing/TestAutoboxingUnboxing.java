package ar.com.thegodsofprogramming.autoboxing;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        // Autoboxing
        int primitivo = 10;
        Integer objeto = primitivo; // autoboxing
        System.out.println("Integer objeto = " + objeto);

        // Unboxing
        int primitivo2 = objeto; // unboxing
        System.out.println("int primitivo2 = " + primitivo2);

        // Métodos de la clase Integer
        System.out.println("objeto.doubleValue() = " + objeto.doubleValue());
    }
}