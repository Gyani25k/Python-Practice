
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