class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

      # Remember you can check if set value is int something
      seen = set()
      for num in nums:
        if(num in seen):
            return True
        else:
            seen.add(num)
      return False


    
