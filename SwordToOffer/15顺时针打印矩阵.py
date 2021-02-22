'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 
1  2  3  4 
5  6  7  8 
9  10 11 12 
13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

时间限制：1秒；空间限制：32768K；本题知识点：数组
'''
'''
常规思路，将一次循环分为4步：从左到右、从上到下、从右到左、从下到上，注意避免重复，
每次循环后判断剩余矩阵是否还能继续这样分4步打印，否则直接停止（行列数相同的情况）
或打印一行后停止（列数大于行数的情况）或打印一列后停止（行数大于列数的情况）。
'''
def printMatrix1(matrix):
    l = []
    row = len(matrix)
    column = len(matrix[0])
    xy = 0  # first circle
    while True:
        # break condition
        if xy == row//2:
            # left --> right
            if row%2 == 1:
                for i in range(xy,column-xy):
                    l.append(matrix[xy][i])
            break

        if xy == column//2:
            # up --> down
            if column%2 == 1:
                for i in range(xy,row-xy):
                    l.append(matrix[i][column-1-xy])
            break

        # left --> right-1
        for i in range(xy, column-xy-1):
            l.append(matrix[xy][i])

        # up --> down-1
        for i in range(xy,row-xy-1):
            l.append(matrix[i][column-1-xy])

        # right --> left-1
        for i in range(column-xy-1, xy, -1):
            l.append(matrix[row-xy-1][i])

        # down --> up-1
        for i in range(row-xy-1, xy, -1):
            l.append(matrix[i][xy])

        xy += 1   # next circle

    return l

'''
利用矩阵旋转的思路，每次取出第一行，然后将矩阵逆时针旋转。
'''
def printMatrix2(matrix):
    result = []
    while len(matrix) > 0:
        result += matrix[0]
        matrix = list(zip(*matrix[1:])) #矩阵转置
        matrix = matrix[::-1] #倒序
    return result

'''
Note: 
first transform, then reverse --> rotate anticlockwise
first reverse, then transform --> rotate clockwise
'''

matrix1 = [[1, 2, 3, 4, 5],\
           [6, 7, 8, 9, 10],\
           [11,12,13,14,15]]

matrix2 = [[1, 2, 3, 4, 5],\
           [6, 7, 8, 9, 10],\
           [11,12,13,14,15],\
           [16,17,18,19,20],\
           [21,22,23,24,25]]

print(printMatrix1(matrix1))
print(printMatrix2(matrix1))

print(printMatrix1(matrix2))
print(printMatrix2(matrix2))


