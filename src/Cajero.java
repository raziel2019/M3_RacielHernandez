import java.util.Scanner;

public class Cajero {

	public static void main(String[] args) {
		 	Banco banco = new Banco("Banco Central");
	        
	        Titular juan = new Titular("44556677K", "Juan", "Garcia Martínez");
	        Titular pedro = new Titular("44556678L", "Pedro", "Lorca Benítez");
	        Titular ana = new Titular("44556679J", "Ana", "Torres Garriga");
	        
	        banco.agregarCuenta(new Cuenta("35-0-2367805", juan, 3000));
	        banco.agregarCuenta(new Cuenta("207-1-0004572", pedro, 8200));
	        banco.agregarCuenta(new Cuenta("207-1-0004573", ana, 100));
	        
	        banco.mostrarCuentas();
	        
	        System.out.println("\nIngresando 2000€ a la cuenta de Juan...");
	        banco.buscarCuentaPorNumero("35-0-2367805").ingresar(2000);
	        
	        System.out.println("\nRetirando 1000€ de la cuenta de Ana...");
	        banco.buscarCuentaPorNumero("207-1-0004573").retirar(1000);
	        
	        banco.mostrarCuentas();
	        
	        Scanner scanner = new Scanner(System.in);
	        while (true) {
	            System.out.println("\nIngrese su DNI (o 'salir' para terminar): ");
	            String dni = scanner.nextLine();
	            if (dni.equalsIgnoreCase("salir")) {
	                break;
	            }
	            Cuenta cuenta = banco.buscarCuentaPorDNI(dni);
	            if (cuenta == null) {
	                System.out.println("DNI no encontrado. Intente de nuevo.");
	                continue;
	            }
	            
	            while (true) {
	                System.out.println("\nSeleccione una opción:\n1. Ver saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Salir");
	                int opcion = scanner.nextInt();
	                scanner.nextLine();
	                
	                switch (opcion) {
	                    case 1:
	                        System.out.println("Saldo actual: " + cuenta.getSaldo() + "€");
	                        break;
	                    case 2:
	                        System.out.print("Ingrese la cantidad: ");
	                        double ingreso = scanner.nextDouble();
	                        cuenta.ingresar(ingreso);
	                        break;
	                    case 3:
	                        System.out.print("Ingrese la cantidad: ");
	                        double retiro = scanner.nextDouble();
	                        cuenta.retirar(retiro);
	                        break;
	                    case 4:
	                        System.out.println("Saliendo del cajero...");
	                        break;
	                    default:
	                        System.out.println("Opción inválida.");
	                }
	                if (opcion == 4) break;
	            }
	        }
	        scanner.close();
		
	}

}
