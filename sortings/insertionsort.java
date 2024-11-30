package sortings;

import java.util.Random;

public class insertionsort {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] a=new int[10];
        int n=a.length;
        for(int i=0;i<n;i++){
            a[i]=rand.nextInt(10);
        }
        print(a);
        
        for(int i=1;i<n;i++){
            int key =a[i];
            int j=i-1;

            while(j>=0 && a[j]>key){
                a[j+1]=a[j];
                j=j-1;
            }
            a[j+1]=key;
        }
        System.out.println();
        
        print(a);
    }
    private static void print(int[] a){
        for(int s:a){
            System.out.print(s+" ");
        }
    }

}
