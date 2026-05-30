class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        # What am I trying to find here 
        # I am trying to find where the lowest number is 
        change = 0
        while low < high:
        
            # Finding the Medium Point
            mid = (low + high)  // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            

            else: 
                high = mid
                
        
        return nums[low]


            # if nums[low] >  num[high]
            # Move the low to mid + 1

            # if nums[low] < num[high]
            # Move the high to mid - 1
