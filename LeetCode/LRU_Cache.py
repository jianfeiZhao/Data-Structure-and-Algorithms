'''
设计数据结构：capacity 参数作为缓存的当前容量，然后实现两个API，
put(key, val) 存入键值对，
get(key) 获取 key 对应的 val，如果 key 不存在则返回 -1。

让 put 和 get 时间复杂度为 O(1)。
区分最近使用的和久未使用的数据；
并且我们要在 cache 中查找键是否已存在；如果容量满了要删除最久的数据；每次访问要把数据更新为最近访问。
'''
import collections
class Solution:
    def __init__(self, k):
        self.dic = collections.OrderedDict()
        self.capacity = k
        
    def get(self, key):
        if key not in self.dic: return -1
        val = self.dic.pop(key)
        self.dic[key] = val    # 在末尾重新加入
        return val
    
    def set(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:   # have capacity to store
                self.capacity -= 1   # capacity reduce one
            else:
                self.dic.popitem(last=False)   # pop the first item
        self.dic[key] = value   # set at the end


s = Solution(3)
s.set(1,1)
s.set(2,'a')
s.set(3,5)
print(s.dic)
print(s.get(1))
print(s.dic)
print(s.get(5))