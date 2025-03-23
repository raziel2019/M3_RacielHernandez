package coche;

import java.util.HashMap;
import java.util.Map;

class Taller {
    private HashMap<Integer, Coche> coches;
    private int idActual = 1;

    public Taller() {
        coches = new HashMap<>();
    }

    public void agregarCoche(Coche coche) {
        coches.put(idActual++, coche);
    }

    public void listarCoches() {
        if (coches.isEmpty()) {
            System.out.println("No hay coches registrados.");
        } else {
            for (Map.Entry<Integer, Coche> entry : coches.entrySet()) {
                System.out.println("ID: " + entry.getKey() + " - " + entry.getValue());
            }
        }
    }
}