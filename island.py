class Solution:

    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            # boundary condition
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            # water or already visited
            if grid[i][j] == "0":
                return

            # mark visited
            grid[i][j] = "0"

            # down
            dfs(i+1, j)

            # up
            dfs(i-1, j)

            # right
            dfs(i, j+1)

            # left
            dfs(i, j-1)

        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1":

                    count += 1

                    dfs(i, j)

        return count

        #make 1 =>0  conencted ones are counted not separate in places