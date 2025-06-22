package ar.com.thegodsofprogramming.enumeraciones;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Día: " + Dias.LUNES);
        indicarDiaSemana(Dias.MARTES);

        System.out.println("Continente: " + Continentes.AMERICA);
        System.out.println("Países: " + Continentes.AMERICA.getPaises());
        System.out.println("Habitantes: " + Continentes.AMERICA.getHabitantes());
    }

    private static void indicarDiaSemana(Dias dia) {
        switch (dia) {
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Séptimo día de la semana");
                break;
        }
    }
}