package h316_407;

import java.util.Scanner;

public class HomeW_03_22 {
    public static void main(String[] args) {
        int a_auto[]={2,3,5,8,9};
        int a[];
        int choise;
        Scanner in=new Scanner(System.in);
        System.out.print("使用默认数组: 1  手动输入: 2");
        choise=in.nextInt();
        if(choise==1) { a=a_auto;}
        else { a=BuildArray(in);}
        a=SortArray(a,0,a.length-1);
        PrintArray(a);

        in.close();
    }
    
    //数组排序方法
    static int[] SortArray(int a[],int start,int end){
        int temp,i,j,e;
        temp=a[start];
        i=start;
        j=end;
        while(i<j){
            while((i<j)&&(a[j]>=temp)){j--;}
            e=a[i];
            a[i]=a[j];
            a[j]=e;
            while((i<j)&&(a[i]<=temp)){i++;}
            e=a[i];
            a[i]=a[j];
            a[j]=e;
        }
        if((i-1)>start) a=SortArray(a,start,i-1);
        if((j+1)<end) a=SortArray(a,j+1,end);
        return (a);
    }
    //数组创建方法
    static int[] BuildArray(Scanner in){
        //Scanner in=new Scanner(System.in);
        System.out.print("输入字符串长度  >");
        int n=in.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++){
            System.out.print("请输入第"+(i+1)+"项  >");
            a[i]=in.nextInt();
        }
        System.out.println("构建完成");
        //in.close();
        return a;
    }
    //数组输出方法
    static void PrintArray(int[] array){
        for(int a:array){
            System.out.print(a+" ");
        }
    }

}
