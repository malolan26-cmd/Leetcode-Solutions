from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)
        for num in nums: 
            counts[num] += 1

        while len(res) < k:
            maxKey = len(nums) + 1
            maxVal = -10**4 + 1
            for key, val in counts.items():
                if val >= maxVal and key not in res:
                    maxVal = val
                    maxKey = key
                
        
            res.append(maxKey)

        return res


            
