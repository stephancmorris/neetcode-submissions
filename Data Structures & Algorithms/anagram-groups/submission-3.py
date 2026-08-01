class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charcount to list of anagrams
        for s in strs: # loop through str with s being each string
            count = [0] * 26 # set to 26 char
            for c in s:
                count[ord(c) - ord('a')] += 1 # a - a = 0, map a to 0
            res[tuple(count)].append(s)

        return list(res.values())


# take in an array of strings
# Grouping anagrams together -> sublists 
# Return this output in any order

# Questions - Just letters, all lower case, 
# should the output be in lower case
# 

#Brute force - compare each string to its self
#Can I sort the problem? m(length) * nlogn(sort) but can it be better

# m * n * 26 is possible using a count of each char 0-26
# m = total number of input strings, n = avergage len of str * 26
# Hashmap is used with pattern(char) as key : Value = list of anagrams




