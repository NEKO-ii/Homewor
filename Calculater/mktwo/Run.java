package mktwo;

interface Averagable{//求平均接口
    public Double averageAll();
    public Double AverageExceptMaxMin();
}

public class Run {
    public static void main(String[] args) {
        Window mainwindow=new Window();
        mainwindow.setTitle("平均值计算器");
    }
}