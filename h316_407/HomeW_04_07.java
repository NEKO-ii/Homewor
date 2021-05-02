package h316_407;

interface USB{  //USB接口
    void Link();
    void Run();
    void Close();
}

interface Power{  //电源接口
    void Recharge();
}

class Computer{
    String id;
    String key;
    void show(){
        System.out.println("  ID: "+id+"  Key: "+key);
    }

    void useUSB(USB usb){
        if(usb!=null){
            usb.Link();
        }
    }
    void usePower(Power pow){
        pow.Recharge();
    }

}

class Laptop extends Computer implements Power{
    String name;

    Laptop(String name){
        this.name=name;
    }
    Laptop(String name,String id,String key){
        this.name=name;
        this.id=id;
        this.key=key;
    }
    void show(){
        System.out.println("  Name of this laptop: "+name);
        super.show();
    }

    public void Recharge() {
        System.out.println("Power recharging...");
    }

    //USB使用
    void Open(USB usb){
        usb.Run();
    }
    void Close(USB usb){
        usb.Close();
    }
}

class Camera implements USB{
    String name="Camera";
    private int state=0;
    public void Link(){
        state=1;
        System.out.println("USB is link now ");
    }
    public void Run(){
        if(state==1){
            System.out.println("Camera is running...");
        }
        else{
            System.out.println("USB not link ");
        }
    }
    public void Close(){
        state=0;
        System.out.println(name+" off line ");
    }
    
}

//Main
public class HomeW_04_07 {
    public static void main(String[] args) {
        Laptop L=new Laptop("元首家后院","192.168.0.0","10****0");
        L.show();
        L.usePower(L);

        Camera C=new Camera();
        L.useUSB(C);

        L.Open(C);
        L.Close(C);
    }
}