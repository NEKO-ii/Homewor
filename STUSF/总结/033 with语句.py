# with语句自动管理资源，若使用with语句打开文件，如论程序运行中途有没有出错，只要跳出with块，系统会自动调用__exit__()方法释放资源
# with语句结构为: with [上下文表达式] as [变量名]
# 例如使用with语句打开文件，可以省略close语句:
with open("./总结/file/033.txt", "r", encoding="UTF-8") as file:
    print(file.read())


# with后面返回的对象要求必须有__enter__()/__exit__()这两个方法(也就是遵循上下文管理协议)，而文件对象刚好是有这两个方法的
# 下面自己定义一个类来实现这两个方法来演示:
class Test(object):

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def show(self):
        print("Test class")


with Test() as t:
    t.show()
