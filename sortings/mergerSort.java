package sortings;

import java.util.Arrays;

public class mergerSort {
//    public static void main(String[] args) {
//        int[] a={9,0,9,8,2};
//        mergeSort(a,0,a.length-1);
//        System.out.println(Arrays.toString(a));
//    }
//    private static void mergeSort(int[] a,int left,int right){
//        if(left<right){
//            int mid=(left+right)/2;
//            mergeSort(a,left,mid);
//            mergeSort(a,mid+1,right);
//            merge(a,left,mid,right);
//        }
//    }
//    private static void merge(int[] a, int left, int mid , int right){
//        int n1=mid-left+1;
//        int n2=right-mid;
//
//        int[] larr=new int[n1];
//        int[] rarr=new int[n2];
//
//        for(int i=0;i<n1;i++) larr[i]=a[left+i];
//        for(int i=0;i<n2;i++) rarr[i]=a[mid+1+i];
//
//        int i=0;
//        int j=0;
//        int k=left;
//        while(i<n1 && j<n2){
//            if(larr[i]<rarr[j]){
//                a[k]=larr[i];
//                i++;
//            }
//            else{
//                a[k]=rarr[j];
//                j++;
//            }
//            k++;
//        }
//        while(i<n1){
//            a[k]=larr[i];
//            i++;
//            k++;
//        }
//        while(j<n2){
//            a[k]=rarr[j];
//            j++;
//            k++;
//        }
//    }

    public static void main(String[] args) {
        int a[]={3,5,2,1,4};
        mergeSort(a,0,a.length-1);
        System.out.println(Arrays.toString(a));
    }
    public static void mergeSort(int[] a,int l, int r){
        if(l<r){
            int mid=(l+r)/2;
            mergeSort(a,l,mid);
            mergeSort(a,mid+1,r);
            merge(a,l,mid,r);
        }
    }
    public static void merge(int[] a,int l, int mid,int r){
        int n1=mid-l+1;
        int n2=r-mid;

        int[] x=new int[n1];
        int[] y=new int[n2];

        for(int i=0;i<n1;i++){
            x[i]=a[l+i];
        }
        for(int i=0;i<n2;i++) y[i]=a[mid+1+i];

        int i=0;
        int j=0;
        int k=l;

        while(i<n1 && j<n2){
            if(x[i]<y[j]) {
                a[k++]=x[i++];
            }
            else a[k++]=y[j++];
        }

        while(i<n1) a[k++]=x[i++];
        while(j<n2) a[k++]=y[j++];
    }
}
