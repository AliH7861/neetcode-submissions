import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Invert the values for the stone
        # Use for lop to invert it
        stones = [-s for s in stones]

        # Convert it into a heap
        heapq.heapify(stones)

        # So now we have the heap 
        while len(stones) > 1:
            # You pop the elements
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            # Then you invert them
            x = -x
            y = -y

            # Then you have a condition
            if x - y != 0:
                value = x - y
                value = -value
                heapq.heappush(stones, value)
         
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]




        
        