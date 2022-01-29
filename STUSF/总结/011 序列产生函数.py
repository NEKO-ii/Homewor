# range(start,end,step) 函数用于创建一个从start(默认为0)到end的步长为setp(默认为1)的整数序列，注：包括start，不包括end，即[start,end)
# 不管range对象的序列有多长，所有range占用的内存空间都是相同的，系统只需要存储它的三个参数，只有在使用时才计算序列
# range对象存储时只存储参数，所以直接输出range对象无法看到它的完整序列，但可以使用list()函数来查看
r1 = range(10)
r2 = range(1, 10)
r3 = range(1, 10, 2)
print("直接输出range对象")
print(r1)  # 直接输出range对象
print(r2)
print(r3)
print("\n使用list()输出range对象")
print(list(r1))
print(list(r2))
print(list(r3))

# 若要对range()函数产生的序列进行一定处理再存到列表中则可使用如下语法
list=[i*i for i in range(1,11)]  #该语法意为: 产生1-10的序列，用变量i遍历该序列，将序列每个值进行平方运算后保存到列表list中
print("\n序列处理后产生的列表 ",list)
