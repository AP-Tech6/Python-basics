#sliding window cpncept add 3 numbers  then result-inital value+ next value
books=list(map(int,input().split()))
k=3
n=len(books)
s=sum(books[:k])
m=s
for i in range(1,n-k+1):
    s=s-books[i-1]+books[i+k-1]
    m=max(m,s)
print(m)    



#avg 643
#note subarrya,subsequence => sliding window problems

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        s = sum(nums[:k])
        m = s
        for i in range(1, n-k+1):
             s = s - nums[i-1] + nums[i+k-1]
             m = max(m, s)
        return m / k