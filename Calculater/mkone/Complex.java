package mkone;
import javax.swing.JOptionPane;

public class Complex {
    private double real,imag;//realΪ����ʵ����imagΪ�����鲿
    boolean legal=true;//Ĭ�ϸø����Ϸ�
    Complex(double r,double i){
        this.real=r;
        this.imag=i;
    }
    Complex(String r,String i){//���ַ�����������
        try{
            this.real=Double.parseDouble(r);
            this.imag=Double.parseDouble(i);
        }catch(Exception exception){
            JOptionPane.showMessageDialog(null, exception+"\n�����봿����", "����", JOptionPane.WARNING_MESSAGE);//��������
            legal=false;//���������ݳ�����ø������Ϸ�
        }
    }
    public Complex add(Complex a,Complex b){//�����ӷ���
        return new Complex(a.real+b.real,a.imag+b.imag);
    }
    public Complex sub(Complex a,Complex b){//����������
        return new Complex(a.real-b.real, a.imag-b.imag);
    }
    public double getReal(){
        return real;
    }
    public double getImag(){
        return imag;
    }
}
