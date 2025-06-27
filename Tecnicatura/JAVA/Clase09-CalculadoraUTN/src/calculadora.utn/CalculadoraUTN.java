package calculadorautn;

import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("***** Aplicación Calculadora UTN *****");
            System.out.print("Ingrese el primer número: ");
            double num1 = leerNumero(scanner);

            System.out.print("Ingrese el segundo número: ");
            double num2 = leerNumero(scanner);

            System.out.println("Operaciones disponibles:");
            System.out.println("1. Suma");
            System.out.println("2. Resta");
            System.out.println("3. Multiplicación");
            System.out.println("4. División");
            System.out.print("Elija una operación: ");
            int operacion = (int) leerNumero(scanner);

            double resultado;
            switch (operacion) {
                case 1:
                    resultado = num1 + num2;
                    System.out.println("Resultado suma: " + resultado);
                    break;
                case 2:
                    resultado = num1 - num2;
                    System.out.println("Resultado resta: " + resultado);
                    break;
                case 3:
                    resultado = num1 * num2;
                    System.out.println("Resultado multiplicación: " + resultado);
                    break;
                case 4:
                    if (num2 == 0) {
                        System.out.println("No se puede dividir por cero.");
                    } else {
                        resultado = num1 / num2;
                        System.out.println("Resultado división: " + resultado);
                    }
                    break;
                default:
                    System.out.println("Opción inválida.");
            }

            System.out.print("¿Desea realizar otra operación? (s/n): ");
            String continuar = scanner.next();
            if (!continuar.equalsIgnoreCase("s")) {
                System.out.println("¡Hasta pronto!");
                break;
            }
            System.out.println();
        }
        scanner.close();
    }

    private static double leerNumero(Scanner scanner) {
        while (true) {
            try {
                return Double.parseDouble(scanner.next());
            } catch (NumberFormatException e) {
                System.out.print("Entrada inválida. Intente de nuevo: ");
            }
        }
    }
}