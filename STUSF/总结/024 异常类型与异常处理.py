import traceback
# 异常处理结构:
# 1.    try...except...                       执行try中的语句，当出现异常时执行except中的异常处理语句
# 2.    try...except...else...                执行try中的语句，当出现异常时执行except中的异常处理语句，若没有出现异常则额外执行else中的语句
# 3.    try...except...else...finally...      执行try中的语句，当出现异常时执行except中的异常处理语句，若没有出现异常则额外执行else中的语句，finally中的代码无论如何都会执行，通常用来释放try中出错时申请的资源
# 针对except块:
# 1.    except [ErrorType][as][name]:         发生特定异常时才执行该except代码块
# 2.    except代码块可以写多个，分别处理不同错误

# 针对异常处理机制进行演示:
print("--------------------------------------------------------异常处理演示")
print("下面进行两数相除运算，你将依次输入两个数")
try:
    val1 = int(input("请输入第被除数> "))  #输入得到的字符串需要转为int型，这里输入字母会导致异常，输入字母测试该异常
    val2 = int(input("请输入第除数> "))
    result = val1 / val2  #计算除法时若除数为0则会导致异常，第二个数输入0测试该异常
    print(val1, " ÷ ", val2, " = ", result)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("无效参数,请检查输入数据类型")
except Exception as e:
    print("出现未知异常: ", e)
else:
    print("程序正常运行完毕")
finally:
    print("finally code")

# 异常处理模块:Traceback用于处理异常信息
# traceback.print.exc()可以输出异常信息，相较于直接print(e)，该方法输出的信息更为完整
print("\n--------------------------------------------------------异常输出演示")
try:
    print(1 / 0)
except Exception:
    traceback.print_exc()

# 常见异常类型:
# BaseException	            所有异常的基类
# Exception	                常规错误的基类
# SyntaxError	            Python 语法错误
# ValueError 	            传入无效的参数
# TypeError	                对类型无效的操作
# KeyError	                映射中没有这个键
# IndexError	            序列中没有此索引(index)
# NameError	                未声明/初始化对象 (没有属性)
# SystemExit	            解释器请求退出
# KeyboardInterrupt	        用户中断执行(通常是输入^C)
# StopIteration 	        迭代器没有更多的值
# GeneratorExit 	        生成器(generator)发生异常来通知退出
# StandardError	            所有的内建标准异常的基类
# ArithmeticError 	        所有数值计算错误的基类
# FloatingPointError 	    浮点计算错误
# OverflowError	            数值运算超出最大限制
# ZeroDivisionError	        除(或取模)零 (所有数据类型)
# AssertionError	        断言语句失败
# AttributeError	        对象没有这个属性
# EOFError 	                没有内建输入,到达EOF 标记
# EnvironmentError 	        操作系统错误的基类
# IOError 	                输入/输出操作失败
# OSError 	                操作系统错误
# WindowsError	            系统调用失败
# ImportError 	            导入模块/对象失败
# LookupError 	            无效数据查询的基类
# MemoryError	            内存溢出错误(对于Python 解释器不是致命的)
# UnboundLocalError 	    访问未初始化的本地变量
# ReferenceError	        弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError 	            一般的运行时错误
# NotImplementedError	    尚未实现的方法
# IndentationError	        缩进错误
# TabError	                Tab 和空格混用
# SystemError 	            一般的解释器系统错误
# UnicodeError 	            Unicode 相关的错误
# UnicodeDecodeError 	    Unicode 解码时的错误
# UnicodeEncodeError 	    Unicode 编码时错误
# UnicodeTranslateError	    Unicode 转换时错误
# Warning 	                警告的基类
# DeprecationWarning	    关于被弃用的特征的警告
# FutureWarning 	        关于构造将来语义会有改变的警告
# OverflowWarning	        旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	关于特性将会被废弃的警告
# RuntimeWarning 	        可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	            可疑的语法的警告
# UserWarning	            用户代码生成的警告
