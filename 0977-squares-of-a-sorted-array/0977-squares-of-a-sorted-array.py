class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums = [i**2 for i in nums]
        res = []
        
        l, r = 0, len(nums) - 1

        while len(res) < len(nums):
            if nums[l] <= nums[r]:
                res.append(nums[r])
                r -= 1
            elif nums[l] > nums[r]:
                res.append(nums[l])
                l += 1

        return res[::-1]