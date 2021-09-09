#  4  3  2 -1
#  3  2  1 -1
#  1  1 -1 -2
# -1 -1 -2 -3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Start searching for the first negative number from the right of the first row
        negatives = 0
        j = len(grid[0]) - 1
        i = 0

        while j >= 0 and i < len(grid):
            # If negative found, all nums below it will also be negative
            # Move to next row and one column to the left
            if grid[i][j] < 0:
                negatives += (len(grid) - i)
                j -= 1
            else:
                i += 1

        return negatives


