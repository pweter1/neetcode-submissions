class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {} # key: number  value: frequency

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # So now we have two hashmaps that have the key being the number and then the value being the frequency
        #We have to compare them now. if there's any difference, 
        if countS.items() == countT.items():
            return True
        return False