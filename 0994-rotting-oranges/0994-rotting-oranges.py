class Solution:
    def finalCheck(self, m):
        row = len(m)
        col = len(m[0])
        flag = True
        for r in range(row):
            for c in range(col):
                if m[r][c] == 1:
                    flag = False
                    break
        return flag 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # print(len(grid))
        rows = len(grid)
        cols = len(grid[0])
        mins = 0
        # print(f"{rows} * {cols}")
        q = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c, mins])
        # print(f"Initial q: {q}")
        while q:
            r,c,mins = q.pop(0)
            print(f"r: {r}, c: {c}, mins: {mins}")
            # check right
            if c+1 < cols and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                q.append([r, c+1, mins+1])
                # print(f"After right check: {q}")
            
            # check left
            if c - 1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                q.append([r, c-1, mins + 1])
                # print(f"After left check: {q}")
            
            # check top
            if r - 1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                q.append([r-1, c, mins+1])
                # print(f"After top check: {q}")
            
            # check bottom
            if r + 1 < rows and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                q.append([r+1, c, mins + 1])
                # print(f"After bottom check: {q}")
            # print(f"Grid: {grid}")
        flag = self.finalCheck(grid)
        return mins if flag else -1