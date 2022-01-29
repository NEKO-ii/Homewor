import time

# Python作为一种面向对象的编程语言，也有自己的类和对象
# 类由属性和方法组成，方法又分为：实例方法、静态方法、类方法
# 自定义类的语法为:
# class [name]:
#    pass


# Student类
class Student:
    # 类中的变量定义变量即为类属性
    # 在python中并未存在私有化属性关键字,当使用双下划线__时，则表明其为实例的私有属性或者私有方法，当私有属性被访问时，只能通过共有类方法进行访问
    # Python中类的属性可以动态绑定，即在类实例化出一个对象后，可继续给此对象添加新的属性
    professional = "学生"
    __name: str
    __sex: str
    __clas: str
    __createTime: time

    # 构造方法(初始化方法)，用于生成实例时的属性初始化(自定义)
    def __init__(self, name, sex, clas) -> None:
        self.__name = name
        self.__sex = sex
        self.__clas = clas
        self.__createTime = self.getTime()

    # 像这样定义在类中的方法是实例方法,其参数必须为实例对象，约定为self，通过self传递类和实例的属性和方法
    # 只能由实例对象调用
    # 类构造方法，也属于实例方法
    def show(self):
        print("我是", self.__name, ",性别", self.__sex, ",是一个", self.professional, ",在", self.__clas)

    def getCTime(self):
        return self.__createTime

    # 使用装饰器 @classmethod 的方法为类方法，参数必须是当前类对象，约定为cls，通过cls来传递类的属性和方法(不能传实例的属性和方法)
    # 类和实例对象都可以调用
    # 原则上，类方法是将类本身作为对象进行操作的方法，另外，如果需要继承，也可以定义为类方法
    @classmethod
    def class_inf(cls):
        print(cls.professional, "类，用于承载", cls.professional, "对象")

    # 使用装饰器 @staticmethod 的方法为静态方法
    # 静态方法是类中的函数，不需要实例，不会涉及到类中的属性和方法的操作，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
    # 类和实例对象都可以调用
    @staticmethod
    def getTime():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 下面是程序演示部分
stu1 = Student("NEKO", "Female", "Software Engineering, Class 5, Grade 19")
stu1.show()
stu1.class_inf()
print(stu1.getCTime())

# 动态绑定新属性
stu1.address = "Earth"
print(stu1.address)


# 动态绑定新方法
def fun():
    print("new fun")


stu1.function = fun
stu1.function()
