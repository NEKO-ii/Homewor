# 这是一个模块
# if __name__ == "__main__":语句可以判断当前是否以主程序运行该.py文件，如果是则执行其下代码，如果是作为模块被导入则不执行


class Student:
    name: str
    age: int
    clas: str

    def __init__(self, name, age, clas) -> None:
        self.name = name
        self.age = age
        self.clas = clas

    def show(self):
        print("My name is " + self.name + ", " + str(self.age) + " years old, I'm in " + self.clas)

    def __str__(self) -> str:
        return "This is a class in a module, named 'Student'"


def fun():
    print("This is a function in a module")


if __name__ == "__main__":
    # 下面语句只有当运行该文件时才会执行，作为模块导入其他程序则会被忽略
    stu = Student("NEKO", 22, "SE19-5")
    print(stu)
    fun()
