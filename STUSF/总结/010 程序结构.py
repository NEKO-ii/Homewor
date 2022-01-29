# 顺序结构 基本结构
print("顺序结构演示:")
print("-----start-----")
print("  progress1...")
print("  progress1...")
print("  progress1...")
print("  progress1...")
print("------end------")

# 分支结构 if ; switch
# Python中每个对象都有一个布尔值，数值0、none、空字符串、空集合、空列表、空元组等空元素的布尔值为false，可以用函数 bool(obj)获取
# if-else分支结构的简写: [表达式1] if (条件表达式) else [表达式2]
print("\n分支结构演示:")
print("-----start-----")
val = input("请输入1或2选择程序段 > ")
if (val == "1"):
    print("  progress1...")
elif (val == "2"):
    print("  progress2...")
else:
    print("  wrong input ")
print("------end------")

# 循环结构 for in ; while
print("\n循环结构演示:")
print("-----start-----")
n = 10
i = 1
k = 1
print("the while loop:")
while (i <= n):
    print("    loop " + str(i))
    i += 1
print("\nthe for loop:")
for k in range(1, 11):  # 因为range序列不包括参数11，所以只循环10次
    print("    loop " + str(k))
print("------end------")

# pass占位,pass在程序执行时并不会产生实际作用，它的用处是搭建代码结构，如if的某一个分支暂时不写其语句，可用pass进行占位来保证程序顺利执行
# 下面的程序不会有任何行为
if (1 < 2):
    pass
else:
    pass

# for in 循环还可以遍历字符串，如下面输出NEKO中的所有字母
print("\nfor-in 循环遍历字符串:")
for str in "NEKO":
    print(str, end=" ")  # 此处end=" "表示每次输出以空格结尾，不会换行

# 若for-in循环中，for后面的变量不会使用到，则可以用下划线替代
for _ in range(10):
    pass

# break可以用于终止循环
for i in range(10):
    if (i == 0): break

# 用于跳过当前循环，进入下一次循环,下面程序当i==2时跳过此次循环，所以不输出2
print("\n\ncontinue演示:")
for i in (1, 2, 3):
    if (i == 2): continue
    print(i)

# else不仅可以和if一起使用，还可以和for、while循环一起使用
# 当循环正常执行完毕后将执行else语句，如果循环提前结束(如break或出错)将不执行else语句
print("\n循环else连用演示:")
for i in (1, 2, 3):
    print(i,end=" ")
else: print("循环正常执行完毕\n")
i=1
while(i<=3):
    print(i,end=" ")
    if(i==2): break
    i+=1
else: print("循环正常执行完毕")
