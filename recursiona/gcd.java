package recursiona;

import java.util.Scanner;

public class gcd {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int a=in.nextInt();
            int b=in.nextInt();
            System.out.println(ggcd(a,b));
        }
    }
    private static int ggcd(int a,int b){
        if(b==0) return a;
        return ggcd(b,a%b);
    }
}
