class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)-1
        if n==0:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return n
        low=0
        high=n
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid+1]<nums[mid]:
                return mid
            elif nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1    

        """
        Peak Element Conditions with Examples
A peak element means:

nums[i] > nums[i-1]
and
nums[i] > nums[i+1]
Condition 1
nums[mid] > nums[mid-1]
and
nums[mid] > nums[mid+1]
✅ Mid itself is peak.

Example:

nums = [1,2,5,3,1]
Suppose:

mid = 2
nums[mid] = 5
Check:

5 > 2
5 > 3
So:

return mid
Peak index:

2
Condition 2
nums[mid] < nums[mid+1]
✅ Peak exists on right side.

Example:

nums = [1,2,3,4,5]
Suppose:

mid = 2
nums[mid] = 3
nums[mid+1] = 4
Since:

3 < 4
array is increasing.

Peak must be towards right.

So:

low = mid + 1
Move right.

Condition 3
nums[mid] > nums[mid+1]
✅ Peak exists on left side (including mid).

Example:

nums = [9,7,5,3,1]
Suppose:

mid = 2
nums[mid] = 5
nums[mid+1] = 3
Since:

5 > 3
array is decreasing.

Peak exists on left side.

So:

high = mid - 1
Move left.
"""