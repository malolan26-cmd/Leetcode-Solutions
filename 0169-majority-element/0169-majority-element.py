class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elem_counts = {}

        for num in nums:
            if num in elem_counts:
                elem_counts[num] += 1
            else:
                elem_counts[num] = 1
        
        for key, value in elem_counts.items():
            if elem_counts[key] > (len(nums) // 2):
                return key