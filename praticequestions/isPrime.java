package praticequestions;

import java.util.Scanner;

public class isPrime {
    public static void main(String[] args) {
        var in=new Scanner(System.in);
        int n=in.nextInt();
        boolean res=isprime(n);
        System.out.print(res);
    }
    private static boolean isprime(int n){
        if(n==0 || n==1) return false;
        if(n<=3) return true;
        if(n%2==0 || n%3==0) return false;
        for(int i=5;i*i<n;i+=6){
            if(n%i==0|| n%(i+2)==0) return false;
        }
        return true;
    }
}
