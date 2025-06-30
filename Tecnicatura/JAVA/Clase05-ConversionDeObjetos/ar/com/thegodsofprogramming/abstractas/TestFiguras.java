package ar.com.thegodsofprogramming.abstractas;

public class TestFiguras {
    public static void main(String[] args) {
        Figura[] figuras = {
            new Rectangulo("Rectángulo 1", 4, 5),
            new Circulo("Círculo 1", 3)
        };

        for (Figura figura : figuras) {
            if (figura instanceof Imprimible) {
                ((Imprimible) figura).imprimir();
            }
        }
    }
}