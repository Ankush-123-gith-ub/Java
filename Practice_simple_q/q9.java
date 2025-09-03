import java.util.*;
public class q9 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String op ;
        do{
            op = sc.nextLine();
            switch(op){
                case "1":
                System.out.println("yes");
                break;
                case "2":
                System.out.println("hha");
                break;
                case "3":
                System.out.println("hmm");
                break;
                case "4":
                System.out.println("are");
                break;
                default:
                System.out.println("Invalid choice!");
            }

        }while(!op.equals("exit"));
    }
}
