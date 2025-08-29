import java.util.*;
public class q2{
    public static void main(String args[]){
        Scanner  sc = new Scanner(System.in);
        int[] arr = {10,20,30,60};
        // int target = sc.nextInt();
        int count = 0;
        for(int i = 0 ; i < arr.length ;i++){
            if(arr[i] % 2==0 || arr[i]%3==0){
               count++;
               
            }}
       
        System.out.println("The numbers divisible by 2 & 3 is: "+count);
            
    }
}