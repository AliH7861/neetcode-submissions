class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create empty set
        setNum = set()

        for i in nums:  
            if i in setNum:
                return True
            else:
                setNum.add(i)
        
        return False


        