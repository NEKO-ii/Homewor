
import java.io.*;

public class Text2 {
    public static void main(String[] args)throws Exception {
        FileOutputStream o=new FileOutputStream("out.txt");
        String s="LNTU";
        byte b[]=s.getBytes();
        for(int i=0;i<b.length;i++){
            o.write(b[i]);
        }
        o.close();
    }
}
