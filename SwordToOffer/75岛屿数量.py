'''
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。
我们只考虑上下左右为相邻。岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 
判断岛屿个数。 
'''
class Solution:
    def solve(self , grid ):
        # write code here
        r , c = len(grid) , len(grid[0])
        if r == 0 or c == 0: return 0
        nums = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':    # 一旦触碰到陆地，就搜索完整个大陆
                    nums += 1
                    self.dfs(grid , i , j)
        return nums

    def dfs(self , grid , i , j):
        grid[i][j] = 0
        rol ,col = len(grid) , len(grid[0])
        # 判断上下左右是否相连
        for i ,j in [(i - 1 , j) , (i + 1 , j) , (i , j - 1) , (i , j + 1)]:
            # 如果相连则继续搜索
            if 0 <= i < rol and 0 <= j < col and grid[i][j] == '1':
                self.dfs(grid , i , j)