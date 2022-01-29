n = 15  #设置行数

# 输出n行星号，第n行有n个星号，组成直角三角形(直角在左)
print("直角三角型1")
for i in range(1, n + 1):
    for _ in range(i):
        print("*", end=" ")
    print()

# 输出n行星号，第n行有n个星号，组成直角三角形(直角在右)
print("\n直角三角型2")
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end=" ")
    for _ in range(i):
        print("*", end=" ")
    print()

# 输出n行星号，第n行有n个星号，组成金字塔形
print("\n金字塔型1")
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end="")
    for _ in range(i):
        print("*", end=" ")
    print()

# 输出n行星号，第i行有n-i个星号，组成倒三角
print("\n金字塔型2")
for i in range(1, n + 1):
    for _ in range(1, i):
        print(" ", end="")
    for _ in range(n + 1 - i):
        print("*", end=" ")
    print()
