class Cuenta {
    private String numeroCuenta;
    private Titular titular;
    private double saldo;

    public Cuenta(String numeroCuenta, Titular titular, double saldoInicial) {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public String getNumeroCuenta() {
        return numeroCuenta;
    }

    public Titular getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void ingresar(double cantidad) {
        saldo += cantidad;
        System.out.println("Ingreso realizado. Nuevo saldo: " + saldo + "€");
    }

    public void retirar(double cantidad) {
        try {
            if (saldo - cantidad < 0) {
                throw new IllegalArgumentException("No puede quedar saldo negativo.");
            }
            saldo -= cantidad;
            System.out.println("Retiro exitoso. Nuevo saldo: " + saldo + "€");
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void mostrarInformacion() {
        System.out.println("Cuenta: " + numeroCuenta + " | Titular: " + titular.getNombreCompleto() + " | Saldo: " + saldo + "€");
    }
}
