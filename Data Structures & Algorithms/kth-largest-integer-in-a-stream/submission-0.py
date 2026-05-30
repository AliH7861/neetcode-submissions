import heapq # This is to import a heap

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        # Getting the k value
        self.k = k
        self.heap = []

        for n in nums:
            # Pushing elements to the heap
            heapq.heappush(self.heap, n)

            # If the heap is getting bigger then k elmeent
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the value to nums
        heapq.heappush(self.heap, val)

        # Only allow k elements in the array
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the kth largest element
        return self.heap[0]
        
