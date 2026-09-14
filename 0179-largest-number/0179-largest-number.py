class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Conver to list of strings
        nums = [str(num) for num in nums]

        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int(''.join(nums)))
        

        