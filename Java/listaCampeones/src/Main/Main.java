package Main;

import java.util.List;
import java.util.Scanner;

import campeon.campeon;
import campeondao.campeondao;
import conexion.conexion;

public class Main {
    public static void main(String[] args) {
    	
        conexion con = new conexion();
        con.conectar("lol", "root", "");
        
        campeondao dao = new campeondao(con.getConexion());

        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n=== MENÚ ===");
            System.out.println("1. Listar Campeones");
            System.out.println("2. Ver Campeón");
            System.out.println("3. Agregar Campeón");
            System.out.println("0. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {
                case 1:
                    List<campeon> lista = dao.listarCampeones();
                    if (lista.isEmpty()) {
                        System.out.println("No hay campeones.");
                    } else {
                        for (campeon c : lista) {
                            System.out.println(c);
                        }
                    }
                    break;

                case 2:
                    System.out.print("Introduce ID o nombre parcial: ");
                    String criterio = sc.nextLine();
                    List<campeon> encontrados = dao.buscarCampeon(criterio);
                    if (encontrados.isEmpty()) {
                        System.out.println("No se encontró ningún campeón.");
                    } else {
                        for (campeon c : encontrados) {
                            System.out.println(c);
                            System.out.println("Lore: " + c.getLore());
                        }
                    }
                    break;

                case 3:
                	System.out.print("id: ");
                    String id = sc.nextLine();
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Título: ");
                    String titulo = sc.nextLine();
                    System.out.print("Tags (separados por coma): ");
                    String tags = sc.nextLine();
                    System.out.print("Lore: ");
                    String lore = sc.nextLine();

                    boolean agregado = dao.agregarCampeon(id,nombre, titulo, tags, lore);
                    if (agregado) {
                        System.out.println("¡Campeón agregado con éxito!");
                    }
                    break;

                case 0:
                    System.out.println("Saliendo...");
                    break;

                default:
                    System.out.println("Opción no válida.");
            }

        } while (opcion != 0);

        sc.close();

    }
}
