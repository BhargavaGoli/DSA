package praticequestions;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class capitalize_frequeny {
    public static void main(String[] args) {
        Map<String,Integer> m=new HashMap<>();
        var in=new Scanner(System.in);
        String input=in.nextLine();
        String[] s=input.split("\\s+");
        for(String i : s){

            String op=i.substring(0,1).toUpperCase()+i.substring(1);
            m.put(op,m.getOrDefault(op,0)+1);
        }

        for(Map.Entry<String,Integer> o:m.entrySet()){
            System.out.print(o.getKey()+" "+o.getValue()+" ");
        }

    }
}
// apple sun sun sppain apple apple ornage sun