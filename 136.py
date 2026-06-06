class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x=x^i
        return x    


#in single number problem to remove duplicate elemnt do xor of the numbers
#then we will get the number which is not repeated