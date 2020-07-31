"""
faster approach than checking str == str[::-1]
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        if len(str_x)==1:
            return True
        j = len(str_x)-1
        i = 0
        while i <= j:
            if(str_x[i]!=str_x[j]):
                return False
            i+=1
            j-=1
        return True


a = Solution()
print(a.isPalindrome(-12321))