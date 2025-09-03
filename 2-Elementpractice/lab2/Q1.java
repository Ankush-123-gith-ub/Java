package lab2;
import java.util.Scanner;

public class Q1 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        double number1, number2;
        number1 = sc.nextDouble();
        number2 = sc.nextDouble();
        double add = number1 + number2;
        double sub = number1 - number2;
        double mul = number1 * number2;
        double div = number1 / number2;
        System.out.println("The addition, subtraction, multiplication and division value of 2 numbers " 
            + number1 + " and " + number2 + " is " + add + ", " + sub + ", " + mul + ", " + div);
    }
}
