class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {} 

        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i
            else:
                return True
        return False
        