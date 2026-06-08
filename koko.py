
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(n,piles,h):
            total=0
            for p in piles:
                total+=math.ceil(p/m)
            if total>h:
                return False
            else:
                return True
        l,h=1,max(piles)
        while l<=h:
            m=(l+h)//2
            if can_eat(m,piles,h):
                h=m-1
            else:
                k=m+1
        return 1                               
