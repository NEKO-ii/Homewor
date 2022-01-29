# 字符串驻留机制: 不同字符串的值相同，其在内存中只存储一份
# 交互模式(cmd-python命令行)下触发驻留机制的情况:
# 1  字符串长度为0或1时
# 2  符合表示符的字符串(只含有字母[a-z]、数字(int)、下划线(_)，有空格也不行除非长度为1)
# 3  [-5,256]之间的整数数字(int型)，这里不是字符串，只是一起拿来演示
# 4  在编译时符合上述规则才进行驻留，运行后再重新满足上述规则不进行驻留
# 5  可使用str1 = sys.intern(str2)来使两个值相等的字符串存储于同一内存

# 下面是python交互式命令行进行的操作
# PS D:\Code\Workspace\Python\STUSF> python
# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s1=""
# >>> s2=""
# >>> s1 is s2
# True              满足规则1，驻留
# >>> s1="s"
# >>> s2="s"
# >>> s1 is s2
# True              满足规则1，驻留
# >>> s1="abc"
# >>> s2="abc"
# >>> s1 is s2
# True              满足规则2，驻留
# >>> s1="abc%"
# >>> s2="abc%"
# >>> s1 is s2
# False             违反规则2，不驻留
# >>> id(s1)        查看内存id
# 1780455553904
# >>> id(s2)
# 1780455554928
# >>> a=" "
# >>> b=" "
# >>> a is b
# True              满足规则1，驻留
# >>> a="  "
# >>> b="  "
# >>> a is b
# False             违反规则2，不驻留
# >>> a="abc"                   编译时满足规则2
# >>> b="ab"+"c"                编译时满足规则2 (其实+也是一种运算，但是这种简单的情况在编译时会自动优化为"abc")
# >>> c="".join(["ab","c"])     编译时违反规则2，但运行时使用join()函数连接后满足规则2
# >>> a is b
# True                          满足规则4，驻留
# >>> a is c
# False                         违反规则4，不驻留
# >>> a=-5
# >>> b=-5
# >>> a is b
# True              满足规则3，驻留
# >>> a=-6
# >>> b=-6
# >>> a is b
# False             违反规则3，不驻留
# >>> a=-1.1
# >>> b=-1.1
# >>> a is b
# False             违反规则3，不驻留
# >>> a="-5"
# >>> b="-5"
# >>> a is b
# False             违反规则2，不驻留
# >>> import sys
# >>> a=sys.intern(b)
# >>> a is b
# True              使用操作5强制处于同一内存

# 下面演示的这三个字符串，显然不满足规则2，但是运行后其内存id确是一致的，原因是VS Code、PyCharm等编译器为了节省内存，对字符串的内存存储进行了优化
print("--------------------------------------字符串驻留机制演示")
str1 = 'hello world'
str2 = "hello world"
str3 = '''hello world'''
print("str1: ", str1, " id: ", id(str1))
print("str2: ", str2, " id: ", id(str2))
print("str3: ", str3, " id: ", id(str3))
print("str1 is str2 ? ", str1 is str2)

# 内存驻留的优点：
# 需要值相同的字符串时直接从字符串池中取用同值字符串，避免频繁创建和销毁，提升效率节约内存
# str类的str.join([str1,str2,...])方法用于拼接字符串，该方法先计算所有字符的长度然后再拷贝，过程中只new了一次对象，效率比连接符(+)要高，所以优先使用join方法
