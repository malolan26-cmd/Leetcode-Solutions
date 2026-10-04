class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_consec = 0

        nums = set(nums)

        for num in nums:
            cur_num = num
            length = 1
            if num - 1 in nums:
                continue
            
            while cur_num + 1 in nums:

                length +=1
                cur_num += 1

            max_consec = max(max_consec, length) 


        return max_consec