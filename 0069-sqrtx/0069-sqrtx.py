class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x
        index = -1
        while left <= right:
            mid = (left+right) // 2

            if mid > x // mid:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
            
        if index == -1:
            return x
        
        return index - 1
        

        