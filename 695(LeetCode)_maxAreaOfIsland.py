class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        is_inbound = lambda r, c: 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and not visited[r][c]
        
        def dfs(r, c):
            island_area = 1
            
            for neighbor_row, neighbor_col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if is_inbound(neighbor_row, neighbor_col):
                    visited[neighbor_row][neighbor_col] = True
                    island_area += dfs(neighbor_row, neighbor_col)
        
            return island_area
                
        
        maximum_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    maximum_area = max(maximum_area, dfs(r, c))
                    
        return maximum_area