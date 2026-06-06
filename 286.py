class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=len(nums)
        x1,x2=0,0
        for i in range(l*l):
            x1=x1^l
        for l in nums:
            x2=x2^l
        return x1^x2        