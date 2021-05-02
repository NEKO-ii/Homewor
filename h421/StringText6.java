package h421;

public class StringText6 {
    public static void main(String[] args) {
        String s="HelloWorld";
        System.out.println("l替换为x："+s.replace("l","x"));
        System.out.println("World换成China："+s.replace("World","China"));

        String ages="20-30";
        String strArray[]=ages.split("-");
        for(int i=0;i<strArray.length;i++){
            System.out.println("数组中索引为"+i+"处的值为："+strArray[i]);
        }

        String name="   admin hello  ";
        name=name.trim();
        name=name.replace(" ","");
        System.out.println(name);

        String s1="hello";
        String s2="aello";
        System.out.println(s1.compareTo(s2));
    }
}
