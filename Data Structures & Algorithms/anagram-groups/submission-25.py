class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given an arry of strings strs, group all anagrams together into sublists
        # I can return the output in any order
        # I am going to create a hashmap key: the list of individual letters and the value is the list f
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
            
        return list(res.values())