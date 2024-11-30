package ds;

//class llNode{
//    int data;
//    llNode next;
//    llNode(int data){
//        this.data=data;
//
//    }
//}
//class ll{
//    //RECURSIVE
//    public llNode reversell(llNode head){  // 1->2->3
//        if( head==null || head.next==null){
//            return head;
//        }
//        llNode result=reversell(head.next);
//
//        head.next.next=head;
//        head.next=null;
//
//        return result;
//    }
//
//    //ITERATIVE
//    public llNode rev_ll(llNode head){
//        llNode curr=head;
//        llNode prev=null;
//        llNode nextll;
//        while(curr!=null){
//            nextll=curr.next;
//            curr.next=prev;
//
//            prev=curr;
//            curr=nextll;
//        }
//        return prev;
//    }
//    /*
//    1-2-3
//    2-3 1
//    3 2-1
//    null 3-2-1
//     */
//    public void printll(llNode head){
//        while(head!=null) {
//            System.out.print(head.data+" ");
//            head=head.next;
//        }
//    }
//}
//public class LinkedList {
//    public static void main(String[] args){
//        ll obj=new ll();
//        llNode head=new llNode(1);
//        head.next=new llNode(2);
//        head.next.next=new llNode(34);
//        head.next.next.next=new llNode(5);
//
//        llNode res=obj.rev_ll(head);
//        obj.printll(res);
//    }
//}
class lnode{
    int data;
    lnode next;
    lnode(int data){
        this.data=data;
    }
}
class LinkedList{
    public static lnode rev(lnode head){
        lnode cur = head;
        lnode prev=null;
        lnode next;
        while(cur!=null){
            next=cur.next;
            cur.next=prev;

            prev=cur;
            cur=next;
        }
        return prev;
    }
    //recursive
    public static lnode rev_r(lnode head){
        if(head==null || head.next==null) return head;
        lnode res=rev_r(head.next);

        head.next.next=head;
        head.next=null;
        return res;
    }
    public static void print(lnode head){
        while(head!=null){
            System.out.print(head.data+" ");
            head=head.next;
        }
    }

    public static void main(String args[]){
        lnode head=new lnode(2);
        head.next=new lnode(9);
        head.next.next=new lnode(4);

        lnode res=rev_r(head);
        print(res);
    }
}
