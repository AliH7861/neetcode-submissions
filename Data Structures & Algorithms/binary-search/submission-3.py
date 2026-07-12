class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        

            # While target is not reached
        while low <= high:
            index = (low + high) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                high = index -1
            else:
                low = index + 1
                
        return -1
        
