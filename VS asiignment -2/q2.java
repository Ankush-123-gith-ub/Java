import java.util.*;
class q2{
	
	String model;
	int year;
	static int numberofobjects = 0;

	// method to display
	void display() {
		System.out.println("Model = "+ model + ", Year = " + year);

	}

	public static void main(String args[]){
		Scanner sc= new Scanner (System.in);
		// first object
		q2 car1 = new q2();
		System.out.print("ENTER MODEL1: ");
		car1.model = sc.nextLine();
		System.out.print("ENTER YEAR1: ");
		car1.year = sc.nextInt();
		sc.nextLine();
		//second object
		q2 car2 = new q2();
		System.out.print("ENTER MODEL2: ");
		car2.model = sc.nextLine();
		System.out.print("ENTER YEAR2: ");
		car2.year = sc.nextInt();
		
		// to call out function
		car1.display();
		car2.display();
    
		
	}
       

	
}

