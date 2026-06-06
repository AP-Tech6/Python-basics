class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fivecount=0
        tencount=0
        for coin in bills:
            if coin==5:
                fivecount=fivecount+1
            elif coin==10:
                if(fivecount>0):
                    fivecount=fivecount-1
                    tencount=tencount+1
                else:
                    return False
            else:
                if fivecount>0 and tencount>0:
                    fivecount=fivecount-1
                    tencount=tencount-1 
                elif fivecount>=3:
                    fivecount=fivecount-3
                else:
                    return False 
        return True                   

        