package sortings;

import java.util.Random;

public class selectionsort {
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
        int min;
        for(int i=0;i<n-1;i++){
            min=i;
            for(int j=i+1;j<n;j++){
                if(a[j]<a[min]){
                    min=j;
                }
                
            }   
            swap(a,i,min);
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
