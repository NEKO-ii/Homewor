package h519;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class HomeW_05_19{
    static JTextField t=new JTextField(20);//���������Ϣ���ı���;
    public static void main(String[] args) {
        JFrame W=new JFrame("Java��ҵ");//��������
        
        JPanel show=new JPanel(new GridLayout(2,1));//������
        JPanel p1=new JPanel();//�ϲ����
        JPanel p2=new JPanel();//�²����
        
        t.setHorizontalAlignment(JTextField.CENTER);//������ʾ
        
        JButton showName=new JButton("��ʾ����");
        JButton showClass=new JButton("��ʾ�༶");
        JButton showNum=new JButton("��ʾѧ��");
        showName.setActionCommand("showName");//��ť�¼���ţ������¼��ǶԲ�ͬ��ť��������
        showClass.setActionCommand("showClass");
        showNum.setActionCommand("showNum");
        
        MyMonitor L=new MyMonitor();
        
        showName.addActionListener(L);
        showClass.addActionListener(L);
        showNum.addActionListener(L);
        
        //�������
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
    //������ʾ�ķ���
    public void showMassage(String s){
        t.setText(s);
    }
}

class MyMonitor extends HomeW_05_19 implements ActionListener{
    public void actionPerformed(ActionEvent e){
        if(e.getActionCommand().equals("showName")){
            showMassage("������");
        }
        if(e.getActionCommand().equals("showClass")){
            showMassage("���19-5��");
        }
        if(e.getActionCommand().equals("showNum")){
            showMassage("1908060525");
        }
    }
}