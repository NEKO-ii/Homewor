# def __str__(self)返回对象的描述，子类中常重写此方法来输出特定描述，通过print(object)直接输出对象时默认会调用该对象中重写的__str__()方法
# def __add__(self,other)在类中定义该类对象的相加操作，在对该类对象执行相加操作是会调用该方法

import re


class Student:
    name: str
    age: int
    clas: str

    def __init__(self, name, age, clas) -> None:
        self.name = name
        self.age = age
        self.clas = clas

    def __str__(self) -> str:
        return ("name:{0}  age:{1}  clas:{2}".format(self.name, self.age, self.clas))

    def __add__(self, other) -> int:
        return self.age + other.age


stu1 = Student("NEKO", 22, "SE19-5")
stu2 = Student("NICO", 21, "SE19-5")
print("\n----------------------------------显示对象自述")
print(stu1)  # 自动调用类中重写的__str__()方法
print(stu2)
print("\n----------------------------------自定义加法演示")
val = stu1 + stu2
print("stu1 + stu2 :",val)  # 调用类中的__add__()方法，进行的是年龄相加
