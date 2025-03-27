package empleado;

public class Contable extends EmpleadoOficina {
    public Contable(String nombre, int edad, float salarioBase) {
        super(nombre, edad, salarioBase);
    }

    @Override
    public void trabajar() {
        System.out.println("Soy un contable y gestiono las cuentas y presupuestos.");
    }
}

