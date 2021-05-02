
import java.io.*;

public class Text1 {
    public static void main(String[] args)throws Exception {
        InputStream in=null;
        try{
            in=new FileInputStream("out.txt");
            int b=0;
            while(true){
            b=in.read();
            if(b==-1){break;}
            System.out.println(b);
            }
        }finally{
            if(in!=null){in.close();}
        }
        
        
    }
}
