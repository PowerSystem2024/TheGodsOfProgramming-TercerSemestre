package ar.com.thegodsofprogramming.modificadores;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
        ClasePublica clase = new ClasePublica();
        System.out.println("atributoPublico = " + clase.atributoPublico);
        System.out.println("atributoProtegido = " + clase.atributoProtegido);
        System.out.println("atributoDefault = " + clase.atributoDefault);
        // System.out.println("atributoPrivado = " + clase.atributoPrivado); // No accesible

        clase.metodoPublico();
        clase.metodoProtegido();
        clase.metodoDefault();
        // clase.metodoPrivado(); // No accesible

        System.out.println("atributoPrivado (get) = " + clase.getAtributoPrivado());
        clase.setAtributoPrivado("Nuevo valor privado");
        System.out.println("atributoPrivado (get) = " + clase.getAtributoPrivado());

        // Uso de clase default
        ClaseDefault claseDefault = new ClaseDefault();
        claseDefault.mostrarMensaje();
    }
}