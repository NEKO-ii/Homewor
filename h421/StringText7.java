package h421;

public class StringText7 {
    public static void main(String[] args) {
        StringBuffer sb=new StringBuffer();
        System.out.println(sb);
        sb.append(100).append(" hello ").append(true).append(12.5);
        System.out.println(sb);

        sb.insert(10, "world");
        System.out.println("第11个字符后插入world："+sb);

        sb.deleteCharAt(1);
        System.out.println("删除第一个字符："+sb);
    }
}
