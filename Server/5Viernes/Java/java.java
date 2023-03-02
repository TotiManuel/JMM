import java.util.Scanner;
public class java{
	public static void main(String args[]){
		Scanner myObj = new Scanner(System.in); //Crear el Input
		System.out.println("Hola Mundo"); //Output
		String userName = myObj.nextLine(); //Pedir el Input
		System.out.println("Username is: " + userName);
	}
}
