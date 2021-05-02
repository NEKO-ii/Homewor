package h316_407;
import java.util.Scanner;//导入Scanner包

public class HomeW_03_16 {
public static void main(String[] args) {
    //输入部分 
    double score;
     Scanner reader=new Scanner(System.in);
    System.out.print("请输入分数：");
    score=reader.nextDouble();

    //判断及输出部分
    if(score<60){  System.out.println("分数为："+score+"  等级为 ——  不合格"); }
    if(60<=score&score<70){ System.out.println("分数为："+score+"  等级为 ——  及格"); }
    if(70<=score&score<80){ System.out.println("分数为："+score+"  等级为 ——  良好"); }
    if(80<=score&score<90){ System.out.println("分数为："+score+"  等级为 ——  优秀"); }
    if(score>=90){ System.out.println("分数为："+score+"  等级为 ——  4极佳"); }

    reader.close();//释放内存
}//main
    
}//class