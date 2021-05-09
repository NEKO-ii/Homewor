package mkone;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Window extends JFrame implements ActionListener{
    Complex c1,c2,c3,answer;//c1��c2��c3Ϊ�û����븴����answerΪ������
    Complex m1,m2;//���ڴ洢��ʱ������
    JTextField text11,text12,text21,text22,text31,text32;//���ݶ�����ͼ���û�����
    JTextArea show;//���ݶ�����ͼ����ʾ���
    JButton calculate;//���������󣬼��㰴ť

    Window(){
        init();
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    void init(){
        text11=new JTextField(5);
        text12=new JTextField(5);
        text21=new JTextField(5);
        text22=new JTextField(5);
        text31=new JTextField(5);
        text32=new JTextField(5);
        show=new JTextArea();
        calculate=new JButton("����");
        JPanel inputArea=new JPanel(new GridLayout(3,4));
        inputArea.add(text11);
        inputArea.add(text12);
        inputArea.add(new JLabel("i"));
        inputArea.add(new JLabel("+"));
        inputArea.add(text21);
        inputArea.add(text22);
        inputArea.add(new JLabel("i"));
        inputArea.add(new JLabel("-"));
        inputArea.add(text31);
        inputArea.add(text32);
        inputArea.add(new JLabel("i"));
        inputArea.add(calculate);
        calculate.addActionListener(this);
        add(inputArea,BorderLayout.NORTH);
        add(new JScrollPane(show),BorderLayout.CENTER);
    }
    
    public void actionPerformed(ActionEvent e) {
        try{
            c1=new Complex(text11.getText().trim(),text12.getText().trim());
            c2=new Complex(text21.getText().trim(),text22.getText().trim());
            c3=new Complex(text31.getText().trim(),text32.getText().trim());
            if(c2.legal==true){
                m1=c2.add(c1, c2);
            }
            if(c3.legal==true){
                if(c2.legal==true){
                    m2=c3.sub(m1, c3);
                    answer=m2;
                }
                else{
                    m2=c3.sub(c1, c3);
                    answer=m2;
                }
            }
            else{
                answer=m1;
            }
            show.append("\n������Ϊ��"+answer.getReal()+"  +  "+answer.getImag()+"  i");
        }catch(Exception ex){
            show.append("\n"+ex+"\n");
        }
    }
}