# object.__dir__()          或dir(object)查看指定对象的所有属性和方法
# object.__dict__           返回对象绑定的所有属性的数据字典
# object.__class__          返回对象所属的类
# class.__bases__           返回该类所属父类类型的元组
# class.__mro__             返回该类的继承结构
# class.__subclasses__()    返回该类的所有子类


class Student:
    name: str
    age: int
    clas: str

    def __init__(self, name, age, clas) -> None:
        self.name = name
        self.age = age
        self.clas = clas


class C(Student):
    pass


class D(Student):
    pass


stu = Student("NEKO", 22, "SE19-5")
print("----------------------------------显示所有属性方法")
print(dir(stu))
print("\n----------------------------------对象属性数据字典")
print(stu.__dict__)
print("\n----------------------------------对象所属的类")
print(stu.__class__)
print("\n----------------------------------父类类型元组")
print(Student.__bases__)  # 由于没有继承，所以默认继承object类
print("\n----------------------------------类的继承结构")
print(Student.__mro__)  # 由于没有继承，所以默认继承object类
print("\n----------------------------------类的所有子类")
print(Student.__subclasses__())
