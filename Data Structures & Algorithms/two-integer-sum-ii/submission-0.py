class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        result = []


        while left < right:
            currentSum = numbers[left] + numbers[right]

            if(currentSum == target):
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif(currentSum < target):
                left+=1
            else:
                right-=1

        