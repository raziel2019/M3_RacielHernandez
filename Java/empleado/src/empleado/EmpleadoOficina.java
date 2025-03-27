package empleado;

public class EmpleadoOficina extends Empleado {
    public EmpleadoOficina(String nombre, int edad, float salarioBase) {
        super(nombre, edad, salarioBase);
    }

    @Override
    public void trabajar() {
        System.out.println("Soy un empleado de oficina y realizo tareas administrativas.");
    }
}
