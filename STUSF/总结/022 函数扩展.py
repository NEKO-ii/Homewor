# --------参数定义--------
# 在给函数定义参数时，可以给形参设置默认值，只有传递的实参与形参默认值不一致时才会用实参值替换默认值
# 定义了形参默认值的函数，在传入实参时可以不传入形参已有默认值的部分
print("-----------------------------------------参数定义演示")
a = 1
b = 2
print(F"a = {a}   b = {b}")


def fun1(a, b=3):
    return (F"a ={a}   b = {b}")


print("只传入实参a: ", fun1(a))
print("传入实参a、b: ", fun1(a, b))

# --------变长形参--------
# 当不确定传入参数的数量时，可以使用定义变长形参，其参数数量会根据传入的实参数量来确定
# 变长形参也包括可变长位置形参和可变长关键字形参，定义方法分别为 fun(*val) 和 fun(**val)，传入的参数分别存储为 元组 和 字典
# 可以同时定义两种，如 fun(*val1,**val2) 注意：这里位置参数 *val1 必须写在前面，函数调用时也是
print("\n-----------------------------------------变长形参演示")


def fun2(*val):
    print(str(val).ljust(30, " "), end="  ")
    print(type(val))


def fun3(**val):
    print(str(val).ljust(30, " "), end="  ")
    print(type(val))


def fun4(*val1, **val2):
    print(str(val1).ljust(30, " "), end="  ")
    print(type(val1))
    print(str(val2).ljust(30, " "), end="  ")
    print(type(val2))


fun2(2, 3, 3)
fun2(2, 3, 3, 3, 3, 3, 3)
fun3(name="NEKO")
fun3(name="NEKO", age=22)
fun4(2, 3, 3, name="NEKO", age=22)
# fun4(name="neko",2,3,3)  # positional argument must begore keyword argument

# --------实参引用--------
# 在向函数传入实参时也可以用 * 和 ** 来将元组和字典的每一项拿出来分别做实参进行传入
print("\n-----------------------------------------实参引用演示")
tup = (2, 3, 3)
dict = {"name": "NEKO", "age": 22}


def fun5(a, b, c):
    print("a = ", a, "  b = ", b, "  c = ", c)


def fun6(name, age):
    print("My name is", name, ", I'm ", age, " years old.")


# fun5(tup)  # TypeError fun5() missing 2 required positional arguments: 'b' and 'c'

fun5(*tup)
fun6(**dict)

# --------递归函数--------
# 如果函数内调用了函数自身，那么该函数为递归函数，使用递归函数能使代码更简洁，但会占用更高的内存，且效率较低
# 递归函数每次调用其自身，都会在内存中占用一个新的栈，并且执行完一次函数，栈空间会释放
# 递归函数内一般都有分支结构，分支其一调用自身，分支其二不调用自身，用于结束递归
print("\n-----------------------------------------递归函数演示")
# 下面以两个计算阶乘的函数来体现递归函数特点


# 一般的实现阶乘的函数:
def fun7(n):
    print(n, "的阶乘为 ", end="")
    s = 1
    while (n > 0):
        s *= n
        n -= 1
    print(s)


def fun8(n):
    if (n == 1): return 1
    else: return n * fun8(n - 1)


fun7(10)
print("10 的阶乘为",fun8(10))

# ----------其他----------
# 若函数这样定义: fun(a,b,*,c,d) 那么传入参数时星号前面的参数采用位置传参，星号后面的参数只能采用关键字传参
