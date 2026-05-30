class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

       
        while low <= high:

            mid = (low + high) // 2

            #1) Target is found
            if nums[mid] == target:
                return mid
            
            # 2) If left side is orted
            if(nums[low] <= nums[mid]):
                if(nums[low] <= target < nums[mid]):
                    high = mid -1
                else:
                    low = mid + 1
            
            #3) When right side is sorted
            else:
                if(nums[mid] < target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
         

 

        