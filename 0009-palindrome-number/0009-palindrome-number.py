class Solution:
    def isPalindrome(self, x: int) -> bool:
        numAsString = str(x)
        
        reverseString = numAsString[::-1]
        
        if numAsString == reverseString:
            return True

        return False