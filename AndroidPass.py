from itertools import combinations,permutations

L1 = list(combinations([1,2,3,4,5,6,7,8,9],4))
L2 = []

for x in range(len(L1)):
    L3 = list(permutations(L1[x]))
    L2 = L2 + L3

def valid_check(L2):
    c = 0
    for x in range(len(L2)-1):
        if L2[x] == 1:
            if 2 in L2[:x] and L2[x+1] == 3:
                c = c + 1
            elif 4 in L2[:x] and L2[x+1] == 7:
                c = c + 1
            elif 5 in L2[:x] and L2[x+1] == 9:
                c = c + 1
            elif L2[x+1] != 3 and L2[x+1] != 7 and L2[x+1] != 9:
                c = c + 1
        if L2[x] == 2:
            if 5 in L2[:x]:
                c = c + 1
            elif L2[x+1] != 8:
                c = c + 1
        if L2[x] == 3:
            if 2 in L2[:x] and L2[x+1] == 1:
                c = c + 1
            elif 5 in L2[:x] and L2[x+1] == 7:
                c = c + 1
            elif 6 in L2[:x] and L2[x+1] == 9:
                c = c + 1
            elif L2[x+1] != 1 and L2[x+1] != 7 and L2[x+1] != 9:
                c = c + 1
        if L2[x] == 4:
            if 5 in L2[:x]:
                c = c + 1
            elif L2[x+1] != 6:
                c = c + 1
        if L2[x] == 5:
            c = c + 1
        if L2[x] == 6:
            if 5 in L2[:x]:
                c = c + 1
            elif L2[x+1] != 4:
                c = c + 1
        if L2[x] == 7:
            if 5 in L2[:x] and L2[x+1] == 3:
                c = c + 1
            elif 4 in L2[:x] and L2[x+1] == 1:
                c = c + 1
            elif 8 in L2[:x] and L2[x+1] == 9:
                c = c + 1
            elif L2[x+1] != 3 and L2[x+1] != 1 and L2[x+1] != 9:
                c = c + 1
        if L2[x] == 8:
            if 5 in L2[:x]:
                c = c + 1
            elif L2[x+1] != 2:
                c = c + 1
        if L2[x] == 9:
            if 6 in L2[:x] and L2[x+1] == 3:
                c = c + 1
            elif 8 in L2[:x] and L2[x+1] == 7:
                c = c + 1
            elif 5 in L2[:x] and L2[x+1] == 1:
                c = c + 1
            elif L2[x+1] != 3 and L2[x+1] != 7 and L2[x+1] != 1:
                c = c + 1
    if c == 3:
        return True
    return False

for y in range(len(L2)):
    if valid_check(L2[y]) == False:
        L2[y] = 0

L2 = list(filter(None,L2))

print(len(L2))

#1624 for 4
#7152 for 5
#26016 for 6
#72912 for 7
#140704 for 8
#140704 for 9

#389112 total possible passwords for a 3by3 grid android lock screen
