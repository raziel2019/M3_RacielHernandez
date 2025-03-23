package coche;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Taller taller = new Taller();

        int opcion;
        do {
            System.out.println("\n--- MENÚ ---");
            System.out.println("1. Listar coches");
            System.out.println("2. Añadir coche");
            System.out.println("3. Salir");
            System.out.print("Elige una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1:
                    taller.listarCoches();
                    break;
                case 2:
                    System.out.print("Marca: ");
                    String marca = scanner.nextLine();

                    System.out.print("Modelo: ");
                    String modelo = scanner.nextLine();

                    System.out.print("Cilindrada: ");
                    float cilindrada = scanner.nextFloat();

                    System.out.print("Potencia: ");
                    float potencia = scanner.nextFloat();
                    scanner.nextLine();

                    System.out.print("Transmisión (Manual/Automatica): ");
                    String transmisionStr = scanner.nextLine().toUpperCase();
                    Transmision transmision = Transmision.valueOf(transmisionStr);

                    System.out.print("¿Es híbrido? (true/false): ");
                    boolean hibrido = scanner.nextBoolean();

                    Coche nuevoCoche = new Coche(marca, modelo, cilindrada, potencia, transmision, hibrido);
                    taller.agregarCoche(nuevoCoche);
                    System.out.println("Coche añadido correctamente.");
                    break;
                case 3:
                    System.out.println("Saliendo del programa.");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }

        } while (opcion != 3);
    }
}
