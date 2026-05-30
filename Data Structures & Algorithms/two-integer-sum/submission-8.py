class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Which of the two values equal target

       # Current value minus target and if its in set you append curent and that index
       
       seen = {}

       for i, num in enumerate(nums):
        # Now what you do is current num value subtract with target
        curTarget = target - num
        

        if curTarget in seen:
            return [seen[curTarget], i]
        
        seen[num] = i

       
        