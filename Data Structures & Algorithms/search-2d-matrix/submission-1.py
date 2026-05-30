class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # We set the low and high
        low = 0

        # So essentially two numbers times for 2D

        # Repersents the number of rows
        m = len(matrix)
        
        # Repersents the number of cols 
        n = len(matrix[0])

        # Gettin the max amount of indexs
        high = (m * n) - 1

        # While Loop to ensure, that low is low and high is high
        while low <= high: 

            # Always divides data in half to see where data stands
            mid = (low + high) // 2

            # Setup what we are searching

            # How many full rows we have
            row = mid // n
            # How many columns are left
            col = mid % n

            # Value
            value = matrix[row][col]
            
            # Now we setup the four cases that is left for the binary search
            if(value == target):
                return True
            elif(value < target):
                low = mid + 1
            elif(value > target):
                high = mid - 1
            
        return False
   
        
        