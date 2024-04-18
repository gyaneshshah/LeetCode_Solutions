class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        column_len = len(grid[0])
        perimeter = 0
        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                if column==1:
                    # Check the square before
                    if j-1<0:
                        perimeter+=1
                    elif grid[i][j-1]==0:
                        perimeter+=1
                    # Check the square below
                    if i-1<0:
                        perimeter+=1
                    elif grid[i-1][j]==0:
                        perimeter+=1
                    # Check the next square
                    if j+1>=column_len:
                        perimeter+=1
                    elif grid[i][j+1]==0:
                        perimeter+=1
                    # Check the square above
                    if i+1>=row_len:
                        perimeter+=1
                    elif grid[i+1][j]==0:
                        perimeter+=1
        return perimeter
