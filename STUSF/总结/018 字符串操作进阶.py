# 字符串是一个字符序列，既然是序列那么就有每个字符的索引，这里的索引是满足常规情况的索引规则的，也有正向索引和逆向索引
# 字符串为不可变序列，对字符串的操作将产生新的字符串，适用于如下所有操作

# 字符串进阶操作:
# --------查询---------
# [str].index(substr)       查找子串substr第一次出现的位置，子串不存在时抛出ValueError
# [str].rindex(substr)      查找子串substr最后出现的位置，子串不存在时抛出ValueError
# [str].find(substr)        查找子串substr第一次出现的位置，子串不存在时返回-1
# [str].rfind(substr)       查找子串substr最后出现的位置，子串不存在时返回-1
# 查询子字符串位置时，返回的位置是子串第一个字符在原字符串中的索引
print("-------------------------------子串查询演示")
str = "233abcabc"
print("str: ", str, end="\n\n")
print("3出现的第一个位置: ", str.index("3"))
print("3最后一次出现的位置: ", str.rindex("3"))
# print("d出现的第一个位置: ",str.rindex("d"))  # ValueError
print("abc出现的第一个位置: ", str.find("abc"))
print("d出现的第一个位置: ", str.rfind("d"))

# ------大小写转换------
# [str].upper()         所有字母转换为大写
# [str].lower()         所有字母转换为小写
# [str].swapcase()      所有字母大小写切换
# [str].capitalize()    第一个字母转换为大写，其余均小写
# [str].title()         每个单词第一个字母转换为大写，其余均小写
# 这些操作均不会改变原字符串
print("\n-------------------------------大小写转换演示")
str = "hElLO woRlD"
print("str: ", str, end="\n\n")
print("转换为大写: ", str.upper())
print("转换为小写: ", str.lower())
print("大小写切换: ", str.swapcase())
print("首字母大写: ", str.capitalize())
print("单词首大写: ", str.title())

# ------字符串对齐------
# [str].center(wide,[fill]) 居中    wide指定宽度，可选参数fill指定填充符(默认为空格)，宽度小于字符串长度返回原字符串
# [str].ljust(wide,[fill])  左对齐  wide指定宽度，可选参数fill指定填充符(默认为空格)，宽度小于字符串长度返回原字符串
# [str].rjust(wide,[fill])  右对齐  wide指定宽度，可选参数fill指定填充符(默认为空格)，宽度小于字符串长度返回原字符串
# [str].zfill(wide)         右对齐  wide指定宽度，左边用0填充，宽度小于字符串长度返回原字符串
print("\n-------------------------------字符串对齐演示")
str = "hello"
print("str: ", str, end="\n\n")
print("居中: |", str.center(11, " "), "|")
print("左齐: |", str.ljust(11, " "), "|")
print("右齐: |", str.rjust(11, " "), "|")
print("右齐: |", str.zfill(11), "|")

# ------字符串分割------
# [str].split([sep=" "],[maxsplit=N])    从左向右分割字符串，sep=" "指定分割符(默认为空格)，maxsplit=N指定最大分割次数为N(默认全部分割)
# [str].rsplit([sep=" "],[maxsplit=N])   从右向左分割字符串，sep=" "指定分割符(默认为空格)，maxsplit=N指定最大分割次数为N(默认全部分割)
print("\n-------------------------------字符串分割演示")
str = "hello world 2|3|3|3"
print("str: ", str, end="\n\n")
print("按空格正向分割全部: ", str.split())
print("按空格正向分割一次: ", str.split(maxsplit=1))
print("按空格反向分割一次: ", str.rsplit(maxsplit=1))
print("按竖线正向分割全部: ", str.split(sep="|"))

# ------字符串判断------
# [str].isidentifier()  判断字符串是否为合法标识符(只能含有字母数字下划线且开头不能是数字)中文也行？？？！！！
# [str].isspace()       判断字符串是否全部由空白字符(空格、回车、换行)组成
# [str].isalpha()       判断字符串是否全部由字母组成,汉字也行
# [str].isdecimal()     判断字符串是否全部由十进制数(阿拉伯数字0-9)组成
# [str].isnumeric()     判断字符串是否全部由数字(阿拉伯数字0-9，中文数字一、二、贰，罗马数字Ⅰ、Ⅱ)组成
# [str].isalnum()       判断字符串是否全部由字母或数字组成，汉字也行
print("\n-------------------------------字符串判断演示")
str1 = "hello_world_2333"
str2 = "hello233"
str3 = "hello"
print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3, end="\n\n")
print("str1全为合法标识？ ", str1.isidentifier())
print("str1全为空白字符？ ", str1.isspace())
print("str2全由字母组成？ ", str2.isalpha())
print("str3全由字母组成？ ", str3.isalpha())
print("str2全为十进制数？ ", str2.isdecimal())
print("str2全由数字组成？ ", str2.isnumeric())
print("str2全为字母数字？ ", str2.isalnum())
print("str3全为字母数字？ ", str3.isalnum())

# ------字符串比较------
# 字符串也可以比较，使用符号(<,>,<=,>=,==,!=)
# 字符串比较是比较原始值(ordinal value)，从左向右依次比较每个字符，字符相同则比较下一个，直到出现不同字符
# 字符原始值查看函数 ord(char)
print("\n-------------------------------字符串比较演示")
str1 = "NEKO"
str2 = "NICO"
print("str1: ", str1)
print("str2: ", str2)
print("ord(E) = ", ord("E"))
print("ord(I) = ", ord("I"))
print()
print("str1 > str2 ? ", str1 > str2)
print("str1 == str2 ? ", str1 == str2)
print("str1 != str2 ? ", str1 != str2)

# ------字符串切片------
# 与列表切片类似，也是通过索引完成的
# str[start:end:step]
# 用法一样，就不演示了

# --------其他--------
# [str].replace(substr,restr,[N])   将字符串str的子字符串substr替换为restr，返回替换后的新字符串，第三个参数N代表替换几次(默认全换)
# [str].join(obj)                   以str为连接符，将obj(列表或元组)中的字符串连接为一个字符串
# [str].__len__()                   返回字符串长度，也可以使用len(str)
print("\n-------------------------------其他操作演示")
str1 = "hello "
str2 = "wor"
str3 = "ld"
print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3, end="\n\n")
print("str1中ll替换为r: ", str1.replace("ll", "r"))
print("str2和str3合并后与str1连接: ", "".join([str1, str2, str3]))
