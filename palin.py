class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True




 #remove atmost character to make palindrome

 class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                skip_left=s[i+1:j+1]
                skip_right=s[i:j]
                if skip_left==skip_left[::-1] or skip_right==skip_right[::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1
        return True                
               