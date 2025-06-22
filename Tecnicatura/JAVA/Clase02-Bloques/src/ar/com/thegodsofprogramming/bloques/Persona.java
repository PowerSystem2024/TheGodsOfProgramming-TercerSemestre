package ar.com.thegodsofprogramming.bloques;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;

    static { // Bloque estático
        System.out.println("Ejecución bloque estático");
        ++Persona.contadorPersonas;
    }

    { // Bloque no estático
        System.out.println("Ejecución bloque no estático");
        this.idPersona = Persona.contadorPersonas++;
    }

    public Persona() {
        System.out.println("Ejecución del constructor");
    }

    public int getIdPersona() {
        return idPersona;
    }

    @Override
    public String toString() {
        return "Persona{idPersona=" + idPersona + '}';
    }
}