package informatica;

public class Cpu extends Article {
    private float velocitat;

    public Cpu(String codi, String descripcio, int unitats, float preuBase, float velocitat) {
        super(codi, descripcio, unitats, preuBase);
        this.velocitat = velocitat;
    }

    public float getVelocitat() {
        return velocitat;
    }

    @Override
    public float preu() {
        return getPreuBase() * velocitat;
    }

    @Override
    public String toString() {
        return String.format("%-5s %-15s %4d %8.1fMHz %6.1f", getCodi(), getDescripcio(), getUnitats(), velocitat, preu());
    }
}