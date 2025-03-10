class Titular {
    
	private String dni;
    private String nombre;
    private String apellidos;

    public Titular(String dni, String nombre, String apellidos) {
        this.dni = dni;
        this.nombre = nombre;
        this.apellidos = apellidos;
    }

    public String getDni() {
        return dni;
    }

    public String getNombreCompleto() {
        return nombre + " " + apellidos;
    }
}
