class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # We set the low and high
        low = 0

        # So essentially two numbers times for 2D
        m = len(matrix)
        n = len(matrix[0])
        high = (m * n) - 1

        # Find the mid point
        while low <= high:

            # Find the mid point
            mid = (low + high) // 2

            # Setup what we are searching
            row = mid // n
            col = mid % n

            value = matrix[row][col]
            
            # Now we setup the four cases that is left for the binary search
            if(value == target):
                return True
            elif(value < target):
                low = mid + 1
            elif(value > target):
                high = mid - 1
            
        return False
   
        
        