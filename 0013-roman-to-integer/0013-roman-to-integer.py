class Solution:
    def romanToInt(self, s: str) -> int:
        # If number after current is greater in value, combine and perform subtraction
        res = 0
        values = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        index = 0
        if len(s) == 1:
            return values[s[0]]
        while index < (len(s) - 1):
            curVal = values[s[index]]
            nextVal = values[s[index + 1]]
            if curVal >= nextVal:
                res += curVal
                index += 1
            elif nextVal > curVal:
                res += (nextVal - curVal)
                index += 2
            if (index == (len(s) - 1)) and (values[s[index]] <= values[s[index - 1]]):
                res += values[s[index]]
            
        return res


        
            
            
            


