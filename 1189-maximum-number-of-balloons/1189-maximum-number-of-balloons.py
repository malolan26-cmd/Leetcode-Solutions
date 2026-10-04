class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_counts = defaultdict(int)
        balloon = 'balloon'
        for c in text:
            if c in balloon:
                letter_counts[c] += 1
        
        if any(c not in letter_counts for c in balloon):
            return 0
        else: 
            return min(letter_counts['b'], letter_counts['a'], letter_counts['l'] // 2, letter_counts['o'] // 2, letter_counts['n'])

            
        