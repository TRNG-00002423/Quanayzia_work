/**
 * Week 2 Exercise — Calculator with static methods and overloads.
 *
 * Division by zero strategy (TODO — choose and implement):
 *   Option A: print error message and return Double.NaN
 *   Option B: return 0.0 and document why (not ideal for production)
 *
 * Compile: javac Calculator.java
 * Run:     java Calculator
 */

public class Calculator {

    public static double add(double a, double b) {

        return a + b;
}

    public static double add(double a, double b, double c) {
	 return add(add(a, b), c);
 }

    public static double subtract(double a, double b) {
        return a - b;
}

    public static double multiply(double a, double b) {


        return a * b;
    }

    public static double divide(double a, double b) {
       if (b == 0) {
            System.out.println("Divide by zero error");
            return Double.NaN;
    }

      return a / b;


    }

    public static void main(String[] args) {

        if (args.length == 3) {

            double a = Double.parseDouble(args[0]);

            double b = Double.parseDouble(args[1]);

            double c = Double.parseDouble(args[2]);

            System.out.println("add(a,b,c): " + add(a, b, c));

        }else if (args.length == 2){

            double a = Double.parseDouble(args[0]);

            double b = Double.parseDouble(args[1]);

            System.out.println("add(a,b): " + add(a, b));

            System.out.println("subtract(a,b): " + subtract(a, b));

            System.out.println("multiply(a,b): " + multiply(a, b));

            System.out.println("divide(a,b): " + divide(a, b));
	}else {

            System.out.println("Use:");
            System.out.println("java Calculator <a> <b>");
            System.out.println("java Calculator <a> <b> <c>");
    }
  }
}