from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for num in nums:
            result.add(num)
        if len(nums) != len(result):
            return True
        return False
                

        


