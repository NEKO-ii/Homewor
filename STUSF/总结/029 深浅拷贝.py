import copy

# Python中，对象的赋值都是进行对象引用(内存地址)传递
# 使用copy.copy()，可以进行对象的浅拷贝，它复制了对象，但对于对象中的元素，依然使用原始的引用，所以针对原对象中元素(可变数据类型)的修改会影响到copy后的对象
# 使用copy.deepcopy()进行深拷贝，也会创建一个新的对象，对于对象中的元素，深拷贝都会重新生成一份，而不是简单的使用原始元素的引用，所以对原对象的修改不会影响到copy对象
# 对于非容器类型(如数字、字符串、和其他'原子'类型的对象)没有被拷贝一说
# 如果元组变量只包含原子类型对象，则不能深拷贝

list1 = [2, 3, 3, [2, 3, 3]]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
print("列表原值:\nlist1: ", end="")
for item in list1:
    print(item, end=" ")
print("\nlist2: ", end="")
for item in list2:
    print(item, end=" ")
print("\nlist3: ", end="")
for item in list3:
    print(item, end=" ")
print()

list1[3].append(3)

print("\n列表修改后值:\nlist1: ", end="")
for item in list1:
    print(item, end=" ")
print("\nlist2: ", end="")
for item in list2:
    print(item, end=" ")
print("\nlist3: ", end="")
for item in list3:
    print(item, end=" ")
print()

# 根据输出结果可以看出，修改原列表list1会影响到其浅拷贝列表list2，但不会影响到深拷贝列表list3
