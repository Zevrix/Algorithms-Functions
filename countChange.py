#finds the number of ways of creating an amount using a list of denominations and a corresponding list with quantities
#of the denominations
#e.g countChange(5,[1,2,5],[2,2,2]) == 2 because we have 2 coins of 5, 2 coins of 2, and 2 coins of 1 and are trying to 
#form 5
#the only two options available are (5) and (2,2,1); (1,1,1,1,1) and (2,1,1,1) will not work because of the lack of 1s

def countChange(amount, denominations, quantities):
    if len(denominations) == 0:
        if amount == 0: #a valid way of forming change exists
            return 1
        return 0 #a valid way of forming change does not exist
    if quantities[0] == 0: #removes denominations left with 0 quantity
        return countChange(amount, denominations[1:], quantities[1:])
    quantities[0] = quantities[0] - 1
    return countChange(amount, denominations[1:], quantities[1:]) + countChange(amount - denominations[0], denominations, quantities)

#works by breaking down the problem into smaller trivial problems
#cC(5,[1,2,5],[2,2,2]) is the same as cC(5,[2,5],[2,2]) + cC(4,[1,2,5],[1,2,2])
#continual breaking down reaches a point where there are 0 denominations left and if at that point the amount == 0
#a way of forming exact change from that branch exists, otherwise if amount still remains then there is change left
#over which cannot be made and 0 is returned

#I have not included the code but it is worth reducing quantities of coins larger than the amount to their max size
#for the sake of speed
#e.g. cC(5,[1,2,3,4,5],[100,100,100,100,100]) is the same as cC(5,[1,2,3,4,5],[5,2,1,1,1]) but the latter is much faster
#with this method
