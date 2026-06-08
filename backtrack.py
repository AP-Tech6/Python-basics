"""

# Directions used in Backtracking

matrix[i-1][j]  # Up
matrix[i+1][j]  # Down
matrix[i][j-1]  # Left
matrix[i][j+1]  # Right
Example Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Indexes:

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
Suppose:

i = 1
j = 1
Current cell:

matrix[1][1] = 5
Visual:

1  2  3
4 [5] 6
7  8  9
Up
matrix[i-1][j]
matrix[0][1]
Output:2
Down
matrix[i+1][j]
matrix[2][1]
Output:8
Left
matrix[i][j-1]
matrix[1][0]
Output:4
Right
matrix[i][j+1]
matrix[1][2]
Output:6
Visualization
      Up(2)
        ↑
Left(4) 5 Right(6)
        ↓
     Down(8)
"""

def wildfire(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
        return
    grid[i][j]=2
    wildfire(grid,i+1,j)
    wildfire(grid,i-1,j)
    wildfire(grid,i,j+1)
    wildfire(grid,i,j-1)
matrix=[[1,1,1,1],[1,0,0,0],[0,0,1,1],[1,0,0,0]]
wildfire(matrix,0,0)
count=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
                   count+=1
print(count)