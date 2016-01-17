from sys import exit
from time import time

stime = time()

L1 = [
    [7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
    [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
    [34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]
]
# 993 max


"""L1 = [
[  7,  53, 183, 439, 863],
[497, 383, 563,  79, 973],
[287,  63, 343, 169, 583],
[627, 343, 773, 959, 943],
[767, 473, 103, 699, 303]
]"""

# 973 max

# L1 = [[90,75,75,80],[35,85,55,65],[125,95,90,105],[45,110,95,115]]

LStore = [] #need to access this after completion to actually find sum

for x in range(len(L1)):
    LStore.append(list(L1[x]))

#below code makes it so that you find the max matrix sum instead of min
    
for x in range(len(L1)):
    for y in range(len(L1)):
        L1[x][y] = 993 - L1[x][y]

LLines = []

for x in L1:
    LLines.append([8] * len(L1))


def printMat(L1):
    """Prints the matrix so that it is somewhat readable."""
    for x in L1:
        for y in x:
            print(str(y) + (6 - len(str(y))) * ' ', end='')
        print()
        print()
    print("""

    """)


def starZeroes(L1):
    """Cycles through L1 and stars zeroes and then makes sure any other zeroes in that row and column are unstarred."""
    for x in range(len(L1)):
        for y in range(len(L1)):
            if L1[x][y] == 0:
                if L1[x].count("0*") == 0:
                    LVert = [L1[k][y] for k in range(len(L1))]
                    if LVert.count("0*") == 0:
                        L1[x][y] = "0*" #if no other starred zeroes in a zeroes row & column then that 0 is starred


def coverStarZeroes(L1, LLines):
    """If a column contains 0* in L1, the corresponding column in LLines is covered in lines."""
    end = 0
    for x in range(len(L1)):
        LVert = [L1[k][x] for k in range(len(L1))]
        if "0*" in LVert:
            end += 1
            for m in range(len(L1)):
                LLines[m][x] = "|" #vertical lines
    if end == len(L1): #we're finished when L1 is completely covered
        printMat(L1)
        print("We're done boys.")
        print()
        total = 0
        for x in range(len(L1)):#compute sum using coords of 0* in L1 and the values in LStore
            for y in range(len(L1)):
                if L1[x][y] == "0*":
                    total += LStore[x][y]
        print(total)
        print()
        print(time() - stime) #actually pretty fast, i'll take O(n^3) over O(n!)
        exit() #need to do this because all this recursion ends with a really complicated stack


def primeZeroes(L1, LLines):
    """Zeroes that are not being covered are primed for coverage."""
    printMat(L1) #just to keep track of whats happening.
    printMat(LLines)
    for x in range(len(L1)):
        for y in range(len(L1)):
            if L1[x][y] == 0 and LLines[x][y] == 8:
                L1[x][y] = "0'"
                if L1[x].count("0*") == 0:#if no starred zeroes in a primed zeroes row we go to swapStars
                    swapStars(L1, LLines, x, y)
                else:
                    m = L1[x].index("0*") #otherwise we horizontally cover the starred zero and primed zero
                    for k in range(len(L1)):#and remove the veritcal covering on the starred zero
                        if LLines[k][m] == "|": #need to make sure we don't uncover anything cover by another horizontal line
                            LLines[k][m] = 8
                    LLines[x] = ["-"] * len(L1)
    LValues = []
    for x in range(len(L1)):#for finding the minimum uncovered value
        for y in range(len(L1)):
            if LLines[x][y] == 8:
                LValues.append(L1[x][y])
    addSubValues(L1, LLines, min(LValues))


def addSubValues(L1, LLines, n):
    """Adds n to all covered rows, subtracts n from all uncovered columns."""
    for x in range(len(L1)):
        if (LLines[x].count("|") + LLines[x].count("-")) == len(L1): #finding covered rows
            for y in range(len(L1)):
                if L1[x][y] != "0*" and L1[x][y] != "0'": #0* and 0' should be unchanged after all is done
                    L1[x][y] += n #if we get a str+int error then something serious is going wrong
    for x in range(len(L1)):
        LVert = [LLines[k][x] for k in range(len(L1))]
        if (LVert.count("|") + LVert.count("-")) != len(L1): #finding uncovered columns
            for p in range(len(L1)):
                if L1[p][x] != "0*" and L1[p][x] != "0'":
                    L1[p][x] -= n
    primeZeroes(L1, LLines) #return to priming zeroes as there will now be new exposed zeroes


def reset(L1, LLines):
    """Reset LLines and clear 0'."""
    for x in range(len(L1)): #changes all remaining 0' to 0
        for y in range(len(L1)):
            if L1[x][y] == "0'":
                L1[x][y] = 0
    LLines = []
    for x in L1: #reset LLines to all 8s
        LLines.append([8] * len(L1))
    coverStarZeroes(L1, LLines)
    primeZeroes(L1, LLines)


def swapStars(L1, LLines, x, y):
    """I'm actually still confused about what this actually does in the grand scheme of things."""
    LZs = [[x, y]] #initialize LZs with coords of the primed zero with no starred zero in its row
    n = True
    k = 1 #in order to alternate between finding 0* in column to 0' in row
    while n: 
        if k == 1:
            LVert = [L1[k][LZs[-1][1]] for k in range(len(L1))]
            if LVert.count("0*") > 0:
                LZs.append([LVert.index("0*"), LZs[-1][1]])
                k = k * -1
            else:
                n = False #while loop terminates when no 0* found in column of 0'
        if k == -1:
            if L1[LZs[-1][0]].count("0'") > 0:
                LZs.append([LZs[-1][0], L1[LZs[-1][0]].index("0'")])
                k *= -1
            else:
                print("Something fucked up.") #there should always be a 0' in a row of 0*
    for m in range(len(LZs)): #changing 0* found in LZs to 0
        if L1[LZs[m][0]][LZs[m][1]] == "0*":
            L1[LZs[m][0]][LZs[m][1]] = 0
    for m in range(len(LZs)): #changing 0' found in LZs to 0*
        if L1[LZs[m][0]][LZs[m][1]] == "0'":
            L1[LZs[m][0]][LZs[m][1]] = "0*"
    reset(L1, LLines)

printMat(L1)

for x in range(len(L1)): #initial row reduction to generate zeroes
    n = min(L1[x])
    for y in range(len(L1)):
        L1[x][y] -= n

printMat(L1)
starZeroes(L1)
coverStarZeroes(L1, LLines)
printMat(L1)
printMat(LLines)
primeZeroes(L1, LLines)
