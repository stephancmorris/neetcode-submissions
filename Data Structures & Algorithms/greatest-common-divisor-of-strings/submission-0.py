class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #measures and stores the lengths of both input strings 
        #we will need these numbers to test whether these can divide evenly
        len1, len2 = len(str1), len(str2)

        #the helper function that takes an int aj t; 
        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            factor1, factor2 = len1 // l, len2 // l
            return str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2


        #For loop staring at the number and going down
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""