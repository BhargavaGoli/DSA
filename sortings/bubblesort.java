package sortings;

import java.util.Random;



public class bubblesort {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] a=new int[10];
        int n=a.length;
        for(int i=0;i<n;i++){
            a[i]=rand.nextInt(100);
        }
        for(int s:a){
            System.out.print(s+" ");
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n-i-1;j++){
                if(a[j]>a[j+1]){
                    swap(a,j,j+1);
                }
            }
        }
        System.out.println();
        System.out.println("after sorting");
        for(int s:a){
            System.out.print(s+" ");
        }

    }

    private static void swap(int[] a, int i, int j) {
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
}
