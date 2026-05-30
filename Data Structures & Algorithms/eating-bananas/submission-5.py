class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        def hoursNeeded(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours

        while low < high:
            mid = (low + high) // 2

            if hoursNeeded(mid) <= h:
                high = mid      # speed works, try smaller
            else:
                low = mid + 1   # speed too slow

        return low
