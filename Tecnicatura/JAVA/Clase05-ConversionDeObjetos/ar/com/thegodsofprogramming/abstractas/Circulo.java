package ar.com.thegodsofprogramming.abstractas;

public class Circulo extends Figura implements Imprimible {
    private double radio;

    public Circulo(String nombre, double radio) {
        super(nombre);
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;
    }

    @Override
    public void imprimir() {
        System.out.println(getNombre() + " (Círculo) - Área: " + calcularArea());
    }
}