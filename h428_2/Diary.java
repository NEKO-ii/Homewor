//�ռǱ�����
//��֪���⣺ʹ��VScode�ڼ��±����޷�д������
//�����ѽ��2021.05.04

package h428_2;
import java.io.*;
import java.util.Scanner;

public class Diary {
    public static void main(String[] args)throws IOException {
        //��������
        Scanner keybord=new Scanner(System.in);//��������int������
        File f=null;//�ļ�
        BufferedWriter input=null;//������
        int order;//ָ��ѡ��
        String filename=null;//�ļ���
        String path="F://NEKO/Code/VS Code/Java/Homework/h428_2/File";//�ռǱ�����Ŀ¼
        File dir=new File(path);//Ŀ��Ŀ¼
        FileAccept fa=new FileAccept();
        fa.setExtendName("txt");//Ŀ����չ��
        String choose;//�򿪺�ɾ���ļ���ѡ���ļ���
        
        //ִ����
        while(true){
            System.out.print("\n������ָ�\n"
            +"1���������±���2�����ռǱ���3���༭�ռǱ���4�������ռǱ���5���ر��ռǱ���6��ɾ���ռǱ�\n"
            +"(����0�˳�����)  _>");
            order=keybord.nextInt();
            
            if(order==0)break;//����0����ѭ�����˳�����
            if(order==1){//����
                System.out.print("�������ļ���>");
                filename=null;
                filename=keybord.next();
                f=new File(path,filename);
                if(!f.exists()){
                    f.createNewFile();
                    System.out.println("�ռǱ� "+filename+" �����ɹ�");
                }
                else System.out.println("ͬ���ļ��Ѵ���");
            }
            if(order==2){//��
                //������ǰ�ļ��б�
                String s[]=dir.list(fa);
                System.out.println("��ǰ�ļ�Ŀ¼��");
                if(s.length==0)System.out.println("(��Ŀ¼)");
                else{
                    for(String name:s){
                        System.out.println(name);
                    }
                    //ѯ�ʴ��ļ�
                    System.out.print("��Ҫ�򿪵��ռǱ�Ϊ>");
                    choose=keybord.next();
                    f=new File(path,choose);
                    if(!f.exists()){
                        System.out.println("�ռǱ������ڣ���������");
                        input=null;
                    }
                    else{
                        OutputStreamWriter osw=new OutputStreamWriter(new FileOutputStream(f,true),"UTF-8");//����������׷�ӻ򸲸�trueΪ׷�ӣ����ø�ʽ
                        input=new BufferedWriter(osw);
                        //BufferedWriter input=new BufferedWriter(new FileWriter(f,true));
                        if(input!=null)System.out.println("�ռǱ��Ѵ�");
                    }
                }
            }
            if(order==3){//�޸�
                //����ռǱ�δ�򿪸�����ʾ
                if(input==null){
                    System.out.println("�ռǱ�δ�򿪣����ȴ��ռǱ�");
                }
                else{
                    //��ȡ��ǰ�ռǱ�����
                    System.out.println("��ǰ�ռǱ�����Ϊ��");
                    InputStreamReader isr = new InputStreamReader(new FileInputStream(f),"UTF-8");//�����ļ���ȡ��ʽ
                    BufferedReader output=new BufferedReader(isr);
                    //BufferedReader output=new BufferedReader(new FileReader(f));
                    String s=null;
                    if(f.length()==0) System.out.println("�����ļ���");
                    while((s=output.readLine())!=null){
                        System.out.println(s);
                    }
                    output.close();
                    System.out.println("\n����������(����\"//\"����)>");
                    while(true){
                        String in=keybord.nextLine();
                        if("//".equals(in)) break;
                        input.write(in);
                        input.newLine();
                        input.flush();
                    }
                   System.out.println("д�����");
                }
            }
            if(order==4){//����
                if(input==null) System.out.println("�ռǱ�δ�򿪣����ȴ��ռǱ�");
                else{
                    input.flush();
                    System.out.println("�ռǱ��ѱ���");
                }
            }
            if(order==5){//�ر�
                if(input==null) System.out.println("�ռǱ�δ�򿪣����ȴ��ռǱ�");
                else{
                    input.close();
                    input=null;
                    System.out.println("�ռǱ��ѹر�");
                }
            }
            if(order==6){//ɾ��
                String s[]=dir.list(fa);
                System.out.println("��ǰ�ļ�Ŀ¼��");
                if(s.length==0)System.out.println("(��Ŀ¼)");
                else{
                    for(String name:s){
                        System.out.println(name);
                    }
                }
                //ѯ��ɾ���ļ�
                System.out.print("��Ҫɾ�����ռǱ�Ϊ>");
                filename=null;
                choose=keybord.next();
                f=new File(path,choose);
                if(!f.exists())System.out.println("�ռǱ������ڣ���������");
                else{
                    if(input!=null) input.close();//��Ҫ�ȹر���ɾ������Ȼ����Ϊռ�ö�ɾ��ʧ��
                    f.delete();
                    f=null;
                    System.out.println("�ռǱ���ɾ��");
                }
            }
            //else{
            //    System.out.println("ָ����ڣ���������");
            //}
        }
        keybord.close();
    }
}