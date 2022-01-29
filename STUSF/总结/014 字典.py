# 字典(dictionary)和列表都是Python的数据结构，本质上也是一个长度可变序列，不同的是字典以(键-值)对应关系存储，而且列表为无序序列
# 字典结构为 [name] = {key1:val1, key2:val2, key3:val3,...}
# 字典中的 key 必须为不可变对象
# 键-值对在字典中的存储位置是根据 键 的哈希值，求哈希值的函数为 : hash(key)
# 由于哈希值的确定性，键-值对在字典中的存储位置和先后顺序是固定的
# 字典是一种占用较大内存的数据结构，但相应的查询键值的时间很短，是一种用空间换时间的数据结构

# 字典创建方式:
# 直接用{key : val, ...}赋予变量
# 使用内置函数 dict(key1 = val1, key2 = val2, ...)
print("---------------------------------------字典创建")
dict1 = {"贰": 2, "叁": 3, "叁": 3}  # 相同键-值对只保留一个，同一键不可有两个值
dict2 = dict(贰=2, 叁=3)
dict3 = {}  # 空字典
print("dict1  ", dict1)
print("dict2  ", dict2)
print("dict3  ", dict3)

# 字典取值方式:
# [name][key]                    如 dict["贰"]       若key不存在，会抛出KeyError异常
# [name].get(key, [difault])     如 dict.get("贰")   若key不存在，返回difault，默认default不写，返回None
print("\n---------------------------------------字典取值")
print("key = \"贰\"  value = ", dict1["贰"])
print("key = \"叁\"  value = ", dict1.get("叁"))
print("key = \"肆\"  value = ", dict1.get("肆", "键不存在"))

# 可用 in 和 not in 来判断 key 是否存在于字典中
# del [name][key]       删除对应的键-值对
# [name][key] = value   新增/修改键-值对
# [name].clear()        清空字典
print("\n---------------------------------------字典操作")
print("key=贰 是否在字典dict1中? ", "贰" in dict1)
print("key=肆 是否在字典dict1中? ", "肆" in dict1)
del dict2["叁"]
print("删除key=\"叁\"后的字典dict2 ", dict2)
dict2["叁"] = 3
print("新增键-值对 \"叁\":3 后的字典dict2 ", dict2)
dict2.clear()
print("清空后的字典dict2 ", dict2)
dict1["叁"] = 4
print("修改键 \"叁\" 的值为 4 后的字典dict1 ", dict1)
dict1["叁"] = 3

# 字典视图
# [name].keys()     获取字典中所有键
# [name].values()   获取字典中所有值
# [name].items()    获取所有键-值对
print("\n---------------------------------------字典视图")
keys = dict1.keys()
values = dict1.values()
items = dict1.items()
print(keys)
print(values)
print(items)
# 存储到列表
l_keys = list(keys)
l_values = list(values)
l_items = list(items)  # 列表中的每一项其实是一个元组，后面要学
print("keys 列表: ", end="")
for i in l_keys:
    print(i, end=" ")
print("\nvalues 列表: ", end="")
for i in l_values:
    print(i, end=" ")
print("\nitems 列表: ", end="")
for i in l_items:
    print(i, end=" ")
print()

# 字典遍历
# 使用 for-in 循环: 如 for item in dict1: print(item) 这里遍历用到的变量item其实是遍历的dict1的键key
print("\n---------------------------------------字典遍历")
print("遍历字典 dict1 的键: ",end="")
for item in dict1:
    print(item, end=" ")
print("\n遍历字典 dict1 的值: ",end="")
for item in dict1:
    print(dict1.get(item), end=" ")

# 字典生成的另一种方法
# 内置函数 zip(list1,list2) 使用两个list列表，将两个列表相同索引处的值打包为元组，再将元组组成新的list列表
# 再使用语法 {key:value for key,value in zip(list1,list2)} 生成字典，若两个列表长度不同，则生成的字典只包含能够键-值配对的部分
print("\n\n---------------------------------------通过列表生成字典")
list1=["贰","叁","肆"]
list2=[2,3,4]
dict={key.upper():value for key,value in zip(list1,list2)}
for item in dict:
    print(item,":",dict.get(item), end="    ")
