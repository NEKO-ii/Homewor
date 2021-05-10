package countdown;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.math.BigDecimal;

public class RunCountDown{
    public static void main(String[] args) {
        Run mainRun=new Run();
        mainRun.setTitle("����ʱ����");
    }
}

class Run extends JFrame implements ActionListener{
    JTextField t1,t2,t3,t4,t;
    int day,hour,min,sec;//��������ʱ��
    int time=0;//������ʱ��(��λ����)
    String name;//�����¼�����
    
    Run(){
        init();
        setBounds(500, 500, 450, 140);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    void init() {
        JPanel show=new JPanel(new GridLayout(2,1));//������
        JPanel p1=new JPanel();//�ϲ����
        JPanel p2=new JPanel();//�²����

        JLabel l1,l2,l3,l4,l5,l6;
        JButton addNewRun;

        t=new JTextField(10);
        t1=new JTextField(5);
        t2=new JTextField(5);
        t3=new JTextField(5);
        t4=new JTextField(5);
        
        l1=new JLabel(" �� ");
        l2=new JLabel(" ʱ ");
        l3=new JLabel(" �� ");
        l4=new JLabel(" �� ");
        l5=new JLabel(" ���õ���ʱ ");
        l6=new JLabel(" �¼��� ");

        addNewRun=new JButton("��ӽ���");
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
        boolean n=true;//�Ƿ���ϴ������̵�����
        try{
            if(!"".equals(t.getText())) {//�¼����Ʋ���Ϊ��
                name=t.getText();
            }
            else{
                n=false;
                JOptionPane.showMessageDialog(null, "�¼�������Ϊ��","����", JOptionPane.WARNING_MESSAGE);
            }
            if(!"".equals(t1.getText())) {
                if(isNum(t1.getText())) {t1.setForeground(Color.BLACK);day= Integer.parseInt(t1.getText().trim());}
                else {day=0;n=false;t1.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "���������֣����������ѱ��","����", JOptionPane.WARNING_MESSAGE);}
            }
            else day=0;
            if(!"".equals(t2.getText())) {
                if(isNum(t2.getText())) {t2.setForeground(Color.BLACK);hour= Integer.parseInt(t2.getText().trim());}
                else {hour=0;n=false;t2.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "���������֣����������ѱ��","����", JOptionPane.WARNING_MESSAGE);}
            }
            else hour=0;
            if(!"".equals(t3.getText())) {
                if(isNum(t3.getText())) {t3.setForeground(Color.BLACK);min= Integer.parseInt(t3.getText().trim());}
                else {min=0;n=false;t3.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "���������֣����������ѱ��","����", JOptionPane.WARNING_MESSAGE);}
            }
            else min=0;
            if(!"".equals(t4.getText())) {
                if(isNum(t4.getText())) {t4.setForeground(Color.BLACK);sec= Integer.parseInt(t4.getText().trim());}
                else {sec=0;n=false;t4.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "���������֣����������ѱ��","����", JOptionPane.WARNING_MESSAGE);}
            }
            else sec=0;
        }catch(Exception ex){}
        
        if(n==true){
            time=sec+60*min+3600*hour+86400*day;
            Window win=new Window();
            win.setName(name);
            win.setTime(time);
            Thread thr=new Thread(win);//��������
            thr.start();
        }
    }
    public static boolean isNum(String str) {//�ж������Ƿ�Ϊ����
        try {
            String bigStr = new BigDecimal(str).toString();
        } catch (Exception e) {
            return false;//�쳣 ˵�����������֡�
        }
        return true;
    }
}

class Window implements Runnable{
    String name;
    int time;
    int d,h,m,s;//��ʾʱ��
    public void setName(String name){
        this.name=name;
    }
    public void setTime(int time){
        this.time=time;
    }
    public void run(){
        JFrame window=new JFrame();//���ڶ���
        window.setTitle("���񵹼�ʱ");
        window.setBounds(500, 500, 350, 100);
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);//�رո�����ʱ���ͷŸ�������Դ�����ر�������
        
        JPanel show=new JPanel(new GridLayout(2,1));//����
        JTextArea t1=new JTextArea();//��ʾ���
        JTextArea t2=new JTextArea();//��ʾ���
        t1.setFont(new Font("΢���ź�",1,20));
        t2.setFont(new Font("΢���ź�",1,20));
        show.add(t1);
        show.add(t2);
        window.add(show);

        while(true){
            d=time / 86400 % 60;
            h=time / 3600 % 60;
            m=time / 60 % 60;
            s=time % 60;
            t1.setText("  ���� "+name+" ����  ");
            t2.setText("  ���� "+d+" �� "+h+" Сʱ "+m+" ���� "+s+" ��  ");//ˢ���ı�������
            time--;
            try{
               Thread.sleep(1000);//ˢ�¼��ʱ�䣬��λ������
            }catch(Exception e){}
            if(time==0){
                JOptionPane.showMessageDialog(null, "�¼�"+name+"ʱ�䵽\n����ʱ�ѽ���","��ʾ", JOptionPane.INFORMATION_MESSAGE);
                window.dispose();
                break;
            }
        }

        
    }
}
