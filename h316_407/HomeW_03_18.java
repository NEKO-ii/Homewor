package h316_407;


public class HomeW_03_18 {
    public static void main(String[] args) {
        int money=20;  //总金钱
        Goods book=new Goods(12,1);
        Goods pen=new Goods(1,0);
        Goods era=new Goods(2,0);
        Goods col=new Goods(3,0);
        Goods foo=new Goods(5,0);
        int leave=money-book.pri*book.num;  //除去比买的书本剩余的钱
        int p=1;  //记录购物清单的编号
        
        System.out.println("除购买"+book.num+"本书之外还可能的购物清单如下：");

        //遍历所有可能情况并输出
        for(pen.num=0;pen.num<=leave/pen.pri;pen.num++){
            int leave_1=leave-pen.pri*pen.num;
            for(era.num=0;era.num<=leave_1/era.pri;era.num++){
                int leave_2=leave_1-era.pri*era.num;
                for(col.num=0;col.num<=leave_2/col.pri;col.num++){
                    int leave_3=leave_2-col.pri*col.num;
                    for(foo.num=0;foo.num<=leave_3/foo.pri;foo.num++){
                        int leave_4=leave_3-foo.pri*foo.num;
                        System.out.println("情况"+p+"：\n"
                        +"铅笔："+pen.num+"支\n"
                        +"橡皮："+era.num+"块\n"
                        +"可乐："+col.num+"瓶\n"
                        +"零食："+foo.num+"袋\n"
                        +"余额"+leave_4+"元\n\n");
                        p++;
                    }
                }
            }
        }
    }
    
}

//声明商品类
class Goods{
    int num,pri;
    Goods(int a,int b){
        pri=a;
        num=b;
    }
}