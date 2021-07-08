package h524;

import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

public class E3 {
    public static void main(String[] args) {
        JFrame F=new JFrame("1920010825");
        F.setLayout(new FlowLayout(FlowLayout.CENTER,3,3));
        JButton B;
        for(int i=1;i<=10;i++){
            B=new JButton("Button 1920010825"+i);
            F.add(B);
        }
        F.setBounds(300,100,800,600);
        F.setVisible(true);
    }
}
