from decimal import Decimal

# 整数 int(Integer)
print("\n----------------------------------------整数 int")
val1 = 0
val2 = 1
val3 = -1
print(val1, type(val1))
print(val2, type(val2))
print(val3, type(val3))

# 整数可转换为其他进制数
# 0b(二进制),0o(八进制),0x(十六进制)
# print()函数都以十进制进行输出
print("十进制233     :", 233)
print("二进制11101001:", 0b11101001)
print("八进制351     :", 0o351)
print("十六进制E9    :", 0xE9)

# 进制转换函数
print("\n----------------------------------------进制转换")
# 转十进制int("n",x) 其中n为待转数，x为待转数的进制数，如将二进制11101001转为十进制则为int("11101001",2),注意第一个参数为字符串类型
# 转二进制bin(n) 其中n为十进制数
# 转八进制oct(n) 其中n为十进制数
# 转十六进制hex(n) 其中n为十进制数
# 非十进制数转换时需要先转换为十进制，再进行转换，如八进制351转为16进制:hex(int("351",8))
print(int("11101001", 2))
print(hex(int("351", 8)))

# 浮点数 float
print("\n----------------------------------------浮点数 float")
val4 = 3.14159265
print(val4, type(val4))
# 浮点数精确计算
# 浮点数由于小数位数的不确定，直接计算结果可能出现误差
val5 = 1.1
val6 = 2.2
val7 = 2.1
print(val5 + val6)
print(val5 + val7)
print(Decimal("1.1") + Decimal("2.2"))

# 布尔值 bool 可转正数计算 true=1 flase=0
print("\n----------------------------------------布尔值 bool")
b1 = True
b2 = False
print(b1, type(b1))
print(b2, type(b2))
print(b1 + b2 + 1)

# 字符串 String
# 字符串是不可变得字符序列
print("\n----------------------------------------字符串 String")
# 单双引号可定义一个单行的字符串，三引号可以定义多行字符串
s1 = 'hello'
s2 = "hello"
s3 = '''hel
lo'''
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
