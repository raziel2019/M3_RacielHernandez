package Main;

import conexion.conexion;
import registros.GestionRegistros;

public class Main {
    public static void main(String[] args) {
    	conexion miConexion = new conexion();
        miConexion.conectar("pelicules", "root", "");

        GestionRegistros gestor = new GestionRegistros(miConexion.getConexion());

        gestor.obtenerTodosLosRegistros("pelicules");
        gestor.obtenerRegistroPorClave("clients", "id_client", "1");
    }
}
