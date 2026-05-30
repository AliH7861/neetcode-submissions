class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:

            # indexes of both i
            width = right - left
            height = min(heights[left], heights[right])

            Area = width * height

            if(Area > maxArea):
                maxArea = Area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return maxArea



        