package ar.com.thegodsofprogramming.sobreescritura;

public class Gerente extends Empleado {
    private String departamento;

    public Gerente(String nombre, double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    @Override
    public String obtenerDetalles() {
        return "Gerente: " + nombre + ", Sueldo: $" + sueldo + ", Departamento: " + departamento;
    }

    public String getDepartamento() {
        return departamento;
    }
}