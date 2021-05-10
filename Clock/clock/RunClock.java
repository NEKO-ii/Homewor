package clock;

import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import javax.swing.*;

public class RunClock{
    public static void main(String[] args) {
        Time time=new Time();
        Thread timenow=new Thread(time);//�½�����
        timenow.start(); //��ʼ����
    }

}

class Time implements Runnable{
    SimpleDateFormat time1 = new SimpleDateFormat("                     HH : mm : ss");//��ʾ��ʽһ
    SimpleDateFormat time2 = new SimpleDateFormat("yyyy��MM��dd��  hhʱmm��ss��  EEEE");//��ʾ��ʽ��
    Calendar now = Calendar.getInstance();
    int moa;//�洢��ȡ����������ֵ
    Date date;
    
    public void run(){
        JFrame window=new JFrame();//���ڶ���
        window.setTitle("ʱ��");
        window.setBounds(500, 500, 450, 140);
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel show=new JPanel(new GridLayout(2,1));//������
        JTextArea t1=new JTextArea();//��ʾһ���
        JTextArea t2=new JTextArea();//��ʾ�����
        t1.setFont(new Font("΢���ź�",1,25));
        t2.setFont(new Font("΢���ź�",0,20));
        show.add(t1);
        show.add(t2);
        window.add(show);

        while(true){
            date=new Date();
            moa = now.get(Calendar.AM_PM);
            //System.out.println(time.format(date));
            t1.setText(String.valueOf(time1.format(date)));//ˢ���ı�������
            t2.setText(String.valueOf(time2.format(date)));//ˢ���ı�������
            if(moa==1)t2.append("  ����");
            else t2.append("  ����");
            try{
                Thread.sleep(1000);//ˢ�¼��ʱ�䣬��λ������
            }catch(Exception e){}
        }
    }
}