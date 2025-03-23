package coche;

enum Transmision {
    MANUAL,
    AUTOMATICA
}

class Coche {
    private String marca;
    private String modelo;
    private float cilindrada;
    private float potencia;
    private Transmision transmision;
    private boolean hibrido;
 

    public Coche(String marca, String modelo, float cilindrada, float potencia, Transmision transmision, boolean hibrido) {
        this.marca = marca;
        this.modelo = modelo;
        this.cilindrada = cilindrada;
        this.potencia = potencia;
        this.transmision = transmision;
        this.hibrido = hibrido;
    }

    @Override
    public String toString() {
        return "Marca: " + marca +
               ", Modelo: " + modelo +
               ", Cilindrada: " + cilindrada +
               ", Potencia: " + potencia +
               ", Transmisión: " + transmision +
               ", Híbrido: " + (hibrido ? "Sí" : "No");
    }
}
