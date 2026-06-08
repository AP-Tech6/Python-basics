class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0
        l = 0
        p = 1
        r=0
        count = 0
        while(r<len(nums)):
            p = p * nums[r]
            while p >= k:
                p = p // nums[l]
                l += 1
            count += (r - l + 1)
            r+=1
        return count