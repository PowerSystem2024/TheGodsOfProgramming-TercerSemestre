package ar.com.thegodsofprogramming.enumeraciones;

public enum Continentes {
    AFRICA(54, 1340000000),
    EUROPA(44, 747000000),
    ASIA(49, 4641000000L),
    AMERICA(35, 1000000000),
    OCEANIA(14, 42000000);

    private final int paises;
    private final long habitantes;

    Continentes(int paises, long habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }

    public int getPaises() {
        return paises;
    }

    public long getHabitantes() {
        return habitantes;
    }
}