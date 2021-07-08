package h519;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class HomeW_05_19{
    static JTextField t=new JTextField(20);//用于输出信息的文本框;
    public static void main(String[] args) {
        JFrame W=new JFrame("Java作业");//建立窗口
        
        JPanel show=new JPanel(new GridLayout(2,1));//主容器
        JPanel p1=new JPanel();//上部面板
        JPanel p2=new JPanel();//下部面板
        
        t.setHorizontalAlignment(JTextField.CENTER);//居中显示
        
        JButton showName=new JButton("显示姓名");
        JButton showClass=new JButton("显示班级");
        JButton showNum=new JButton("显示学号");
        showName.setActionCommand("showName");//按钮事件编号，处理事件是对不同按钮进行区分
        showClass.setActionCommand("showClass");
        showNum.setActionCommand("showNum");
        
        MyMonitor L=new MyMonitor();
        
        showName.addActionListener(L);
        showClass.addActionListener(L);
        showNum.addActionListener(L);
        
        //容器添加
        p1.add(showName);
        p1.add(showClass);
        p1.add(showNum);
        p2.add(t);
        show.add(p1);
        show.add(p2);
        W.add(show);
        
        W.setBounds(500, 500, 300, 120);
        W.setVisible(true);
        W.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    //更新显示的方法
    public void showMassage(String s){
        t.setText(s);
    }
}

class MyMonitor extends HomeW_05_19 implements ActionListener{
    public void actionPerformed(ActionEvent e){
        if(e.getActionCommand().equals("showName")){
            showMassage("张永佳");
        }
        if(e.getActionCommand().equals("showClass")){
            showMassage("软件19-5班");
        }
        if(e.getActionCommand().equals("showNum")){
            showMassage("1908060525");
        }
    }
}