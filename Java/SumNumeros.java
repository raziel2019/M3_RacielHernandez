package SumaNumeros;

import java.util.Scanner;

public class SumNumeros {
	public static void main(String[] args) {
	
	int sum,num1,num2;
	Scanner sc = new Scanner(System.in);
	
	System.out.println("Introduce el primer numero: ");
	num1 = sc.nextInt();
	
	
	System.out.println("Introduce el segundo numero: ");
	num2 = sc.nextInt();
	
	sum = num1 + num2;
	
	System.out.println("El resultado de la suma es: " + sum);
	
	
	
	}
}
