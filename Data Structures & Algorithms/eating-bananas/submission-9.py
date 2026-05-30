from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # The condition within the problem, is how many bananas has to be eaten
        # A user cannot use another pile, if one pile is occured

        # Setting up the min and max
        low = 1
        high = max(piles)
        
        # Defines how many hours are neeed


        # Design a Function that determines how many hours we need based on speed
        def HoursNeeded(speed):
            totalHours = 0
            for pile in piles:
                hour = ceil(pile / speed)
                totalHours += hour
            return totalHours
        
        # Setting up the while loop
        while low <= high:
            
            mid = (low + high) // 2
            
            # Case 1: TotalHour is less than hour
            if HoursNeeded(mid) <= h:
                # If Hours are less than time given then you reduce the speed
                high = mid - 1
            
            # Case 2: TotalHour is more than hour
            else:
                # If TotalHour is more than total hour, then you increase speed
                low = mid + 1

        # Case 3:
        return low