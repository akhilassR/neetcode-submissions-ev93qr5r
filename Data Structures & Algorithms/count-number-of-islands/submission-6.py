class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #logic:
        # start from first '1', check left, right, up, down for similar '1'
        # if encountered, recursively call the check for that nodes neighbours
        # keep going until no more'1's, and make sure to save all seen nodes in a set or smth

        # then move on to the next location of unseen node, and complete until all nodes traversed
        # islands = 0

        # for each cell in grid:
        #     if cell is land:
        #         islands += 1
        #         dfs(cell)  # visit all connected land

        #     def dfs(r, c):
        # # 1. Stop if out of bounds
        # # 2. Stop if this cell is water
        # # 3. Mark this land as visited
        # # 4. Explore up, down, left, right

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(r, c):
            #for invalid values:
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or (r,c) in visited):
                return
            # record visitation
            visited.add((r,c))
            # explore neighbours to include all associated nodes of the same island to one
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands