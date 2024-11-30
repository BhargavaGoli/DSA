// Sample test cases :
// Input 1 :

// rohit is a cricket player

// Output 1 :

// Rohit Is A Cricket Player 

// Input 2 :

// CAMEL cAsE

// Output 2 :

// Camel Case 




package praticequestions;



import java.util.*;
public class capitalize {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            String input=in.nextLine();
            
            String[] s=input.split(" ");

            for (String item : s) {
                String start = item.substring(0, 1).toUpperCase();
                String remaining = item.substring(1);
                System.out.print(start+remaining+" ");
            }
        }
    }
}
