// import java.util.*;

// public class q3 {
//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter month number (1-12): ");
//         int month = sc.nextInt();

//         int days;

//         switch (month) {
//             case 1: case 3: case 5: case 7: case 8: case 10: case 12:
//                 days = 31;
//                 break;

//             case 4: case 6: case 9: case 11:
//                 days = 30;
//                 break;

//             case 2:
//                 days = 28; // Non-leap year
//                 break;

//             default:
//                 days = -1; // Invalid month
//         }

//         if (days == -1) {
//             System.out.println("Invalid month number!");
//         } else {
//             System.out.println("Number of days = " + days);
//         }
//     }
// }

import java.util.*;
