# 输入函数 input("输入提示") 返回的输入类型为字符串Str 括号中的输入提示用于提示用户应该输入什么内容
name = input("请输入你的名字 > ")
print("hello " + name)

val1 = input("\n下面是两数相加操作\n请输入第一个数 > ")
val2 = input("请输入第二个数 > ")
plus = float(val1) + float(val2)
print("两数之和为: " + str(plus))
