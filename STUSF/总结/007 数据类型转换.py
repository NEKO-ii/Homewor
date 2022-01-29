# 数据类型的转换

name = "NEKO"
age = 22
print(name, type(name))
print(age, type(age))
# print()函数在进行连接时，不能将字符串类型(string)与数字类型(int,float,...)进行连接，下面这句是错的
# print("我是" + name + ",今年" + age + "岁")
# 解决方案为将数字类型转换为字符串类型，函数为 str()
print("我是" + name + ",今年" + str(age) + "岁")

# 类似的转换函数还有
# int() 将数据转换为int整数类型，注意原类型若为字符串，则该字符串必须为数字且为整数时才能进行转换，若为小数则报错
# float() 将数据转换为float浮点数类型，注意原类型若为字符串，则该字符串必须为数字才能进行转换
# str() 将数据转换为str字符串类型
# bool() 将数字0或字符串"0"转换为布尔False,大于0的数字或字符串全部转换为布尔True

n1 = 233
n2 = 2.33
n3 = "233"
n4 = "二三三"
print(str(n1))
print(str(n2))
print(int(n2))  # 浮点数转换为整数时不会进行四舍五入，而是舍去小数部分只保留整数
print(int(2.99))  # 舍去小数部分
# print(int("2.33"))  # 字符串为非整数字类型，会报错
print(int(n3))
print(float(n1))
print(float(n3))
# print(int(n4))  # 非数字字符串转换为数字类型会报错
print(bool(1))
print(bool("2"))
print(bool(0))
