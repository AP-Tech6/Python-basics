l = list(map(int, input().split()))
k = int(input())

if l:
    k %= len(l)
    l = l[-k:] + l[:-k]

print(l)


///from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        if nums:
            k %= len(nums)
            nums[:] = nums[-k:] + nums[:-k]





