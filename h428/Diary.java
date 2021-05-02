package h428;
import java.io.*;
import java.util.Scanner;

public class Diary {
    public static void main(String[] args) throws IOException {
        Scanner keybord=new Scanner(System.in);
        File f=null;
        int order;
        while(true){
            System.out.print("请输入指令：\n"
                                     +"1新建日记本；2选择日记本；3修改日记本内容；4显示日记本内容；5删除日记本\n"
                                     +"（输入0退出程序）"
                                     +"_> ");
            order=keybord.nextInt();
            if(order==0)break;
            if(order==1){
                f=createFile(keybord);
            }
            if(order==2){
                getList();
                f=openDiary(f,keybord);
            }
            if(order==3){
                f=writeDiary(f,keybord);
            }
            if(order==4){
                showDiary(f,keybord);
            }
            if(order==5){
                deleteDiary(f,keybord);
            }
        }
        keybord.close();
    }

    static File createFile(Scanner keybord)throws IOException{
        String filename;
        int q;
        System.out.print("请输入文件名>");
        filename=keybord.next();
        File f=new File("F://NEKO/Code/VS Code/Java/Homework/h428/File",filename);
        if(!f.exists()){f.createNewFile();}
             else{
                 System.out.println("已有日记本，是否覆盖？1：是；2：否  >");
                 q=keybord.nextInt();
                 if(q==1){
                     f.delete();
                     f.createNewFile();
                 }
                 else{
                     System.out.print("请重新输入文件名>");
                     filename=keybord.next();
                     f=new File("F://NEKO/Code/VS Code/Java/Homework/h428/File",filename);
                     if(!f.exists()){f.createNewFile();}
                 }
             }
        //keybord.close();
        return f;
    }
    static void getList(){
        File dir=new File("F://NEKO/Code/VS Code/Java/Homework/h428/File");
        FileAccept fa=new FileAccept();
        fa.setExtendName("txt");
        String filename[]=dir.list(fa);
        System.out.println("当前文件目录：");
        for(String name:filename){
            System.out.println(name);
        }
    }
    static File openDiary(File f,Scanner keybord) throws IOException{
        System.out.print("你要打开的日记本为>");
        String name=keybord.next();
        f=new File("F://NEKO/Code/VS Code/Java/Homework/h428/File",name);
        if(!f.exists()){
            System.out.print("您输入的文件不存在，是否创建？1：是；2：否  >");
            int q=keybord.nextInt();
            if(q==1) {
                f=createFile(keybord);
                System.out.println("日记本已打开");
            }
        }
        else{
            System.out.println("日记本已打开");
        }
        return f;
    }
    static void showDiary(File f,Scanner keybord)throws IOException{
        if(f==null){
            System.out.println("未选择日记本，请先选择日记本");
            getList();
            f=openDiary(f,keybord);
        }
        else{
            BufferedReader output=new BufferedReader(new FileReader(f));
            String s=null;
            if(f.length()==0) System.out.println("（空文件）");
            while((s=output.readLine())!=null){
                System.out.println(s);
            }
            output.close();
        }
    }
    static File writeDiary(File f,Scanner keybord)throws IOException{
        if(f==null){
            System.out.println("未打开日记本，请先打开日记本");
            getList();
            f=openDiary(f,keybord);
        }
        else{
            BufferedWriter input=new BufferedWriter(new FileWriter(f));
            System.out.println("当前日记本内容为：");
            showDiary(f,keybord);
            System.out.println("\n请输入内容(输入\"//\"结束)>");
            while(true){
                String s=keybord.next();
                if("//".equals(s)) break;
                input.write(s);
                input.newLine();
            }
            System.out.println("写入完毕");
            input.close();
        }
        return f;
    }
    static void deleteDiary(File f,Scanner keybord)throws IOException{
        if(f==null){
            System.out.println("未选择日记本，请先选择日记本");
            getList();
            f=openDiary(f,keybord);
        }
        else{
            f.delete();
            System.out.println("删除完成");
        }
    }
    //

}
