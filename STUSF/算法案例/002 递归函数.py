# 计算阶乘
def fun1(n: int):
    if (n == 1): return 1
    else: return n * fun1(n - 1)


print("10 的阶乘为", fun1(10))


# 输出斐波那契数列的前N个数
def fun2(limit=15):
    if (limit == 1): print("1")
    elif (limit == 2): print("1 1")
    else:
        print("1 1", end=" ")
        a = 1
        b = 1
        for _ in range(limit - 2):
            c = a + b
            a = b
            b = c
            print(a + b, end=" ")
    print()


print("输出斐波那契数列到第15位: ",end="")
fun2()


# 输出斐波那契数列的第N个数
def fun3(limit=15):
    if (limit == 1): return 1
    elif (limit == 2): return 2
    else: return fun3(limit - 1) + fun3(limit - 2)


print("斐波那契数列的第10个数为: ", fun3(10))

# 上面的方法其实也可以加一个循环来输出前N个数，但是套娃太多对计算机来说简直就是折磨，试着运行下面的代码输出前50个你就懂了
# for i in range(1,51):
#     print(fun3(i))
# 再用前面的fun2来输出前50个对比一下差距，所以说递归函数的效率就很拉胯
# fun2(50)
