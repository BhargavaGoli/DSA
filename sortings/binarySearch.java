package sortings;

public class binarySearch {
    public static void main(String[] args){
        int[] a={4,5,6,7,8,9};
        System.out.println(binarySearch(a,0));
    }
    private static int binarySearch(int[] a, int element){
        int l=0;
        int h=a.length-1;
        int middle ;
        while(l<=h){
            middle =(l+h)/2;
            if(a[middle]==element) return middle;
            else if(a[middle]>element) h=middle-1;
            else l=middle+1;
        }
        return -1;
    }
}
