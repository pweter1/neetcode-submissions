class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #So nums is an array of integers 
        #given ingeter target too
        #I need to find the indicies i and j in the nums array so that the integers of the indicies in the array add up to the target
        #I may assume that every input has exactl one pair of indices i and j that satisfy the condition

        #I will go through the array and then check if 
        h_map = {}
        result = []
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in h_map:
                return [h_map[diff], idx]
            h_map[num] = idx