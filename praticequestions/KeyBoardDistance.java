package praticequestions;

import java.util.HashMap;
import java.util.Map;

public class KeyBoardDistance {
    public static void main(String[] args) {
        String word="HELLO";
        Map<Character,int[]> m=new HashMap<>();
        String[] rows={"QWERTYUIOP","ASDFGHJKL","ZXCVBNM"};
        for(int i=0;i<rows.length;i++){
            for(int j=0;j<rows[i].length();j++){
                m.put(rows[i].charAt(j),new int[]{i,j});
            }
        }

        int dist=0;
        int[] a=m.get('Q');

        for(char c:word.toCharArray()){
            int[] b=m.get(c);
            dist+=Math.abs(b[0]-a[0])+Math.abs(b[1]-a[1]);
            a=b;
        }

        System.out.println(dist);
    }
}
