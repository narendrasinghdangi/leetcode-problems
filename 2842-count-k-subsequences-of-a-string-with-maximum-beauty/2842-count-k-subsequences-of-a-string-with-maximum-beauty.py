class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        freq = collections.Counter(s)    
        unique = len(freq)
                
        max_beauty = sum(cnt for cnt in sorted(freq.values())[unique - k:])
            
        res = 0
        for comb in itertools.combinations(freq.keys(), k):
            if sum(freq[char] for char in comb) == max_beauty:
                curr = 1 
                for char in comb:
                    curr *= freq[char]

                res += curr
        
        return res % MOD