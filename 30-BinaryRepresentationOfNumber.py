'''
TO PRINT BINARY REPRESENTATION OF A NUMBER
'''

def binary(n):
    if n==0:
        return 
    binary(n//2)
    print(n%2)

result=binary(13)
print(result)