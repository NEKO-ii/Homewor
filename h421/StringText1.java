package h421;

public class StringText1 {
    public static void main(String[] args) {
        String s1=new String();
        s1="abcde";
        System.out.println("通过String()创建："+s1);
        
        byte []b={95,98,99,100};
        String s2=new String(b);
        System.out.println("通过String(byte []byte)创建："+s2);

        String s3=new String(b,1,2);
        System.out.println("通过String(byte []byte,index,index)创建："+s3);

        char ch1[]={'a','b','c','d','e'};
        String s4=new String(ch1);
        System.out.println("通过String(char []value)创建："+s4);

        String s5=new String(ch1,2,3);
        System.out.println("通过String(char []value,index,index)创建："+s5);

        String s6=new String("abcde");
        System.out.println("通过String(String str)创建："+s6);

        String s7="abcdef";
        System.out.println("通过字符串创建："+s7);
    }
}
