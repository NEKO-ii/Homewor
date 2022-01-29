# os模块内的方法可以完成一些操作系统功能

# os.system(command:str)执行操作系统指令，其作用相当于在控制台执行指令
# os.startfile(exe file)运行可执行文件
# os.getcwd()获取当前工作目录(控制台的路径)
# os.listdir(url)获取指定路径下的文件、文件夹列表
# os.mkdir(url,[mode])创建目录
# os.makedirs(url1/url2/...,[mode])创建多级目录
# os.rmdir(url)删除目录
# os.removedirs(url1/url2/...)删除多级目录
# os.chdir(url)将指定目录设置为当前工作目录
# os.path.abspath(url)获取文件或目录的绝对路径
# os.path.splitext(file_name)分离文件名和扩展名，返回元组
# os.path.basename(url)从一个目录中提取文件名
# os.path.dirname(url)从一个目录中提取文件路径(不包含文件名)
# os.path.realpath(__file__)获取文件全路径(包含文件名)
# os.path.join(url,file_name)将目录与目录/目录与文件名拼接
# os.walk(url)获取路径下所有文件(包含子文件夹内的文件)，每个子文件夹单独返回一个元组

# 使用前导入
import os

print("输出Python版本信息:")
os.system("python --version")

print("\n打开可执行文件...")
os.startfile(".\\总结\\file\\034.jpg")

print("\n当前工作目录:")
print(os.getcwd())

print("\nfile目录下的文件:")
print(os.listdir(".\\总结\\file"))

print("\n当前文件绝对路径:")
print(os.path.abspath("034 os模块.py"))
print("分离文件名和扩展名: ",os.path.splitext("034 os模块.py"))
url=os.path.realpath(__file__)
print("当前文件全路径: ",url)
print("提取文件名: ",os.path.basename(url))
print("提取路径地址: ",os.path.dirname(url))

print("\n我写的所有文件: ")
for item in os.walk("./总结"):
    print(item)

input("输入任意值退出程序 > ")
