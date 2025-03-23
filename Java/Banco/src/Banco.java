import java.util.ArrayList;
import java.util.List;

class Banco {
    private String nombre;
    private List<Cuenta> cuentas = new ArrayList<>();

    public Banco(String nombre) {
        this.nombre = nombre;
    }

    public void agregarCuenta(Cuenta cuenta) {
        cuentas.add(cuenta);
    }

    public void mostrarCuentas() {
        System.out.println("\n--- Cuentas en el banco " + nombre + " ---");
        for (Cuenta cuenta : cuentas) {
            cuenta.mostrarInformacion();
        }
    }

    public Cuenta buscarCuentaPorNumero(String numeroCuenta) {
        for (Cuenta cuenta : cuentas) {
            if (cuenta.getNumeroCuenta().equals(numeroCuenta)) {
                return cuenta;
            }
        }
        return null;
    }

    public Cuenta buscarCuentaPorDNI(String dni) {
        for (Cuenta cuenta : cuentas) {
            if (cuenta.getTitular().getDni().equals(dni)) {
                return cuenta;
            }
        }
        return null;
    }
}