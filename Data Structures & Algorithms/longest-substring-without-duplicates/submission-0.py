class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(len(s)): #Left Window
            non_repeating = set()
            for j in range(i, len(s)): #Right Window
                if s[j] in non_repeating:
                    break
                non_repeating.add(s[j])
            result = max(result, len(non_repeating))
        return result
