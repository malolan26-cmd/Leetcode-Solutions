class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        valid_letters = {}
        for c in magazine:
            if c in valid_letters:
                valid_letters[c] += 1
            else:
                valid_letters[c] = 1
            
        for c in ransomNote:
            if c not in valid_letters:
                return False
            elif valid_letters[c] == 1:
                del valid_letters[c]
            else:
                valid_letters[c] -= 1
            
        return True
        