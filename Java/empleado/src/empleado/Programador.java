package empleado;

public class Programador extends EmpleadoTecnico {
    public Programador(String nombre, int edad, float salarioBase) {
        super(nombre, edad, salarioBase);
    }

    @Override
    public void trabajar() {
        System.out.println("Soy un programador y escribo código y desarrollo aplicaciones.");
    }
}
