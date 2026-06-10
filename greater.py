class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        stack=[]
        for curr in nums2:
            while stack and stack[-1]<curr:
                ele=stack.pop()
                d[ele]=curr
            stack.append(curr)
        while stack:
            d[stack.pop()]=-1

        res=[]
        for i in nums1:
            res.append(d[i])
        return res

"""
This is the Monotonic Stack solution for Next Greater Element.

Idea
For every number in nums2, store its next greater element in a dictionary.

Example:

nums2 = [1,3,4,2]
We want:

1 -> 3
3 -> 4
4 -> -1
2 -> -1
Store in:

d = {
    1: 3,
    3: 4,
    4: -1,
    2: -1
}
Then for nums1, simply look up answers from the dictionary.

Dry Run
nums2 = [1,3,4,2]
Start:

stack = []
d = {}
curr = 1
stack = []
Push:

stack = [1]
curr = 3
Check:

stack[-1] < curr

1 < 3
Pop:

ele = 1
So:

d[1] = 3
Dictionary:

{1:3}
Push current:

stack = [3]
curr = 4
Check:

3 < 4
Pop:

ele = 3
Store:

d[3] = 4
Dictionary:

{1:3, 3:4}
Push:

stack = [4]
curr = 2
Check:

4 < 2
False.

Push:

stack = [4,2]
End of Loop
Elements left in stack have no greater element on the right.

stack = [4,2]
Pop:

d[2] = -1
Pop:

d[4] = -1
Final dictionary:

{
    1: 3,
    3: 4,
    2: -1,
    4: -1
}
Build Result
nums1 = [4,1,2]
Look up:

d[4] = -1
d[1] = 3
d[2] = -1
Result:

[-1,3,-1]
Why does the while loop work?
while stack and stack[-1] < curr:
Suppose:

stack = [1,3]
curr = 4
Since 4 is greater than both:

1 -> next greater is 4
3 -> next greater is 4
So we pop them and store:

d[1] = 4
d[3] = 4
This is why the algorithm is O(n) instead of checking every pair (O(n²)).
"""