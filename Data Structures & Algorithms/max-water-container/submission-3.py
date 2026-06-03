class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maxi = 0

        while left < right:
            
            ans = min(heights[left], heights[right]) * (right - left)

            if heights[left] < heights[right]:
                left +=1
            else:
                right-=1
            
            
    
            
            if ans > maxi:
                maxi = ans
        
        return maxi