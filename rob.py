#a robot has to reach from top of a grid to bottom, how many paths are possible to reach its required destination
"""
Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).
The matrix contains only two possible values:
0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list

ChatGPT5:59 PM
"""

def maze(grid,path,i,j,n):
    if i==n and j==n:
        print(path)
    if i+1<=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j,n)
    if j+1<=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1,n)
grid=[[1,1,0,1],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
n=len(grid)
maze(grid," ",0,0,n-1)
