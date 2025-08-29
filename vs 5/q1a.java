import java.util.*;
public class q1a{
    public static void main(String args[]){
        Scanner  sc = new Scanner(System.in);
        int[] arr = {10,20,30,40};
        int target = sc.nextInt();
        boolean check = true;
        for(int i = 0 ; i < arr.length ;i++){
            if(arr[i]==target){
                check = false;
                break;
                // System.exit(0);
            }}
            
        if(check == true){
            System.out.println("Target is not present");
        } else{System.out.println("Target is present");}
            
    }
}