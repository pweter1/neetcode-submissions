class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            countS[char_s] = 1 + countS.get(char_s, 0)
            countT[char_t] = 1 + countT.get(char_t, 0)
        for c in countS:
             if countS[c] != countT.get(c, 0):
                return False
        return True