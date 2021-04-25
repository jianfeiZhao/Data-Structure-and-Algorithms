import copy

a = [1,2,{3:4}]
b = a    # 简单赋值，地址不变
c = a.copy()    # 浅拷贝，只改变浅层的地址
d = copy.deepcopy(a)    # 深拷贝，连同深层的地址也改变了

# 其余都为 True
print(id(a) == id(c))    # False
print(id(a) == id(d))    # False
print(id(a[2] == id(d[2])))    # False
# 对于 False 修改其中一个的值，另一个不变