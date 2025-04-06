package informatica;

public abstract class Article {
    private String codi;
    private String descripcio;
    private int unitats;
    private float preuBase;

    public Article(String codi, String descripcio, int unitats, float preuBase) {
        this.codi = codi;
        this.descripcio = descripcio;
        this.unitats = unitats;
        this.preuBase = preuBase;
    }

    public abstract float preu();

    public String getCodi() {
        return codi;
    }

    public String getDescripcio() {
        return descripcio;
    }

    public int getUnitats() {
        return unitats;
    }

    public float getPreuBase() {
        return preuBase;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Article) {
            Article other = (Article) obj;
            return codi.equals(other.codi);
        }
        return false;
    }

    @Override
    public int hashCode() {
        return codi.hashCode();
    }
}
