class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

      seen = set()
      for num in nums:
        # Check Condition
        if(num in seen):
          return num
        # Add after
        seen.add(num)
        

      


        