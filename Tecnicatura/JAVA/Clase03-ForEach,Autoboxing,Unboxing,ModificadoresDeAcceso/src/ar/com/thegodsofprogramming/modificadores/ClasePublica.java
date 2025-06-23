package ar.com.thegodsofprogramming.modificadores;

public class ClasePublica {
    public String atributoPublico = "Valor público";
    protected String atributoProtegido = "Valor protegido";
    String atributoDefault = "Valor default";
    private String atributoPrivado = "Valor privado";

    public void metodoPublico() {
        System.out.println("Método público");
    }

    protected void metodoProtegido() {
        System.out.println("Método protegido");
    }

    void metodoDefault() {
        System.out.println("Método default");
    }

    private void metodoPrivado() {
        System.out.println("Método privado");
    }

    public String getAtributoPrivado() {
        return atributoPrivado;
    }

    public void setAtributoPrivado(String valor) {
        this.atributoPrivado = valor;
    }
}