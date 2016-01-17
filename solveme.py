#L1 is a list of consecutive integers from 1 to n
#represents the people in the circle

def circRemove(L1, x):
    if len(L1) == 1:
    	return L1[0]
    L1[x:len(L1):2] = [0]*len(range(x,len(L1),2))
    if L1[-1] == 0:
    	L1 = list(filter(None, L1))
    	return circRemove(L1,1)
    if L1[-1] != 0:
    	L1 = list(filter(None, L1))
    	return circRemove(L1,0)

#General function: 1+2*n-2**(ceil(log2(n)) where n is the number of people in the circle
#This formula gives the position of the final person left in the circle
#Example with n = 11:
#1 + 2*(11) - 2**(ceil(log2(11)) = 1 + 22 - 2**4 = 7
#the 7th person in the circle will be the last one remaining
    
