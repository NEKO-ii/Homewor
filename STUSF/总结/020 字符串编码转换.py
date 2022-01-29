# 字符串在传输时要对字符进行编码，转换为字节传输
# 编码转换函数:
# [str].encode(encoding="UTF-8") 将字符串以UTF-8格式编码，返回值为byte字节类型
# [byte].decode(encoding="UTF-8") 将byte字节以UTF-8格式规则解码为字符串

str1 = "233"
str2 = "neko"
str3 = "字符串"
print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)

print("\n---------------------------------以UTF-8格式编码")
by1 = str1.encode(encoding="UTF-8")
by2 = str2.encode(encoding="UTF-8")
by3 = str3.encode(encoding="UTF-8")
print("str1[byte]: ", by1)
print("str2[byte]: ", by2)
print("str3[byte]: ", by3)
# 根据输出结果可以看出，在UTF-8编码格式中，数字和英文字母占1字节，中文占3字节

print("\n---------------------------------以GBK格式编码")
by1 = str1.encode(encoding="GBK")
by2 = str2.encode(encoding="GBK")
by3 = str3.encode(encoding="GBK")
print("str1[byte]: ", by1)
print("str2[byte]: ", by2)
print("str3[byte]: ", by3)
# 根据输出结果可以看出，在GBK编码格式中，数字和英文字母占1字节，中文占2字节

print("\n---------------------------------byte字节解码")
print("str1[GBK]: ", by1.decode(encoding="GBK"))
print("str2[GBK]: ", by2.decode(encoding="GBK"))
print("str3[GBK]: ", by3.decode(encoding="GBK"))
print("str1[UTF-8]: ", by1.decode(encoding="UTF-8"))
print("str2[UTF-8]: ", by2.decode(encoding="UTF-8"))
# print("str3[UTF-8]: ",by3.decode(encoding="UTF-8"))  # UnicodeDecodeError
# 中文字符通过GBK编码得到的字节by3无法使用UTF-8格式解码，但是数字和英文字母可以
