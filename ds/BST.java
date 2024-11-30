package ds;



import java.util.LinkedList;
import java.util.Queue;

class bstNode {
    int data;
    bstNode left;
    bstNode right;

    bstNode(int data) {
        this.data = data;
    }
}

public class BST {
    public static bstNode insert(bstNode root, int val) {
        if (root == null) return new bstNode(val);
        if (val < root.data) root.left = insert(root.left, val);
        else root.right = insert(root.right, val);
        return root;
    }

    public static void inorder(bstNode root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);

    }
    public static bstNode lca(bstNode root, bstNode p,bstNode q){
        if(root==null) return null;
        if(q.data<root.data && p.data<root.data) lca(root.left,p,q);
        if(q.data>root.data && p.data>root.data) lca(root.left,p,q);
        return root;
    }

    public static void main(String args[]) {
        int[] a = {10, 13, 1, 4, 20, 8};
        bstNode root = null;
        for (int n : a) root=insert(root, n);
//        inorder(root);
        bstNode res=lca(root,root.left,root.right);
        System.out.print(res.data);

    }

}

//class bstNode{
//    int data;
//    bstNode left;
//    bstNode right;
//    bstNode(int data){
//        this.data=data;
//    }
//}
//
//class op{
//    public bstNode insert(bstNode root, int val){
//        if(root==null) return new bstNode(val);
//
//        if(val<root.data) root.left=insert(root.left,val);
//        else root.right=insert(root.right,val);
//
//        return root;
//    }
//
//    public void inOrder(bstNode root){
//        if(root==null) return;
//
//        inOrder(root.left);
//        System.out.print(root.data+" ");
//        inOrder(root.right);
//    }
//
//    public void levelOrder(bstNode root){
//        if(root==null) return;
//        Queue<bstNode> q=new LinkedList<>();
//        q.add(root);
//        while(!q.isEmpty()){
//            int size=q.size();
//            for(int i=0;i<size;i++){
//                bstNode temp=q.poll();
//                System.out.print(temp.data+" ");
//                if(temp.left!=null) q.add(temp.left);
//                if(temp.right!=null) q.add(temp.right);
//            }
//            System.out.println();
//        }
//    }
//    public bstNode lca(bstNode root,bstNode p,bstNode q){
//        if(root==null) return null;
//        if(p.data<root.data && q.data<root.data) return lca(root.left,p,q);
//        if(p.data>root.data && q.data>root.data) return lca(root.right,p,q);
//
//        return root;
//    }
//    public boolean search(bstNode root, int val){
//        if(root==null ) return false;
//        if(root.data==val) return true;
//        if(val<root.data) return search(root.left,val);
//        if(val>root.data) return search(root.right,val);
//        return false;
//    }
//}
//public class BST{
//    public static void main(String args[]){
//        int values[]={50,45,55,30,47,52,60};
//        bstNode root=null;
//        op obj=new op();
//        for(int v:values) root=obj.insert(root,v);
////        obj.inOrder(root);
////        obj.levelOrder(root);
////        System.out.println();
////        bstNode res=obj.lca(root, root.left.left,root.right.right);
////        System.out.println(res.data);
////
//        if(obj.search(root,55)) System.out.print("found");
//        else System.out.print("not found");
//    }
//}
