package ds;

import java.util.LinkedList;
import java.util.Queue;

import static ds.tree.op.lca;


class treeNode{
    int data;
    treeNode right;
    treeNode left;
    treeNode(int data){
        this.data=data;
    }
}


class tree{
    static class op{
        static int i=-1;
        public static treeNode buildtree(int a[]){
            i++;
            if(a[i]==-1) return null;
            treeNode newNode=new treeNode(a[i]);
            newNode.left=buildtree(a);
            newNode.right=buildtree(a);
            return newNode;
        }

        public static void preorder(treeNode root){
            if(root==null) return;
            System.out.print(root.data+" ");
            preorder(root.left);
            preorder(root.right);
        }
        public static void inorder(treeNode root){
            if(root==null) return;

            preorder(root.left);
            System.out.print(root.data+" ");
            preorder(root.right);
        }

        public static void levelOrder(treeNode root){
            Queue<treeNode> q=new LinkedList<>();
            q.add(root);
            while(!q.isEmpty()){
                int size=q.size();
                for(int i=0;i<size;i++){
                    treeNode t=q.poll();
                    System.out.print(t.data+" ");
                    if(t.left!=null) q.add(t.left);
                    if(t.right!=null) q.add(t.right);
                }
                System.out.println();
            }
        }
        public static int countNodes(treeNode root){
            if(root==null) return 0;
            return countNodes(root.left)+countNodes(root.right)+1;
        }
        static int d=0;
        public static int height(treeNode root){
            if(root==null) return 0;
            int left=height(root.left);
            int right=height(root.right);
            int h=Math.max(left,right);
            d=Math.max(d,left+right+1);
            return h+1;
        }
        public static int diameter (treeNode root){
            height(root);
            return d;
        }
        public static treeNode lca(treeNode root,treeNode p,treeNode q){
            if(root==null || root==p || root == q) return root;
            treeNode left=lca(root.left,p,q);
            treeNode right=lca(root.right,p,q);
            if(left!=null && right!=null) return root;
            if(left!=null) return left;
            else return right;
        }

    }
    public static void main(String args[]){
        int[] a={1,2,-1,-1,3,-1,-1};

        treeNode root=op.buildtree(a);
//        op.inorder(root);
//        op.levelOrder(root);
        treeNode res=lca(root,null,root.right);
        System.out.print(res.data);

    }
}