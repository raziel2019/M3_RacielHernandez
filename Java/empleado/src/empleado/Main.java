package empleado;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Empleado empOficina = new EmpleadoOficina("Anna", 30, 2000);
        Empleado empSecretario = new Secretario("Laura", 28, 2100);
        Empleado empContable = new Contable("Joan", 35, 2300);
        Empleado empProgramador = new Programador("Marc", 25, 2500);
        Empleado empAdministrador = new Administrador("Jordi", 40, 2700);


        ArrayList<Empleado> empleados = new ArrayList<>();
        empleados.add(empOficina);
        empleados.add(empSecretario);
        empleados.add(empContable);
        empleados.add(empProgramador);
        empleados.add(empAdministrador);

        for (Empleado e : empleados) {
            e.trabajar();
            System.out.println("----------------------");
        }

        empProgramador.pagarSueldo();
        empAdministrador.pagarSueldo(500);
        empProgramador.aumentarSueldo(500);
        empProgramador.pagarSueldo();
    }
}
