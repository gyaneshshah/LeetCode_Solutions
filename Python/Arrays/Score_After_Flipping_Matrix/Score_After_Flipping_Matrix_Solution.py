class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        def row_flip(grid, row_no):
            for i in range(0, len(grid[0])):
                if grid[row_no][i] == 0:
                    grid[row_no][i]=1
                else:
                    grid[row_no][i]=0
            return grid
        
        def col_sum(grid, col_no):
            summ = 0
            for i in range(0, len(grid)):
                summ += grid[i][col_no]
            return summ
        
        no_of_rows = len(grid)
        half_of_no_of_rows = no_of_rows//2
        no_of_columns = len(grid[0])
        score = 0

        for i in range(0, no_of_rows):
            if grid[i][0] == 0:
                grid = row_flip(grid, i)
            score += 2**(no_of_columns-1)

        for j in range(1, len(grid[0])):
            temp_sum = col_sum(grid, j)
            if temp_sum <= half_of_no_of_rows:
                score += (2**(no_of_columns-j-1))*(no_of_rows-temp_sum)
            else:
                score += (2**(no_of_columns-j-1))*temp_sum
        return score
