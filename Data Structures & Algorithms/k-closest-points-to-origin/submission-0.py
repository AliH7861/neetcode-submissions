import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Heap = []
        # We output an array of k points

        # So the heap will be min to max
        # We will use a for loop because we will check every element in the points
        for x,y in points:
            dist = x*x + y*y
            heapq.heappush(Heap, (dist, [x,y]))
        
        # only give k results
        result = []
        for i in range(k):
            result.append(heapq.heappop(Heap)[1])
        
        # reutrn
        return result
        