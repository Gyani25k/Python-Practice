'''
You are given a number n. You need to see if the number is a palindrome or not (recursively)

Example 1:

Input:
n = 100
Output: 0

'''

def isPalidrome(N):
    n=str(N)
    if len(n)==0 or len(n)==1:
        return 1
    if n[0]==n[-1]:
        return isPalidrome(n[1:-1])
    else:
        return 0
    
result=isPalidrome(121)
print(result)