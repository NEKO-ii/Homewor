package h421;

public class StringText2 {
    public static void main(String[] args) {
        String s="HelloWorld";

        System.out.println("是否和helloWorld相等："+s.equals("helloWorld"));
        System.out.println("是否和helloworld相等："+s.equals("helloworld"));
        System.out.println("是否和helloWorld相等(忽略大小写)："+s.equalsIgnoreCase("helloworld"));
        System.out.println("是否包含or："+s.contains("or"));
        System.out.println("是否以Hel开头："+s.startsWith("Hel"));
        System.out.println("是否为空："+s.isEmpty());
    }
    
}
