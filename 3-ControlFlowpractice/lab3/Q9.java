import java.util.Scanner;
public class Q9 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int sum=0;
        for(int i=1;i<num;i++){
            if(num%i==0) sum+=i;
        }
        System.out.println(num + ((sum>num) ? " is an Abundant Number" : " is not an Abundant Number"));
    }
}