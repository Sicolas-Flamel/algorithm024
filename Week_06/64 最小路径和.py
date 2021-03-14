# 分析
# 动态规划，左上角走到最右下角
# 还可以用 BFS 来做，一层层加起来保存，直到走到最右下角的元素

# 设定 d[i][j] 为 从起点（即左上i行j列的最短路径。
# d[i][j] = min(d[i-1][j],d[i][j-1])+grid[i][j]
# 若  i=0，为上边界，j=0 为左边界，直接加上之前的就可以。

def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
        
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # 这里控制的是非边界元素
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[-1][-1]
