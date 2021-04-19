'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下
递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
'''
Solution: 从左下角开始遍历
'''

def Find(target, array):
    row = len(array)-1  #行数
    col = len(array[0])-1  #列数
    i = row
    j = 0
    while i>=0 and j<=col:
        if target > array[i][j]:
            j += 1
        elif target < array[i][j]:
            i -= 1
        else:
            return True
    return False

arr = [[1,2,3,4],\
       [2,3,4,5],\
       [3,4,5,6]]

print(Find(9, arr))
print(Find(5, arr))
