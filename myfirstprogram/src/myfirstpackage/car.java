package myfirstpackage;
import java.util.*;
class car{
	
	String model;
	int year;
	
	// method to display
	void display() {
		System.out.println("Model = "+ model + ", Year = " + year);
	}

	public static void main(String args[]){
		Scanner sc= new Scanner (System.in);
		// first object
		car car1 = new car();
		System.out.print("ENTER MODEL1: ");
		car1.model = sc.nextLine();
		System.out.print("ENTER YEAR1: ");
		car1.year = sc.nextInt();
		sc.nextLine();
		//second object
		car car2 = new car();
		System.out.print("ENTER MODEL2: ");
		car2.model = sc.nextLine();
		System.out.print("ENTER YEAR2: ");
		car2.year = sc.nextInt();
		
		// to call out function
		car1.display();
		car2.display();
		
	}
	
}
