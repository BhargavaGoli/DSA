package recursiona;

public class subsequeces {
    public static void main(String args[]){
        String s="ab";
        subsequece(s,0,"");
    }
    private static void subsequece(String s,int index,String cur){
        if(index==s.length()){
            System.out.println(cur);
            return;
        }

        subsequece(s,index+1,cur+s.charAt(index));
        subsequece(s,index+1,cur);
    }
}
/*
(ab,0,) ab,1,b ab,2,
ab,1,a ab,2,a
ab,2,ab

 */