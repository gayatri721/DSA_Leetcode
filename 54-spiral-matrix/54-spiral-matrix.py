# https://www.youtube.com/watch?v=1ZGJzvkcLsA&ab_channel=TECHDOSE
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        m, n = len(matrix), len(matrix[0])
        i, first_row, first_col = 0, 0, 0
        last_row, last_col = m - 1, n - 1
        spiral_order = []
        # until a boundary overlaps
        while first_row <= last_row and first_col <= last_col:
            #left 
            for i in range(first_row, last_col + 1): 
                spiral_order.append(matrix[first_row][i])
            first_row += 1
            #down
            for i in range(first_row, last_row + 1): 
                spiral_order.append(matrix[i][last_col])
            last_col -= 1
            # right
            if first_row <= last_row:
                i = last_col
                while i >= first_col:
                    spiral_order.append(matrix[last_row][i])
                    i -= 1
                last_row -= 1
             # up
            if first_col <= last_col:
                i = last_row 
                while i >= first_row:
                    spiral_order.append(matrix[i][first_col])
                    i -= 1 
                first_col += 1
        
        return spiral_order