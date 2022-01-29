# coding:UTF-8
# 语法规范

# 参数之间的逗号后加一个空格  print("hello", "world")
# 纯注释行#后加一个空格，代码后注释#前加两个空格，#后加一个空格
# 文件末尾增加一空行
"""多行注释其实就是三引号字符串
这个字符串不赋予任何变量就是多行注释"""

# 可通过注释来决定python文件的编码格式(默认为UTF-8)，写在文件开头如：coding:UTF-8
# pass占位,pass在程序执行时并不会产生实际作用，它的用处是搭建代码结构，如if的某一个分支暂时不写其语句，可用pass进行占位来保证程序顺利执行
# 在Python中,类型属于对象,变量是没有类型的，例如val="python"，产生一个类型为str，值为python的对象，变量val只是引用内存中的这一变量(指针)

# 获取文件路径:
# 获取全路径(包含文件名):   os.path.realpath(__file__)
# 获取全路径(不含文件名):   os.path.dirname(os.path.realpath(__file__))
# 获取文件名              os.path.basename(os.path.realpath(__file__))

# 第三方模块安装命令: pip install [module_name]
