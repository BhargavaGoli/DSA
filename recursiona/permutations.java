package recursiona;
import java.util.*;
import java.util.Scanner;

class permutations{
    public static void main(String args[]){
        Scanner in=new Scanner(System.in);
        String s=in.next();
        generatepermutation(s,"");
        in.close();
    }

    private static void generatepermutation(String s, String string) {
        if(s.length()==0) {
            System.out.println(string);
            return;
        }

        for(int i=0;i<s.length();i++){
            char curchar=s.charAt(i);
            String newstr=s.substring(0,i)+s.substring(i+1);
            generatepermutation(newstr, string+curchar);
        }

    }
//    public static void main(String[] args) {
//        String word="abc";
//        List<List<Character>> res=new ArrayList<>();
//        backtrack(res,new ArrayList<>(), word);
//
////        res.forEach(System.out::println);
//        res.forEach(System.out::println);
//    }
//    public static void backtrack(List<List<Character>> res, List<Character> l, String word){
//        if(l.size()==word.length()){
//            res.add(new ArrayList<>(l));
//            return;
//        }
//
//        for(Character c:word.toCharArray()){
//            if(l.contains(c)) continue;
//            l.add(c);
//            backtrack(res,l,word);
//            l.remove(l.size()-1);
//        }
//    }

    
}
