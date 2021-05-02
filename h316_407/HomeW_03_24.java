package h316_407;

import java.util.Scanner;

 class Animal{
    private String name;
    private int age;
    private int leg_num;
    private String color;
    private String action;

    Animal(){}
    Animal(String name,int age,int leg_num,String color,String action){
        this.name=name;
        if(age>0){this.age=age;}
        else{
            System.out.print("年龄数据不合法，请重新输入  > ");
            setAge();
        }
        if(leg_num>=0){this.leg_num=leg_num;}
        else{
            System.out.print("腿数据不合法，请重新输入  > ");
            setLeg_num();
        }
        this.color=color;
        this.action=action;
    }

    public int setAge(int age){
        if(age>0){this.age=age;return 1;}
        else{
            System.out.print("年龄数据不合法");
            return 0;
        }
    }
    public void setAge(){
        int a;
        System.out.print("年龄  > ");
        Scanner in=new Scanner(System.in);
        a=in.nextInt();
        if(a>0){age=a;}
        else{
            System.out.print("年龄数据不合法，请重新输入  ");
            setAge();
        }
        in.close();
    }
    public int setLeg_num(int age){
        if(age>0){this.leg_num=age;return 1;}
        else{
            System.out.print("腿数据不合法");
            return 0;
        }
    }
    public void setLeg_num(){
        int a;
        System.out.print("腿的数量  > ");
        Scanner in=new Scanner(System.in);
        a=in.nextInt();
        if(a>0){leg_num=a;}
        else{
            System.out.print("腿数据不合法，请重新输入  ");
            setLeg_num();
        }
        in.close();
    }

    void read(){
        System.out.println("\nname: "+name
                                    +"\nage: "+age
                                    +"\nnumber of leg: "+leg_num
                                    +"\ncolor: "+color);
    }
    void action(){
        System.out.println("\nA "+name+" can "+action);
    }

}

class HomeW_03_24{
    public static void main(String[] args) {
        Animal cat=new Animal("cat",1,4,"white","say meow~ and bite you");
        Animal bird=new Animal("bird",2,2,"blue","fly and jump");
        Animal snake=new Animal("snake",1,0,"black","climb on the ground");
        cat.read();
        bird.read();
        snake.read();
        cat.action();
        bird.action();
        snake.action();
        cat.setAge();
    }
}