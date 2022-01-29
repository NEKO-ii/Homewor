# Python中的类可以继承多个父类(默认继承object类),子类的构造方法中需要调用父类的构造方法
# 语法格式:
# class [name] ([parent class1],[parent class2]):
#    def __init__(self,val1,val2,val3):
#        super().__init__(val1,val2)
#        self.val3 = val3

# 在子类中进行方法重写时，若使用到父类原方法，可通过super()函数调用，若不使用父类方法，可直接编写


class Person:
    name: str
    age: int

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        print("name: " + self.name + "\nage: " + str(self.age))


class Student(Person):
    clas: str

    def __init__(self, name, age, clas) -> None:
        super().__init__(name, age)
        self.clas = clas

    def show(self):
        super().show()
        print("clas: " + self.clas)


class Teacher(Person):
    ID: str

    def __init__(self, name, age, id) -> None:
        super().__init__(name, age)
        self.id = id

    def show(self):
        super().show()
        print("id: " + self.id)


stu = Student("NEKO", 22, "SE19-5")
tea = Teacher("NEKO", 22, "2022001")
print("---------------------------------stu.show")
stu.show()
print("\n---------------------------------tea.show")
tea.show()
