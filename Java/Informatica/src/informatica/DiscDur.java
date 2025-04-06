package informatica;

public class DiscDur extends Article {
    private float capacitat;

    public DiscDur(String codi, String descripcio, int unitats, float preuBase, float capacitat) {
        super(codi, descripcio, unitats, preuBase);
        this.capacitat = capacitat;
    }

    public float getCapacitat() {
        return capacitat;
    }

    @Override
    public float preu() {
        return getPreuBase() * capacitat * 0.9f;
    }

    @Override
    public String toString() {
        return String.format("%-5s %-15s %4d %8.1fGB %6.1f", getCodi(), getDescripcio(), getUnitats(), capacitat, preu());
    }
}
