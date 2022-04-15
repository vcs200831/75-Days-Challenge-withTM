class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cSum = 0
        pSums = {0 : 1}
        
        for n in nums:
            cSum +=n
            diff = cSum-k
            
            result += pSums.get(diff,0)
            pSums[cSum] = 1 + pSums.get(cSum,0)
        return result
            
            
            
            
        