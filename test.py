class Solution:
    def solve(self, grid):
        r, c = len(grid), len(grid[0])
        if r == 0 or c == 0: return 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    self.dfs(grid, i, j)
        return grid
    
    def dfs(self, grid, i, j):
        rol, col = len(grid), len(grid[0])
        if 0 < i < rol-1 and 0 < j < col-1 and grid[i][j] == '0':
            grid[i][j] = '1'
            for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 < i < rol-1 and 0 < j < col-1 and grid[i][j] == '0':
                    self.dfs(grid, i, j)

mat = [['0','1','0'],['1','0','1'],['0','1','0']]
s = Solution()
res = s.solve(mat)
for i in res:
    sub = ''
    for j in i:
        sub += j
    print(sub)