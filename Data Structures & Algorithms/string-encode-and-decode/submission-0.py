class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if not strs:
            return ""
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        if not s:
            return []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j]) # we should be at the number but its a string
            # i = j + 1 - starting indx
            # j = i + length - ending indx
            res.append(s[j + 1 : j + 1 + length]) #gives us the entire string 
            i = j + 1 + length

        return res

        
