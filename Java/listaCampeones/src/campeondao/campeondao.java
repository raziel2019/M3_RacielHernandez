package campeondao;

import campeon.campeon;
import java.sql.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class campeondao {

    private Connection conn;

    public campeondao(Connection conn) {
        this.conn = conn;
    }

    public List<campeon> listarCampeones() {
        List<campeon> lista = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM champions");

            while (rs.next()) {
                campeon c = new campeon(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("title"),
                        Arrays.asList(rs.getString("tags").split(",")),
                        rs.getString("lore")
                );
                lista.add(c);
            }
        } catch (SQLException e) {
            System.out.println("Error al listar campeones: " + e.getMessage());
        }
        return lista;
    }

    public List<campeon> buscarCampeon(String criterio) {
        List<campeon> resultados = new ArrayList<>();
        try {
            String sql;
            PreparedStatement stmt;

            try {
                int id = Integer.parseInt(criterio);
                sql = "SELECT * FROM champions WHERE id = ?";
                stmt = conn.prepareStatement(sql);
                stmt.setInt(1, id);
            } catch (NumberFormatException ex) {
                sql = "SELECT * FROM champions WHERE name LIKE ?";
                stmt = conn.prepareStatement(sql);
                stmt.setString(1, "%" + criterio + "%");
            }

            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                campeon c = new campeon(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("title"),
                        Arrays.asList(rs.getString("tags").split(",")),
                        rs.getString("lore")
                );
                resultados.add(c);
            }

        } catch (SQLException e) {
            System.out.println("Error en la búsqueda: " + e.getMessage());
        }
        return resultados;
    }

    public boolean agregarCampeon(String id, String nombre, String titulo, String tags, String lore) {
        try {
            PreparedStatement checkStmt = conn.prepareStatement(
                    "SELECT COUNT(*) FROM champions WHERE LOWER(name) = LOWER(?)");
            checkStmt.setString(1, nombre);
            ResultSet rs = checkStmt.executeQuery();
            rs.next();
            if (rs.getInt(1) > 0) {
                System.out.println("Ya existe un campeón con ese nombre.");
                return false;
            }

            PreparedStatement stmt = conn.prepareStatement(
                    "INSERT INTO champions (id, name, title, tags, lore) VALUES (?, ?, ?, ?, ?)");
            stmt.setString(1, id);
            stmt.setString(2, nombre);
            stmt.setString(3, titulo);
            stmt.setString(4, tags);
            stmt.setString(5, lore);
            stmt.executeUpdate();
            return true;

        } catch (SQLException e) {
            System.out.println("Error al agregar campeón: " + e.getMessage());
            return false;
        }
    }
}