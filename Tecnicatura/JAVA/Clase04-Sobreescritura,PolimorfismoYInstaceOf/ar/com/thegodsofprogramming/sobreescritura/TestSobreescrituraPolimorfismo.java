package ar.com.thegodsofprogramming.sobreescritura;

public class TestSobreescrituraPolimorfismo {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Andres", 4000);
        Gerente gerente1 = new Gerente("Ricardo", 5000, "Sistemas");

        imprimir(empleado1);
        imprimir(gerente1);

        // instanceof y acceso a métodos específicos
        if (gerente1 instanceof Gerente) {
            System.out.println("Departamento del gerente: " + ((Gerente) gerente1).getDepartamento());
        }
        if (empleado1 instanceof Gerente) {
            System.out.println("Esto no se imprime porque empleado1 no es Gerente");
        }
    }

    public static void imprimir(Empleado empleado) {
        System.out.println(empleado.obtenerDetalles());
        if (empleado instanceof Gerente) {
            System.out.println("Es un objeto de tipo Gerente");
        } else if (empleado instanceof Empleado) {
            System.out.println("Es de tipo Empleado");
        }
    }
}