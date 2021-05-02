package h421;

public class StringText4 {
    public static void main(String[] args) {
        String s="HelloWorld";
        System.out.println("字符串长度："+s.length());
        System.out.println("第2个字符是什么："+s.charAt(1));
        System.out.println("l第一次出现的位置："+s.indexOf('W'));
        System.out.println("从第五个字符到结尾的字符串是："+s.substring(4));
        System.out.println("从第五个到第八个字符组成的字符串为："+s.substring(4, 8));
    }
}
