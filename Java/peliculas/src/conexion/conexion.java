package conexion;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class conexion {
	
	 private Connection conexion;

	    public void conectar(String baseDeDatos, String usuario, String contraseña) {
	        String url = "jdbc:mysql://localhost:3306/" + baseDeDatos;
	        try {
	            conexion = DriverManager.getConnection(url, usuario, contraseña);
	            System.out.println("¡Conexión exitosa!");
	        } catch (SQLException e) {
	            System.out.println("Error de conexión: " + e.getMessage());
	        }
	    }
	    
	    
	 public Connection getConexion() {
	      return conexion;
	 }
	
}
