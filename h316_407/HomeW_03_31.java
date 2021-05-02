package h316_407;

//Homework_03_31  类的继承

class Animal_{  //这里在Animal类名后面加了一个下划线是因为我的Homework包里之前写过一个Animal类，避免重名报错
    private String name;
    Animal_(){}
    Animal_(String name){
        this.name=name;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name=name;
    }
    public void Speak(){
        System.out.println("My name is"+name);
    }
}

class Dog extends Animal_{
    private int age;
    Dog(){}
    Dog(int age){
        this.age=age;
    }
    public int getAge(){
        return age;
    }
    public void setAge(int age){
        this.age=age;
    }
}

class Sheepdog extends Dog{
    private String action;
    Sheepdog(){}
    Sheepdog(String action){
        this.action=action;
    }
    public String getAction(){
        return action;
    }
    public void setAction(String action){
        this.action=action;
    }
}

class Colliedog extends Sheepdog{
    private String name;  //虽然Animal_类已经有了name变量，这里加一个name是想保存我们自己给狗起的名字（realname）
    Colliedog(String realname,String typename,int age,String action){
        this.name=realname;
        super.setAge(age);
        super.setAction(action);
        super.setName(typename);
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name=name;
    }
    public  void Speak(){
        System.out.println("My name is "+name+", a "+super.getName()+".  My age is "+getAge()+".  I can "+getAction());
    }
}

class Homework_03_31{
    public static void main(String[] args) {
        Colliedog dog1=new Colliedog("dazhuang","Colliedog",4,"take care of the sheep");
        dog1.Speak();
    }
}