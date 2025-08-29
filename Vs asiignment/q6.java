import java.util.*;

public class q6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;

        while (true) {
            System.out.print("Enter a number: ");
            int num = sc.nextInt();
            if (num < 0) break;
            sum += num;
        }

        System.out.println("Sum of positive numbers = " + sum);
    }
}

