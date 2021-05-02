//日记本程序
//已知问题：win10系统在记事本中无法写入中文
//问题未解决

package h428_2;
import java.io.*;
import java.util.Scanner;

public class Diary {
    public static void main(String[] args)throws IOException {
        //参数定义
        Scanner keybord=new Scanner(System.in);//方便输入int型数据
        File f=null;//文件
        BufferedWriter input=null;//输入流
        int order;//指令选择
        String filename=null;//文件名
        String path="F://NEKO/Code/VS Code/Java/Homework/h428_2/File";//日记本保存目录
        File dir=new File(path);//目标目录
        FileAccept fa=new FileAccept();
        fa.setExtendName("txt");//目标扩展名
        String choose;//打开和删除文件的选择文件名
        
        //执行体
        while(true){
            System.out.print("\n请输入指令：\n"
            +"1：创建日记本；2：打开日记本；3：编辑日记本；4：保存日记本；5：关闭日记本；6：删除日记本\n"
            +"(输入0退出程序)  _>");
            order=keybord.nextInt();
            
            if(order==0)break;//输入0跳出循环（退出程序）
            if(order==1){//创建
                System.out.print("请输入文件名>");
                filename=null;
                filename=keybord.next();
                f=new File(path,filename);
                if(!f.exists()){
                    f.createNewFile();
                    System.out.println("日记本 "+filename+" 创建成功");
                }
                else System.out.println("同名文件已存在");
            }
            if(order==2){//打开
                //给出当前文件列表
                String s[]=dir.list(fa);
                System.out.println("当前文件目录：");
                if(s.length==0)System.out.println("(空目录)");
                else{
                    for(String name:s){
                        System.out.println(name);
                    }
                    //询问打开文件
                    System.out.print("需要打开的日记本为>");
                    choose=keybord.next();
                    f=new File(path,choose);
                    if(!f.exists()){
                        System.out.println("日记本不存在，重新输入");
                        input=null;
                    }
                    else{
                        OutputStreamWriter osw=new OutputStreamWriter(new FileOutputStream(f,true),"UTF-8");//设置新内容追加或覆盖true为追加，设置格式
                        input=new BufferedWriter(osw);
                        //BufferedWriter input=new BufferedWriter(new FileWriter(f,true));
                        if(input!=null)System.out.println("日记本已打开");
                    }
                }
            }
            if(order==3){//修改
                //如果日记本未打开给出提示
                if(input==null){
                    System.out.println("日记本未打开，请先打开日记本");
                }
                else{
                    //读取当前日记本内容
                    System.out.println("当前日记本内容为：");
                    InputStreamReader isr = new InputStreamReader(new FileInputStream(f),"UTF-8");//设置文件读取格式
                    BufferedReader output=new BufferedReader(isr);
                    //BufferedReader output=new BufferedReader(new FileReader(f));
                    String s=null;
                    if(f.length()==0) System.out.println("（空文件）");
                    while((s=output.readLine())!=null){
                        System.out.println(s);
                    }
                    output.close();
                    System.out.println("\n请输入内容(输入\"//\"结束)>");
                    while(true){
                        String in=keybord.nextLine();
                        if("//".equals(in)) break;
                        input.write(in);
                        input.newLine();
                    }
                   System.out.println("写入完毕");
                }
            }
            if(order==4){//保存
                if(input==null) System.out.println("日记本未打开，请先打开日记本");
                else{
                    input.flush();
                    System.out.println("日记本已保存");
                }
            }
            if(order==5){//关闭
                if(input==null) System.out.println("日记本未打开，请先打开日记本");
                else{
                    input.close();
                    input=null;
                    System.out.println("日记本已关闭");
                }
            }
            if(order==6){//删除
                String s[]=dir.list(fa);
                System.out.println("当前文件目录：");
                if(s.length==0)System.out.println("(空目录)");
                else{
                    for(String name:s){
                        System.out.println(name);
                    }
                }
                //询问删除文件
                System.out.print("需要删除的日记本为>");
                filename=null;
                choose=keybord.next();
                f=new File(path,choose);
                if(!f.exists())System.out.println("日记本不存在，重新输入");
                else{
                    if(input!=null) input.close();//需要先关闭再删除，不然会因为占用而删除失败
                    f.delete();
                    f=null;
                    System.out.println("日记本已删除");
                }
            }
            //else{
            //    System.out.println("指令不存在，重新输入");
            //}
        }
        keybord.close();
    }
}
