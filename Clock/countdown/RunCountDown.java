package countdown;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.math.BigDecimal;

public class RunCountDown{
    public static void main(String[] args) {
        Run mainRun=new Run();
        mainRun.setTitle("倒计时设置");
    }
}

class Run extends JFrame implements ActionListener{
    JTextField t1,t2,t3,t4,t;
    int day,hour,min,sec;//保存设置时间
    int time=0;//保存总时长(单位：秒)
    String name;//保存事件名称
    
    Run(){
        init();
        setBounds(500, 500, 450, 140);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    void init() {
        JPanel show=new JPanel(new GridLayout(2,1));//主容器
        JPanel p1=new JPanel();//上部面板
        JPanel p2=new JPanel();//下部面板

        JLabel l1,l2,l3,l4,l5,l6;
        JButton addNewRun;

        t=new JTextField(10);
        t1=new JTextField(5);
        t2=new JTextField(5);
        t3=new JTextField(5);
        t4=new JTextField(5);
        
        l1=new JLabel(" 天 ");
        l2=new JLabel(" 时 ");
        l3=new JLabel(" 分 ");
        l4=new JLabel(" 秒 ");
        l5=new JLabel(" 设置倒计时 ");
        l6=new JLabel(" 事件名 ");

        addNewRun=new JButton("添加进程");
        addNewRun.addActionListener(this);

        p1.add(l5);
        p1.add(new JLabel("     "));
        p1.add(l6);
        p1.add(t);
        p1.add(addNewRun);

        p2.add(t1);
        p2.add(l1);
        p2.add(t2);
        p2.add(l2);
        p2.add(t3);
        p2.add(l3);
        p2.add(t4);
        p2.add(l4);

        show.add(p1);
        show.add(p2);
        add(show);
        
    }
    public void actionPerformed(ActionEvent e) {
        boolean n=true;//是否符合创建进程的条件
        try{
            if(!"".equals(t.getText())) {//事件名称不能为空
                name=t.getText();
            }
            else{
                n=false;
                JOptionPane.showMessageDialog(null, "事件名不能为空","警告", JOptionPane.WARNING_MESSAGE);
            }
            if(!"".equals(t1.getText())) {
                if(isNum(t1.getText())) {t1.setForeground(Color.BLACK);day= Integer.parseInt(t1.getText().trim());}
                else {day=0;n=false;t1.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            else day=0;
            if(!"".equals(t2.getText())) {
                if(isNum(t2.getText())) {t2.setForeground(Color.BLACK);hour= Integer.parseInt(t2.getText().trim());}
                else {hour=0;n=false;t2.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            else hour=0;
            if(!"".equals(t3.getText())) {
                if(isNum(t3.getText())) {t3.setForeground(Color.BLACK);min= Integer.parseInt(t3.getText().trim());}
                else {min=0;n=false;t3.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            else min=0;
            if(!"".equals(t4.getText())) {
                if(isNum(t4.getText())) {t4.setForeground(Color.BLACK);sec= Integer.parseInt(t4.getText().trim());}
                else {sec=0;n=false;t4.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            else sec=0;
        }catch(Exception ex){}
        
        if(n==true){
            time=sec+60*min+3600*hour+86400*day;
            Window win=new Window();
            win.setName(name);
            win.setTime(time);
            Thread thr=new Thread(win);//创建进程
            thr.start();
        }
    }
    public static boolean isNum(String str) {//判断输入是否为数字
        try {
            String bigStr = new BigDecimal(str).toString();
        } catch (Exception e) {
            return false;//异常 说明包含非数字。
        }
        return true;
    }
}

class Window implements Runnable{
    String name;
    int time;
    int d,h,m,s;//显示时间
    public void setName(String name){
        this.name=name;
    }
    public void setTime(int time){
        this.time=time;
    }
    public void run(){
        JFrame window=new JFrame();//窗口定义
        window.setTitle("任务倒计时");
        window.setBounds(500, 500, 350, 100);
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);//关闭副窗口时仅释放副窗口资源，不关闭主窗口
        
        JPanel show=new JPanel(new GridLayout(2,1));//容器
        JTextArea t1=new JTextArea();//显示组件
        JTextArea t2=new JTextArea();//显示组件
        t1.setFont(new Font("微软雅黑",1,20));
        t2.setFont(new Font("微软雅黑",1,20));
        show.add(t1);
        show.add(t2);
        window.add(show);

        while(true){
            d=time / 86400 % 60;
            h=time / 3600 % 60;
            m=time / 60 % 60;
            s=time % 60;
            t1.setText("  距离 "+name+" 到期  ");
            t2.setText("  还有 "+d+" 天 "+h+" 小时 "+m+" 分钟 "+s+" 秒  ");//刷新文本区内容
            time--;
            try{
               Thread.sleep(1000);//刷新间隔时间，单位：毫秒
            }catch(Exception e){}
            if(time==0){
                JOptionPane.showMessageDialog(null, "事件"+name+"时间到\n倒计时已结束","提示", JOptionPane.INFORMATION_MESSAGE);
                window.dispose();
                break;
            }
        }

        
    }
}
