package informatica;

import java.util.ArrayList;

public class Tienda {
    private ArrayList<Article> estoc;

    public Tienda() {
        estoc = new ArrayList<>();
    }

    public boolean añadirArtículo(Article a) {
        return estoc.add(a);
    }

    public boolean eliminarArtículo(Article a) {
        return estoc.remove(a);
    }

    public float valorEstoc() {
        float total = 0;
        for (Article a : estoc) {
            total += a.preu() * a.getUnitats();
        }
        return total;
    }

    public void listarEstoc() {
        int totalDiscs = 0;
        int totalCpus = 0;

        System.out.println("CODI  DESCRIPCIÓ     UNI  CAP/VEL  PREU");
        System.out.println("----- ------------- ---- -------- ------");

        for (Article a : estoc) {
            System.out.println(a);
            if (a instanceof DiscDur) {
                totalDiscs += a.getUnitats();
            } else if (a instanceof Cpu) {
                totalCpus += a.getUnitats();
            }
        }

        System.out.println("\nNombre total de discs durs en estoc: " + totalDiscs);
        System.out.println("Nombre total de CPUs en estoc: " + totalCpus);
        System.out.println("\nValor total de l'estoc: " + valorEstoc());
    }
}