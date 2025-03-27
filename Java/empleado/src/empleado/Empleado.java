package empleado;

public class Empleado {
    protected String nombre;
    protected int edad;
    protected float salarioBase;

    public Empleado(String nombre, int edad, float salarioBase) {
        this.nombre = nombre;
        this.edad = edad;
        this.salarioBase = salarioBase;
    }

    public void trabajar() {
        System.out.println("Soy un empleado.");
    }

    public void pagarSueldo() {
        System.out.println(nombre + " ha cobrado " + salarioBase + " euros.");
    }

    public void pagarSueldo(float extra) {
        System.out.println(nombre + " ha cobrado " + (salarioBase + extra) + " euros con bonificación.");
    }

    public void aumentarSueldo(float aumento) {
        salarioBase += aumento;
        System.out.println(nombre + " ha recibido un aumento de " + aumento + " euros.");
    }
}
