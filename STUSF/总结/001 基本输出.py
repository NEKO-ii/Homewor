x = 1.01**365
print(x)

a = 230
b = 3
c = 233
print(c)
print("输出字符串: 233")
print("输出表达式:")
print(a + b)

# 不换行输出
print("this is", " my first python ", "code")
# print("输出内容",end="输出结尾")，其中输出结尾默认为\n即为换行，如果将其改为end=" "则会以空格结尾，不换行

# 转义字符
# \n 换行 在新的一行输出后面的内容
print("hello\nworld")
# \t 水平制表位Tab
# 若tab前为完整制表位(一般为四个字符大小)则该tab占用完整制表位;若此tab前为不完整制表位，则此tab将该制表位补全到四个字符
print("hello\tworld")
print("hell\tworld")
# \r 光标重置(回车？)
# 将光标移动到起始位置开始写，光标处有内容则覆盖原有内容
print("hello\rworld")
print("hello\r***")
# \b 退格，删除光标左边的一个字符
print("hello\bworld")

# 输出特殊符号
print("\\")
print("\"\"")

# 原字符 禁用字符串中的转义字符(字符串前加控制符R) 字符串末尾不能是单个反斜线\(俩\\没事)
print("hello\nworld")
print(R"hello\nworld")

# 单个print()括号里啥也不写通常用于换行
print("\n第一行")
print()
print("\n第三行")


# -------------------------------------------
# 输出到文件
# print("str", file = [file])
