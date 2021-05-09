package mktwo;

import java.awt.*;
import java.awt.event.*;
import java.math.BigDecimal;

import javax.swing.*;

public class Window extends JFrame implements ActionListener,Averagable{
    JTextField t1,t2,t3,t4,t5,t6,t7,t8,t9,t10;//输入文本框
    JTextField o1,o2;//输出文本框
    JButton calculate;//计算按钮
    Double m1,m2,m3,m4,m5,m6,m7,m8,m9,m10;//存储输入数据用于计算
    Double a1,a2;//存储计算结果
    Double n=0.0;//存储输入数据个数

    Window(){
        init();
        setVisible(true);//是否可见
        setBounds(500, 500, 600, 260);//窗口位置和大小
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    void init(){
        JPanel p=new JPanel();
        JPanel p1=new JPanel();//顶行提示
        p1.add(new JLabel("请输入数据\n第一个不能为空"));

        JPanel p2=new JPanel(new GridLayout(2,5));//输入区
        t1=new JTextField(6);
        t2=new JTextField(6);
        t3=new JTextField(6);
        t4=new JTextField(6);
        t5=new JTextField(6);
        t6=new JTextField(6);
        t7=new JTextField(6);
        t8=new JTextField(6);
        t9=new JTextField(6);
        t10=new JTextField(6);
        p2.add(t1);
        p2.add(t2);
        p2.add(t3);
        p2.add(t4);
        p2.add(t5);
        p2.add(t6);
        p2.add(t7);
        p2.add(t8);
        p2.add(t9);
        p2.add(t10);

        JPanel p3=new JPanel();//输出区
        o1=new JTextField(6);
        o2=new JTextField(6);
        calculate=new JButton("计算");
        p3.add(calculate);
        p3.add(new JLabel("averageAll"));
        p3.add(o1);
        p3.add(new JLabel("AverageExceptMaxMin"));
        p3.add(o2);
        calculate.addActionListener(this);

        p.add(p1);
        p.add(p2);
        p.add(p3);
        add(p);
    }

    public Double averageAll() {
        Double s=0.0;
        try{
            if(isNum(t1.getText())) {s=s+m1;}
            if(isNum(t2.getText())) {s=s+m2;}
            if(isNum(t3.getText())) {s=s+m3;}
            if(isNum(t4.getText())) {s=s+m4;}
            if(isNum(t5.getText())) {s=s+m5;}
            if(isNum(t6.getText())) {s=s+m6;}
            if(isNum(t7.getText())) {s=s+m7;}
            if(isNum(t8.getText())) {s=s+m8;}
            if(isNum(t9.getText())) {s=s+m9;}
            if(isNum(t10.getText())) {s=s+m10;}
        }catch(Exception e){}
        return s/n;
    }

    public Double AverageExceptMaxMin() {
        Double s=0.0;
        Double max=0.0;
        Double min=0.0;
        try{
            if(isNum(t1.getText())) {
                s=s+m1;
                max=m1;
                min=m1;
            }
            else{JOptionPane.showMessageDialog(null, "第一个不能为空，此计算结果有误","警告", JOptionPane.WARNING_MESSAGE);}
            if(isNum(t2.getText())) {
                s=s+m2;
                if(m2>max) max=m2;
                if(m2<min) min=m2;
            }
            if(isNum(t3.getText())) {
                s=s+m3;
                if(m3>max) max=m3;
                if(m3<min) min=m3;
            }
            if(isNum(t4.getText())) {
                s=s+m4;
                if(m4>max) max=m4;
                if(m4<min) min=m4;
            }
            if(isNum(t5.getText())) {
                s=s+m5;
                if(m5>max) max=m5;
                if(m5<min) min=m5;
            }
            if(isNum(t6.getText())) {
                s=s+m6;
                if(m6>max) max=m6;
                if(m6<min) min=m6;
            }
            if(isNum(t7.getText())) {
                s=s+m7;
                if(m7>max) max=m7;
                if(m7<min) min=m7;
            }
            if(isNum(t8.getText())) {
                s=s+m8;
                if(m8>max) max=m8;
                if(m8<min) min=m8;
            }
            if(isNum(t9.getText())) {
                s=s+m9;
                if(m9>max) max=m9;
                if(m9<min) min=m9;
            }
            if(isNum(t10.getText())) {
                s=s+m10;
                if(m10>max) max=m10;
                if(m10<min) min=m10;
            }
        }catch(Exception e){}
        return (s-max-min)/(n-2.0);
    }

    public void actionPerformed(ActionEvent e) {
        try{
            n=0.0;
            if(!"".equals(t1.getText())) {
                if(isNum(t1.getText())) {n++;t1.setForeground(Color.BLACK);m1= Double.parseDouble(t1.getText().trim());}
                else {t1.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t2.getText())) {
                if(isNum(t2.getText())) {n++;t2.setForeground(Color.BLACK);m2= Double.parseDouble(t2.getText().trim());}
                else {t2.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t3.getText())) {
                if(isNum(t3.getText())) {n++;t3.setForeground(Color.BLACK);m3= Double.parseDouble(t3.getText().trim());}
                else {t3.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t4.getText())) {
                if(isNum(t4.getText())) {n++;t4.setForeground(Color.BLACK);m4= Double.parseDouble(t4.getText().trim());}
                else {t4.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t5.getText())) {
                if(isNum(t5.getText())) {n++;t5.setForeground(Color.BLACK);m5= Double.parseDouble(t5.getText().trim());}
                else {t5.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t6.getText())) {
                if(isNum(t6.getText())) {n++;t6.setForeground(Color.BLACK);m6= Double.parseDouble(t6.getText().trim());}
                else {t6.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t7.getText())) {
                if(isNum(t7.getText())) {n++;t7.setForeground(Color.BLACK);m7= Double.parseDouble(t7.getText().trim());}
                else {t7.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t8.getText())) {
                if(isNum(t8.getText())) {n++;t8.setForeground(Color.BLACK);m8= Double.parseDouble(t8.getText().trim());}
                else {t8.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t9.getText())) {
                if(isNum(t9.getText())) {n++;t9.setForeground(Color.BLACK);m9= Double.parseDouble(t9.getText().trim());}
                else {t9.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
            if(!"".equals(t10.getText())) {
                if(isNum(t10.getText())) {n++;t10.setForeground(Color.BLACK);m10= Double.parseDouble(t10.getText().trim());}
                else {t10.setForeground(Color.RED);JOptionPane.showMessageDialog(null, "请输入数字，错误输入已标红","警告", JOptionPane.WARNING_MESSAGE);}
            }
        }catch(Exception ex){
            JOptionPane.showMessageDialog(null, ex,"警告", JOptionPane.WARNING_MESSAGE);//弹出输入错误警告
        }
        
        a1=averageAll();
        a2=AverageExceptMaxMin();
        o1.setText(String.valueOf(a1));
        o2.setText(String.valueOf(a2));
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
