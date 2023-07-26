
#GFG METHOD

def checkPalindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        last_digit = temp % 10
        rev = rev * 10 + last_digit
        temp = temp // 10
    if rev == n:
        return True
    else:
        return False

result = checkPalindrome(7)
print(result)

#LEETCODE

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        rev = temp[::-1]
        return rev==temp