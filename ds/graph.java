package ds;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
//
//public class graph {
//    static class edge{
//        int src;
//        int dest;
//        edge(int src,int dest){
//            this.src=src;
//            this.dest=dest;
//        }
//    }
//    public static void create(List<ArrayList<edge>> graph){
//        for(int i=0;i<4;i++){
//            graph.add(new ArrayList<edge>());
//        }
//        graph.get(0).add(new edge(0,2));
//
//        graph.get(1).add(new edge(1,2));
//        graph.get(1).add(new edge(1,3));
//
//        graph.get(2).add(new edge(2,0));
//        graph.get(2).add(new edge(2,1));
//        graph.get(2).add(new edge(2,3));
//
//        graph.get(3).add(new edge(3,1));
//        graph.get(3).add(new edge(3,2));
//
//    }
//
//    public static void bfs(List<ArrayList<edge>> graph,int v,boolean vis[]){
//        Queue<Integer> q=new LinkedList<>();
//
//        q.add(2);
//        while(!q.isEmpty()){
//            int curr=q.poll();
//            if(vis[curr]==false){
//                System.out.print(curr+" ");
//                vis[curr]=true;
//
//                for(int i=0;i<graph.get(curr).size();i++){
//                    edge e=graph.get(curr).get(i);
//                    q.add(e.dest);
//                }
//            }
//        }
//    }
//
//    public static void dfs(List<ArrayList<edge>> graph,boolean vis[],int curr){
//        System.out.print(curr+" ");
//        vis[curr]=true;
//        for(int i=0;i<graph.get(curr).size();i++){
//            edge e=graph.get(curr).get(i);
//            if(vis[e.dest]==false)
//              dfs(graph,vis,e.dest);
//        }
//    }
//    public static void main(String args[]){
//            int v=4;
//            List<ArrayList<edge>> graph=new ArrayList<>();
//            create(graph);
//            boolean vis[]=new boolean[v];
////            for(edge n:graph.get(2)){
////                System.out.print(n.dest+" ");
////            }System.out.println();
////            bfs(graph,v,vis);
//
//            dfs(graph,vis,0);
//    }
//}
class edge{
    int src;
    int dest;
    edge(int src,int dest){
        this.src=src;
        this.dest=dest;
    }
}
class graph{
    public static void build(List<List<edge>> graph,int n){
        for(int i=0;i<n;i++){
            graph.add(new ArrayList<>());
        }

        graph.get(0).add(new edge(0,1));
        graph.get(0).add(new edge(0,2));

        graph.get(1).add(new edge(1,0));
        graph.get(1).add(new edge(1,3));

        graph.get(2).add(new edge(2,0));
        graph.get(2).add(new edge(2,4));

        graph.get(3).add(new edge(3,1));
        graph.get(3).add(new edge(3,4));

        graph.get(4).add(new edge(4,2));
        graph.get(4).add(new edge(4,3));
    }

    public static void bfs(List<List<edge>> g,boolean[] vis){
        Queue<Integer> q=new LinkedList<>();
        q.add(0);
        while(!q.isEmpty()) {
            int cur = q.poll();
            if (!vis[cur]) {
                System.out.print(cur + " ");
                vis[cur] = true;

                for (int i = 0; i < g.get(cur).size(); i++) {
                    edge e = g.get(cur).get(i);
                    q.add(e.dest);
                }
            }
        }
    }


    public static void dfs(List<List<edge>> g,boolean[] vis,int cur){
        if(vis[cur]==true) return;
        System.out.print(cur+" ");

        vis[cur]=true;
        for(int i=0;i<g.get(cur).size();i++){
            edge e=g.get(cur).get(i);
            if(!vis[e.dest]){
                dfs(g,vis,e.dest);
            }
        }
    }


    public static void main (String args[]){
    /*     1--3
         /    |
        0     |
         \    |
           2--4
      */
        int n=5;
        List<List<edge>> graph=new ArrayList<>();
        build(graph, n);
        boolean[] vis=new boolean[n];
        dfs(graph,vis,0);
    }
}