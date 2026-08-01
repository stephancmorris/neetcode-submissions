class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_seen = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap_seen:
                return [hashmap_seen[complement], i]
            hashmap_seen[n] = i
        return [] 
