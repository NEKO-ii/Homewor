package h524;

import java.awt.*;
import javax.swing.*;

public class E2 {
    public static void main(String[] args) {
        Window2 W=new Window2();
        W.setTitle("1920010825");
        W.pack();
        W.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        W.setLocationRelativeTo(null);
        W.setVisible(true);
    }
}

class Window2 extends JFrame{
    Window2(){
        this.setLayout(new BorderLayout(5,5));
        getContentPane().add("North",new JButton(BorderLayout.NORTH));
        getContentPane().add("South",new JButton(BorderLayout.SOUTH));
        getContentPane().add("East",new JButton(BorderLayout.EAST));
        getContentPane().add("West",new JButton(BorderLayout.WEST));
        getContentPane().add("Center",new JButton(BorderLayout.CENTER));
    }
}
