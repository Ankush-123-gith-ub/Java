import java.util.*;
public class q2 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your first number: ");
        int a = sc.nextInt();
        System.out.print("Enter your second number: ");
        int b = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter your op: ");
        String op = sc.nextLine();
        switch (op) {
            case "*":
                System.out.println(a*b);
                break;
        
            case "/":
                System.out.println(a/b);
                break;
        
            case "-":
                System.out.println(a-b);
                break;
        
            case "+":
                System.out.println(a+b);
                break;
        
            default:
                break;
        }
    }
}
