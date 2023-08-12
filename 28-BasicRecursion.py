'''
Learn about What is Recursion and its types.
Learn about base cases and how to implement it

'''

def basecases(n):
    if n<0:
        return "Negative Number"
    if n==0:
        return "Recursion End"
    print("GFG")
    basecases(n-1)

basecases(-3)