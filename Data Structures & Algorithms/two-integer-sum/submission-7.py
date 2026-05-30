class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Output = []
        n = len(nums)
        for i in range(0, n):

            firstNum = nums[i]
            secondNum = target - firstNum

            if(secondNum in nums):
                if(firstNum == secondNum):
                    if(nums.count(firstNum) < 2):
                        continue
                    else:
                        first = nums.index(firstNum)
                        second = nums.index(secondNum, first + 1)
                        Output.append(first)
                        Output.append(second)
                        break
                        
                first = nums.index(firstNum)
                second = nums.index(secondNum)
                Output.append(first)
                Output.append(second)

                break

        return Output
