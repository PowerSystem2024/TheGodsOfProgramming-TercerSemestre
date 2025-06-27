package ar.com.thegodsofprogramming.abstractas;

public class Rectangulo extends Figura implements Imprimible {
    private double base;
    private double altura;

    public Rectangulo(String nombre, double base, double altura) {
        super(nombre);
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public void imprimir() {
        System.out.println(getNombre() + " (Rectángulo) - Área: " + calcularArea());
    }
}