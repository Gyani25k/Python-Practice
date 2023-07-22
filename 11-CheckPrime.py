# A prime number is a number which is only divisible by 1 and itself.
# Given number N check if it is prime or not.

# Method 1 

def CheckPrime1(n):
    for i in range(2,n):
        if i%n == 0:
            return False
    return True 

# Example : For n=37 we have to run loop for 36 times 

# Time Complexity is O(N)

# Method 2 

def CheckPrime2(n):
    if n==1:
        return False
    i=2
    while (i*i<=n):
        if n%i==0:
            return False
        i=i+1
    return True

# Example : For n=37 we have to run loop for 6 times (Squaring Method) 

# Time Complexity is O(N^1/2)


# Method 3 (Super Efficient Method)

def CheckPrime3(n):
    
    if n==1:
        return False
    
    if n==2 or n==3:
        return True
    
    if n%2==0 or n%3==0:
        return False
    
    i = 5

    while (i*i<=n):

        if n%i==0 or n%(i+2)==0:
            return False
        
        i += 6
    return True


