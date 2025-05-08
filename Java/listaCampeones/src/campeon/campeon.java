package campeon;

import java.util.List;

public class campeon {
    private int id;
    private String nombre;
    private String titulo;
    private List<String> tags;
    private String lore;

    public campeon(int id, String nombre, String titulo, List<String> tags, String lore) {
        this.id = id;
        this.nombre = nombre;
        this.titulo = titulo;
        this.tags = tags;
        this.lore = lore;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTitulo() {
        return titulo;
    }

    public List<String> getTags() {
        return tags;
    }

    public String getLore() {
        return lore;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Nombre: " + nombre + ", Título: " + titulo +
                ", Tags: " + String.join(", ", tags);
    }
}