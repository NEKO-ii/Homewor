package clock;

import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import javax.swing.*;

public class RunClock{
    public static void main(String[] args) {
        Time time=new Time();
        Thread timenow=new Thread(time);//新建进程
        timenow.start(); //开始进程
    }

}

class Time implements Runnable{
    SimpleDateFormat time1 = new SimpleDateFormat("                     HH : mm : ss");//显示格式一
    SimpleDateFormat time2 = new SimpleDateFormat("yyyy年MM月dd日  hh时mm分ss秒  EEEE");//显示格式二
    Calendar now = Calendar.getInstance();
    int moa;//存储获取的上下午数值
    Date date;
    
    public void run(){
        JFrame window=new JFrame();//窗口定义
        window.setTitle("时钟");
        window.setBounds(500, 500, 450, 140);
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel show=new JPanel(new GridLayout(2,1));//主容器
        JTextArea t1=new JTextArea();//显示一组件
        JTextArea t2=new JTextArea();//显示二组件
        t1.setFont(new Font("微软雅黑",1,25));
        t2.setFont(new Font("微软雅黑",0,20));
        show.add(t1);
        show.add(t2);
        window.add(show);

        while(true){
            date=new Date();
            moa = now.get(Calendar.AM_PM);
            //System.out.println(time.format(date));
            t1.setText(String.valueOf(time1.format(date)));//刷新文本区内容
            t2.setText(String.valueOf(time2.format(date)));//刷新文本区内容
            if(moa==1)t2.append("  下午");
            else t2.append("  上午");
            try{
                Thread.sleep(1000);//刷新间隔时间，单位：毫秒
            }catch(Exception e){}
        }
    }
}