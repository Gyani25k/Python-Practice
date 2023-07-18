# Given the first 2 terms A and B of a Geometric Series. 
# The task is to find the Nth term of the series.

class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        #Your code here
        common_ratio=B/A
        gp_term = A*(common_ratio)**(N-1)
        return gp_term
    
    