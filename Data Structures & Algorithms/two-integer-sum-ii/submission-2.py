class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            # There are conditions
            
             # 3 - 1 < 4
             while target - numbers[left] > numbers[right]:
                left+=1

             while target - numbers[left] < numbers[right]:
                right-=1
            
             if target - numbers[left] == numbers[right]:
                return [left + 1, right + 1]

                
            
    