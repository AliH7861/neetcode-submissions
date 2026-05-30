class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

      # So How do you do determine if number is duplicate
      seen = set()

      # How to append
      for num in nums:
        if num in seen:
          return True
        seen.add(num)
      return False
        
        

    
