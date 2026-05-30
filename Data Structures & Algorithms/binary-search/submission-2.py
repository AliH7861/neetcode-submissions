class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # So get the high value
        high = len(nums) - 1
        low = 0
        
        # Remember in binary search everything is sorted
        # So everything can be divided into half

        while low <= high:
            # This is what is used to divide into half
            mid = (low + high) // 2

            # Case 1: Return mid value
            if(nums[mid] == target):
                return mid
            
            # Case 2: Now if target is less than mid
            elif(nums[mid] < target):
                low = mid + 1

            # Case 3: Now if target is more than mid
            elif(nums[mid] > target):
                high = mid - 1

        return -1
        