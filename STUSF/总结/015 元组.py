# 元组(tuples)为python内置数据结构之一，和字符串一样为不可变序列(已经定义的元组不能在id不变的情况下修改其中的值)
# 其结构为 [name] = (val1, val2, val3) 例如 tup = (2,3,"3")

# 元组创建方式
# 直接使用结构式 [name] = (val1, val2, val3)
# 使用内置函数 tuple((val1, val2, val3))
# 只包含一个元素的元组定义时需要在元素后加逗号 如 tup = (1,)
print("--------------------------------------元组的创建")
tup1 = (2, 3, 3)
tup2 = tuple(("2", "3", "3"))
tup3 = (1, )
tup4 = ()
print("tup1: ", tup1)
print("tup2: ", tup2)
print("tup3: ", tup3)
print("tup4: ", tup4)

print("--------------------------------------元组的遍历")
print("tup1: ", end="")
for item in tup1:
    print(item, end=" ")
print("\ntup2: ", end="")
for item in tup2:
    print(item, end=" ")
