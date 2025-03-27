package empleado;

public class Secretario extends EmpleadoOficina {
    public Secretario(String nombre, int edad, float salarioBase) {
        super(nombre, edad, salarioBase);
    }

    @Override
    public void trabajar() {
        System.out.println("Soy un secretario y gestiono reuniones y documentos.");
    }
}

