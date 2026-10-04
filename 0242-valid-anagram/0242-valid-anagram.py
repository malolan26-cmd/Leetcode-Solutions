class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_s = {}
        for c in s:
            if c in letters_in_s:
                letters_in_s[c] += 1
            else:
                letters_in_s[c] = 1
        
        letters_in_t = {}
        for c in t:
            if c in letters_in_t:
                letters_in_t[c] += 1
            else:
                letters_in_t[c] = 1

        return letters_in_s == letters_in_t