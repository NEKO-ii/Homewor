package h421;

public class StringText5 {
    public static void main(String[] args) {
        String s="HelloWorld";
        char chs[]=s.toCharArray();

        for (int i=1;i<chs.length;i++){
            System.out.println(chs[i]);
        }

        char chs2[]={'a','b','c','中','国'};
        System.out.println("数组转字符串："+String.copyValueOf(chs2));

        int i=100;
        System.out.println("整形转字符串："+String.valueOf(i));

        System.out.println("小写："+s.toLowerCase());
        System.out.println("大写："+s.toUpperCase());
        System.out.println("与LNTU拼接："+s.concat("LNTU"));
    }
}
