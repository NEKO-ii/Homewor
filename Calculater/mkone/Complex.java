package mkone;
import javax.swing.JOptionPane;

public class Complex {
    private double real,imag;//real为复数实部，imag为复数虚部
    boolean legal=true;//默认该复数合法
    Complex(double r,double i){
        this.real=r;
        this.imag=i;
    }
    Complex(String r,String i){//由字符串构建复数
        try{
            this.real=Double.parseDouble(r);
            this.imag=Double.parseDouble(i);
        }catch(Exception exception){
            JOptionPane.showMessageDialog(null, exception+"\n请输入纯数字", "警告", JOptionPane.WARNING_MESSAGE);//弹出警告
            legal=false;//若输入数据出错，则该复数不合法
        }
    }
    public Complex add(Complex a,Complex b){//复数加方法
        return new Complex(a.real+b.real,a.imag+b.imag);
    }
    public Complex sub(Complex a,Complex b){//复数减方法
        return new Complex(a.real-b.real, a.imag-b.imag);
    }
    public double getReal(){
        return real;
    }
    public double getImag(){
        return imag;
    }
}
