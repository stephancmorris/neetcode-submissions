class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k is the number of values, not index we will be outputting
        #Only numbers will be in the array 

        #Sort Nums 
        # from the back, traverse the array, and for each k add distint num

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # creates the empty array / bucket

        for num in nums:
            count[num] = 1 + count.get(num,0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
            
        