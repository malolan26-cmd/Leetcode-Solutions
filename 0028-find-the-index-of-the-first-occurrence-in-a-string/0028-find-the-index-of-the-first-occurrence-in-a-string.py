class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        matching_count = 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                for j in range(len(needle)):
                    if needle[j] == haystack[i + j]:
                        matching_count += 1
                    if matching_count == len(needle):
                        return i
                matching_count = 0
        
        