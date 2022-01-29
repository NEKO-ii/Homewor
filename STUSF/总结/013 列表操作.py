list = [2, 3, 3, 233, "h", "e", "l", "l", "o"]
f_index = "[0  1  2   3    4    5    6    7    8 ]     正向索引"
r_index = "[-9-8 -7  -6   -5   -4   -3   -2   -1 ]     反向索引"
print(list)
print(f_index)
print(r_index)

# list列表的相关函数
# [list].index(val)             查看列表中某个元素的索引,若列表中有多个相同元素，则返回正向第一个的索引，若元素不存在，则抛出ValueError
# [list].index(val,start,end)   可以规定查找的索引范围由start到end，不包括end
# [list][start : end : step]    可以对列表list进行切片操作,范围包括start不包括end，step默认为1；setp为负数时，反向切，从索引为start切到end(不包括end)，切片结果为新的列表对象
# [list][ : end : step]         step为正数时，从索引为0开始切到end(不包括end)；step为负数时，反向切，从最后面切到索引为end(不包括end)为止
# [list][start : : step]        step为正数时，从索引为start开始切到最后；step为负数时，反向切，从索引为start切到最前面为止
# [list][ : : -1]               可用来将原列表进行倒置排序
# [list].append(val)            向list列表最后追加一个元素
# [list].extend(list2)          将list2列表中的所有元素追加到list末尾
# [list].insert(index,val)      在索引为index处插入元素val，从插入位置原来的元素到最后的所有元素索引改变
# [list][start : end] = list2   将list列表索引从start到end(不包括end)的元素替换为list2的所有元素，特殊的，当start = end时即为在该处插入多个元素
# [list].remove(val)            从list列表中删除元素val，若有多个相同元素则只删除第一个，若没有该元素则抛出ValueError
# [list].pop(index)             删除索引为index的元素，若不指定索引则删除最后一个，所索引超出范围则抛出IndexError
# [list][start : end] = []      将list列表从索引start到end(不包括end)的元素删除(本质上是替换为空列表，可理解为删除)
# [list].clear()                清空列表所有元素(此时列表依然存在，为空列表)
# del [list]                    删除列表
# [list].sort(reverse=False)    列表排序，默认reverse=False(升序)，reverse=True为降序，会使列表发生改变
# sorted(list,reverse=False)    该函数为内置函数，可以用于list列表排序，默认reverse=False(升序)，函数返回值为新的列表，原列表不会发生改变

print("\n----------------------------------------------index()函数演示")
print("列表中元素e的索引为: ", list.index("e"))
print("列表中元素3的索引为: ", list.index(3))
# print("\n列表中元素x的索引为: ",list.index("x"))  # 元素x不存在，抛出ValueError
print("在索引范围2-6中查找3的索引为: ", list.index(3, 2, 7))

print("\n----------------------------------------------list切片演示")
print("截取索引范围4-8的元素为: ", list[4:9])
print("截取开头三个元素: ", list[:3])
print("截取最后五个元素: ", list[-5:])
print("反向截取最后五个元素: ", list[:-6:-1])
print("从索引6的元素反向截取到索引4的元素: ", list[6:3:-1])

# 由于列表为可迭代对象，所以文件[012 列表.py]中列表的遍历输出方法可以改为
print("\n----------------------------------------------list遍历进阶")
print("正向索引输出")
for val in list:
    print(val, end=" ")
print("\n反向索引输出")
for val in list[::-1]:  # 遍历倒置后的列表即可
    print(val, end=" ")

print("\n\n----------------------------------------------list增加元素")
print("末尾追加一个元素")
list.append("new1")
for val in list:
    print(val, end=" ")

print("\n末尾追加多个元素")
list2 = ["new2", "new3", "new4"]
list.extend(list2)
for val in list:
    print(val, end=" ")

print("\n索引为9处插入一个元素")
list.insert(9, "new0")
for val in list:
    print(val, end=" ")

print("\n索引为9到13的元素替换为new")
list[9:14] = ["new"]
for val in list:
    print(val, end=" ")

print("\n索引为9的位置插入new2和new1")
list[9:9] = ["new2", "new1"]
for val in list:
    print(val, end=" ")

print("\n\n----------------------------------------------list删除元素")
print("删除第一个3")
list.remove(3)
for val in list:
    print(val, end=" ")

print("\n删除索引为8的元素")
list.pop(8)
for val in list:
    print(val, end=" ")

print("\n删除最后一个元素")
list.pop()
for val in list:
    print(val, end=" ")

print("\n删除索引3-7的元素")
list[3:8] = []
for val in list:
    print(val, end=" ")

print("\n清空列表")
list.clear()
print(list)

print("\n初始化列表")
del list
list = [2, 3, 3, 233, 80, 25, 99]
print(list)

print("\n----------------------------------------------list列表排序")
list.sort()
print("升序排序",list)
list.sort(reverse=True)
print("降序排序",list)
list3=sorted(list,reverse=False)
print("内置函数sorted()升序排序 ",list3)
print("原列表不发生变化         ",list)
