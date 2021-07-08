package h524;

import javax.swing.JFrame;

public class E1 {
    public static void main(String[] args) {
        Window.createGUI();
    }
}
class Window extends JFrame{
    public static void createGUI(){
        JFrame F=new JFrame();
        F.setTitle("1920010825");
        F.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        F.setBounds(300, 100, 400, 300);
        F.setVisible(true);
    }
}