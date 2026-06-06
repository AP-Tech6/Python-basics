l=list(map(int,input().split()))
m=0
for i in l:
    m=max(m,i)
print(m)    




class Solution:
    def canJump(self, nums: List[int]) -> bool:
        petrol=0
        for p in nums:
            if petrol<0:
                return False
            elif p>petrol:
                petrol=p
            petrol=petrol-1
        return True            
2,3,1,1,4
initally zero petrol when i reach first petrol pump, i take 2 petrol when i moved to next petrol pump
my current petrol is 1, when i move to next petrol pump i take 3 petrol but i have only 1 petrol so i can not move to next petrol pump so return false
