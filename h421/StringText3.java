package h421;

public class StringText3 {
    public static void main(String[] args) {
        String s1="Monday";
        String s2=new String("Monday");

        if(s1==s2){//比较地址值
            System.out.println("s1=s2");
        }
        else{
            System.out.println("s1≠s2");
        }

        if(s1.equals(s2)){//比较字符串内容
            System.out.println("s1 equals s2");
        }
        else{
            System.out.println("s1 does not equals s2");
        }
    }
}
