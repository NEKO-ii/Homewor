# open(url, [mode], [encoding])  文件打开
# file.close() 关闭文件资源

# open() 函数打开文件的参数有如下几种:
# r      只读模式
# w或wt  文本模式写，打开文件时清空文件数据
# wb     二进制写，打开文件时清空文件数据
# a      追加写，只能在文件末尾追加
# a+     可读写模式，写只能写在文件末尾
# w+     可读写模式，打开文件时清空文件数据，可写在任意位置
# r+     可读写模式，写可以写在文件任意位置

file = open("./总结/file/032.txt", "r", encoding="UTF-8")

# 文件对象的常用方法:
# read([size])          读取文件，默认读取整个文件，可选变量size设置读取的字节/字符限制
# readline()            从文本文件中读取一行
# readlines()           将文本文件的每一行作为一个字符串，并返回每行字符串的列表
# write(str)            将字符串写入文本文件(不换行)
# writelines(s_list)    将字符串列表写入文本文件(不添加换行符)
# seek(offset,[mode])   移动文件指针，offset为移动距离，mode默认为0:从文件头开始计算；1:从当前位置开始计算；2:从文件末尾开始计算
# tell()                返回文件指针当前位置
# flush()               将缓冲区内容写入文件
# close()               关闭文件释放资源

print("读取文件全部内容:")
print(file.read())
file.seek(0)  # 因为每次读完会将指针(光标)移动，所以每次读之前要将指针移动到起始位置
print("读取一行")
print(file.readline())
file.seek(0)
print("读取每一行返回列表")
print(file.readlines())

file.close()
file = open("./总结/file/032.txt", "w+", encoding="UTF-8")
print("\n重新以文本读写模式(w+)打开文件，此时文件内容已清空")

file.write("line 1\n")
file.write("line 2\n")

print("\n写入两行\n\nflush前读取")
print(file.read())
file.seek(0)

file.flush()

print("flush后读取")
print(file.read())

file.seek(0)
print("光标移动到起始位置")

file.writelines(["line 3\n","line 4\n","line 5\n"])
file.flush()
file.seek(0)

print("\n写入多行并flush后读取")
print(file.read())

print("关闭文件")
file.close()
