package registros;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class GestionRegistros {
    private Connection conexion;

    public GestionRegistros(Connection conexion) {
        this.conexion = conexion;
    }

    public void obtenerTodosLosRegistros(String tabla) {
        try {
            Statement stmt = conexion.createStatement();
            String sql = "SELECT * FROM " + tabla;
            ResultSet rs = stmt.executeQuery(sql);

            while (rs.next()) {
                int columnas = rs.getMetaData().getColumnCount();
                for (int i = 1; i <= columnas; i++) {
                    System.out.print(rs.getString(i) + " ");
                }
                System.out.println();
            }

            rs.close();
            stmt.close();
        } catch (SQLException e) {
            System.out.println("Error al obtener los registros: " + e.getMessage());
        }
    }

    public void obtenerRegistroPorClave(String tabla, String campoClave, String valorClave) {
    	
        try {
            Statement stmt = conexion.createStatement();
            String sql = "SELECT * FROM " + tabla + " WHERE " + campoClave + " = '" + valorClave + "'";
            ResultSet rs = stmt.executeQuery(sql);

            if (rs.next()) {
                int columnas = rs.getMetaData().getColumnCount();
                for (int i = 1; i <= columnas; i++) {
                    System.out.print(rs.getString(i) + " ");
                }
                System.out.println();
            } else {
                System.out.println("No se encontró ningún registro con ese valor de clave.");
            }

            rs.close();
            stmt.close();
        } catch (SQLException e) {
            System.out.println("Error al obtener el registro: " + e.getMessage());
        }
    }
}
