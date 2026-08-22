class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0 , 0

        for el in nums:
            if count == 0:
                res = el
            
            count += (1 if el == res else -1)
        
        return res