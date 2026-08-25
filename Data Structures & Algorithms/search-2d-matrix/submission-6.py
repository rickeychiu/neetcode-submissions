class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # obtaining the correct row
        x = 0
        y = len(matrix) - 1
        correctRow = -1

        while x <= y:
            mid = (x + y) // 2
            # if target < first val of row, search rows above
            if target < matrix[mid][0]:
                y = mid - 1
            # if target > last val of row, search rows below
            elif target > matrix[mid][-1]:
                x = mid + 1
            else:
                correctRow = mid
                break

        if correctRow < 0:
            return False


        # now search through the row
        i = 0
        j = len(matrix[correctRow]) - 1

        while i <= j:
            mid = (i + j) // 2
            if matrix[correctRow][mid] == target:
                return True
            elif matrix[correctRow][mid] < target: # too small
                i = mid + 1
            elif matrix[correctRow][mid] > target: # too big
                j = mid - 1
        
        return False