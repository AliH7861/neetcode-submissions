class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

       # Count frequency of every element
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Get the frequencys
        freq = [[] for _ in range(len(nums) + 1)]
        for num,c in count.items():
            freq[c].append(num)


        # Get the result values
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if(len(result) == k):
                    return result 




       

        
        