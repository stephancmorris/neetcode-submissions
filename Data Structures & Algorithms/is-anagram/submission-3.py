class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {} 

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        return s_count == t_count


        # loop through s and t in parrallel, compare each letter at a time 
        # Store the letters in a hashmap 
        # Return true by the end if there are no differences in counts

