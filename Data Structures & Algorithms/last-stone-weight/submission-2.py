import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # So we need to convert the stones to a min heap

        # Turn this to negative for max-heap (cuz no min-heap)
        stones = [-s for s in stones]
        # Convert into heap
        heapq.heapify(stones)

        # While condition is used here (i forgo twhy?)
        while len(stones) > 1:
            # Pop
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            # Negate
            x = - x
            y = - y

            # Apply rule
            if x - y != 0:
                value = x - y
                value = - value
                heapq.heappush(stones, value)
            
        
        if not stones:
            return 0

        return -stones[0] 
            

        
        


            

    