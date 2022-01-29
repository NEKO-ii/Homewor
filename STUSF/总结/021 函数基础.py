# 函数是执行特定任务以完成特定功能的代码块
# 使用函数的优点: 相同功能的代码复用、程序结构模块化、隐藏实现细节、提高可读性和可维护性、便于调试

# 自定义函数的创建:
# def function_name([parameter1:type],[parameter2:type],...) -> int:  参数后面加冒号和数据类型可以限制传入参数的类型,函数名后面-> Any 表示返回值为int类型，默认不加为Any
#     function_body
#     [return value]

print("----------------------------------自定义函数演示")


def function1(val1, val2):
    return val1 + val2


n1 = n2 = 2
s1 = s2 = "2"
print(n1, " ", n2, "\n", s1, " ", s2)
print("n1 + n2 = ", function1(n1, n2))
print("s1 + s2 = ", function1(s1, s2))
# print("n1 + s1 = ",function1(n1,s1))  # TypeError
# 自定义函数function1()未设置参数类型，其参数可以是任何类型
# 当输入为数字时，进行算术相加，输入为字符串时进行字符串拼接，输入数据无法被运算符(+)运算则报错

# --------函数传参--------
# 在进行参数传递时，有两种方式，假设有函数fun(a,b):
# 不写参数名称，只写值时为位置实参传递，如fun(1,2)
# 写参数名=值时为关键字实参传递，如fun(a=1,b=2)或fun(b=2,a=1)这样的话可以不考虑参数在括号中的位置
print("\n----------------------------------函数传参演示")


def function2(name:str, age:int):
    return "".join(["name = ", str(name), " age = ", str(age)])


print("参数位置传递1: ", function2("NEKO", 22))
print("参数位置传递2: ", function2(22, "NEKO"))
print("参数名称传递1: ", function2(name="NEKO", age=22))
print("参数名称传递2: ", function2(age=22, name="NEKO"))
# 使用关键字实参传递可以忽略参数先后顺序

# --------实参变化--------
# 如果不可变对象(元组,字符串,数字)作为实参传进函数中，在函数内针对该实参的修改不会改变原参数变量的值
# 如果可变对象(列表,字典,集合)作为实参传进函数中，在函数内针对该实参的修改将会改变原参数变量的值
print("\n----------------------------------实参变化演示")
a = 3
b = "hello"
c = [2, 3, 3]
print("a: ", a)
print("b: ", b)
print("c: ", c)
print()


def function3(ai, bo, ci):
    ai += 1
    bi = " ".join([bo, "world"])
    ci.append(3)
    print("ai: ", ai)
    print("bi: ", bi)
    print("ci: ", ci)


function3(a, b, c)

print()
print("a: ", a)
print("b: ", b)
print("c: ", c)
# 可以看到函数内对数字和字符串的修改并没有影响到实参本身，但是列表修改后，实参本身也进行了修改

# --------返回多值--------
# 函数返回多个值时，所有返回值将组成一个元组然后返回该元组
print("\n----------------------------------返回多值演示")
a = 1
b = 2
c = 3
print(F"a = {a}   b = {b}   c = {c}")


def function4(a, b, c):
    return a, b, c


re = function4(a, b, c)
print(re, type(re))
