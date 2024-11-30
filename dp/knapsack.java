package dp;

//Vijay, an industrialist recently opened a fuel industry .
// There are N numoers oi different category of fuels and each fuel is stored in a fixed size container.
// Size of each container can vary from fuel to fuel .
//Hari, a fuel merchant, Visited Vijay's Industry and he wanted to purchase fuels for his shop. Hari has a limited amount of money (K) and wants to buy fuel.
// Hari will not buy more than one container of any fuel category. Hari wants to maximize the overall volume i.e sum of volume of fuels he buys.
// Your task is to get the maximum overall volume of fuels which Hari can purchase
//Given the number of categories of fuels (N) money units (k) price of container of each category of fuel and volume contained in container for each category,
//NOTE Quantity (volume) of container will be given in the same order as of the price.price

import java.util.Scanner;

//Example 1:
//Input :
// 5
//105
//10 10 40 50 90 -> prices
//10 20 20 50 150 -> container
//Output :
//        170
public class knapsack {
    public static void main(String args[]){
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int k=in.nextInt();
        int[] prices=new int[n];
        int[] container=new int[n];
        for(int i=0;i<n;i++){
            prices[i]=in.nextInt();
        }
        for(int i=0;i<n;i++){
            container[i]=in.nextInt();
        }


        int[] dp=new int[k+1];



        for(int i=0;i<n;i++){
            for(int j=k;j>=prices[i];j--){
                dp[j]=Math.max(dp[j],dp[j-prices[i]]+container[i]);
            }
        }

        System.out.print(dp[k]);
    }


}
