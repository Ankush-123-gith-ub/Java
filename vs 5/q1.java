import java.util.*;
public class q1{
    public static void main(String args[]){
        Scanner  sc = new Scanner(System.in);
        int[] arr = {10,20,30,40};
        int target = sc.nextInt();
        boolean check = true;
        for(int i = 0 ; i < arr.length ;i++){
            if(arr[i]==target){
                System.out.println("Target is present");
                // break;
                System.exit(0);
            }}
       
        System.out.println("Target is not present");
    }
}