# You are given two numbers A and B. 
# When A is raised to some power P, we get a number X. 
# Now, you need to find what is the value of X that is closest to B.

def nearestPower(A, B):
    closest = None
    min_difference = B
    P = 0
    while True:
        X = A ** P
        difference = abs(X - B)
        if difference < min_difference:
            closest = X
            min_difference = difference
        else:
            break
        P += 1

    return closest