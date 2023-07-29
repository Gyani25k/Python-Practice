
class Solution:
    def majorityWins(self, arr, n, x, y):
        count_x=0
        count_y=0
        for num in arr:
            if num==x:
                count_x+=1
            elif num==y:
                count_y+=1
        if count_x>count_y:
            return x
        elif count_x<count_y:
            return y
        else:
            return min(x,y)