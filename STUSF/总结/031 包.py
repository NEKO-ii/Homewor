# Python中的包与其他面向对象编程语言类似，也是一个分层次的目录结构，他的作用是将一组功能的模块放到一起，使项目结构清晰，方便维护和阅读，同时也能避免模块名称冲突
# 包与一般目录文件夹的区别是，python中的包含有一个名为__init__.py的文件
# 若想直接导入包名即可使用包里的所有模块，需要在__init__.py中将模块导入(导入包时会自动执行__init__.py文件)
# 包的导入: import package_name.module_name      导入包中指定模块
#          import package_name                  导入包中所有模块

import pack

pack.module_a.fun()
pack.module_b.fun()
