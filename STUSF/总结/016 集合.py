# 集合一是Python内置的数据结构之一，属于可变序列，与字典相比，集合只有键，但是没有键对应的值，值不能重复
# 其键的存储位置也是通过哈希值确定
# 集合输出时会将整形(int)的数据进行排序，其他类型不会

# 集合的创建
# 使用 [name] = {val1, val2, val3, ...}
# 使用函数 set() 如 s = set(range(11))
# 集合也有生成式 例如 {i*2 for i in range(6)}
print("-------------------------------------集合创建")
se1 = {2, 3, 3, 4}  # 会进行去重
se2 = set(range(3, 8))
se3 = set("NEKO")  # 这样将字符串转为集合会使每个字母成为一个元素(顺序是不确定的，因为是通过哈希值确定存储位置)
se4 = set()  # 空集合，无法直接通过 se4 = {} 创建空集合，因为这样是创建空字典
se5 = {i * 2 for i in range(6)}
print("se1: ", se1)
print("se2: ", se2)
print("se3: ", se3)
print("se4: ", se4)
print("se5: ", se5)

# 集合的操作方法
# [name].add(val)                       向集合中添加一个元素
# [name].update(val | list | tuples)    向集合中添加多个元素
# [name].remove(val)                    移除指定元素，若元素不存在则抛出KeyError
# [name].discard(val)                   移除指定元素，若元素不存在不会抛出异常
# [name].pop()                          字符集合随机删除，其他数据类型默认删除集合中最前面的元素
# [name].clear()                        清空集合
print("-------------------------------------集合操作")
se4.add(2)
print("向空集合 se4 中添加元素2: ", se4)
se4.update({3, 4, 5, 6})
print("向集合 se4 中添加元素3,4,5,6: ", se4)
se4.remove(5)
print("se4 中删除元素5: ", se4)
se4.pop()
print("se4 中删除最前面的元素: ", se4)
se4.clear()
print("清空集合 se4: ", se4)

# 集合的数学操作(均不会使原集合发生变化)
# [se1].issubset(se2)               se1是se2的子集？
# [se1].issuperset(se2)             se1是se2的超集？
# [se1].isdisjoint(se2)             se1与se2没有交集？  (注：这里返回true代表没有交集)
# [se1].intersection(se2)           求se1与se2的交集    (也可以用 se1 & se2 得到两者交集)
# [se1].union(se2)                  求se1与se2的并集    (也可以用 se1 | se2 得到两者并集)
# [se1].difference(se2)             求se1与se2的差集    (这里是se1减去se1和se2的交集，可以用 se1 - se2 得到)
# [se1].symmetric_difference(se2)   求se1与se2的对称差集 (这里是两个集合的并集减去交集，可以用 se1 ^ se2 得到)
print("-------------------------------------集合数学")
print("se1是se2的子集吗？ ", se1.issubset(se2))
print("se3是se2的子集吗？ ", se3.issubset(se2))
print("se2是se1的超集吗？ ", se2.issuperset(se1))
print("se2与se1没有交集吗？ ", se2.isdisjoint(se1))
print("se2与se3没有交集吗？ ", se2.isdisjoint(se3))
print("求se1与se2的交集: ", se1.intersection(se2))
print("求se1与se2的并集: ", se1.union(se2))
print("求se1与se2的差集: ", se1.difference(se2))
print("求se1与se2的对称差集: ", se1.symmetric_difference(se2))
