# 模块(module)其实就是一个包含解决特定问题的函数、变量、类的.py文件
# 使用模块能方便其他程序导入，避免函数或变量名冲突，并提高代码的可维护性与可重用性
# 模块导入方式: import module_name [as][other_name]             导入一个模块的所有内容
#             from module_name import fun/class/val_name      导入一个模块的特定函数/类/变量
# 若所使用的的模块在其他目录，可使用sys.path.append(url)来添加系统路径
import sys
sys.path.append("./总结/file")
import module

stu=module.Student("NEKO",22,"SE19-5")
stu.show()
print(stu)
module.fun()

# Python的常用内置模块:
# sys       Python解释器及其环境操作的标准库
# time      时间相关函数标准库
# os        操作系统功能访问标准库
# math      标准算数运算函数标准库
# calendar  日期相关函数标准库
# urllib    网络服务器数据读取标准库
# json      用于使用json序列化与反序列化对象
# re        用于在字符串中使用正则表达式匹配和替换
# decimal   用于在十进制计算中精确控制运算精度、有效位数和四舍五入操作
# logging   用于日志记录
