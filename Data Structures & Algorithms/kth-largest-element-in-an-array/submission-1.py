import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # First you sort the element from largest to smallest

        # Create Reverse and then return
        nums = [-n for n in nums]
        heapq.heapify(nums)


        # Because only the first element is sorted we need to heap it invidualy:
        for i in range(k):
            value = heapq.heappop(nums)
        
        return -value

     



        
        