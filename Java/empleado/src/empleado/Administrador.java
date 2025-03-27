package empleado;

public class Administrador extends EmpleadoTecnico {
    public Administrador(String nombre, int edad, float salarioBase) {
        super(nombre, edad, salarioBase);
    }

    @Override
    public void trabajar() {
        System.out.println("Soy un administrador de sistemas y gestiono los servidores y la red.");
    }
}

