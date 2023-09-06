
class Solution:
    
    def isAnagram(self,a,b):
        a = sorted(a)
        b = sorted(b)
        if a == b:
            return True
        else:
            return False