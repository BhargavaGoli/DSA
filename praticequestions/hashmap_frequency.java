package praticequestions;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class hashmap_frequency {
    public static void main(String args[]){
        try (Scanner in = new Scanner(System.in)) {
            in.nextLine();
            String s=in.nextLine();
            String[] a=s.split(" ");
            
            Map<String, Integer> m=new HashMap<>();
            
            for(String i:a) {
                m.put(i, m.getOrDefault(i,0)+1);
            }
            for(Map.Entry<String,Integer> r: m.entrySet()){
                System.out.println(r.getKey()+" "+r.getValue());
            }
        }
    }
    

}
