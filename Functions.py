from math import factorial
from math import floor
from fractions import gcd

def inverse(x): #turns a number the the other way around e.g. 379 --> 973
    L1 = [int(i) for i in str(x)]
    L1.reverse()
    return int(''.join(str(i) for i in L1))

def palincheck(x): #checks if a number is a palindrome
    L1 = [int(i) for i in str(x)]
    L1.reverse()
    n = int(''.join(str(i) for i in L1))
    if n == x:
        return True
    return False

def choose(n,r):
    return (factorial(n))/(factorial(r)*factorial(n-r))

def factors(n):#returns a list containing factors of n, e.g. 10 --> [1,2,5,10]
    L1 = []
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            if (i != n/i):
                L1.append(i)
                L1.append(n/i)
            else:
                L1.append(i)
    L1.sort()
    return L1

def amic_chain(x): #https://projecteuler.net/problem=95
    z = 1  
    L1 = [x,sum(factors(x))]
    while L1[0] != L1[len(L1)-1] and L1[len(L1)-1] != 0 and L1[len(L1)-1] < 1000000 and sum(factors(L1[len(L1)-1])) != L1[len(L1)-1] and sum(factors(L1[len(L1)-1])) not in L1:
        L1.append(sum(factors(L1[z])))
        z = z + 1
    if L1[0] == L1[len(L1)-1] or sum(factors(L1[len(L1)-1])) == L1[0]:
        return L1
    return []

def sieve(n):#sieve of erastothenes returns a list of primes less than n
    L1 = list(range(n+1))
    L1[1] = 0
    limit = int(round(n**0.5))
    for i in range(2, limit + 1): 
        if L1[i]:
            L1[i*i: n+1: i] = [0] * len(range(i*i, n+1, i))
    return list(filter(None,L1))

def diagonal_spiral(n): #https://projecteuler.net/problem=58
    x = n 
    L1 = []
    while x != 1:
        y = x
        n = 0
        while n != 4:
            L1.append(x)
            x = x - y**(1/2) + 1
            n = n + 1
    L1.append(1)
    return(L1)

def long_division(n):
    L1 = []
    x = 1
    while True:
        if [floor(x*10/n),x] in L1:
            break
        L1.append([floor(x*10/n),x])
        x = (x*10) % n
    return L1

def prime_factors(n): #returns a list of prime factors of n e.g. 20 --> [2,2,5]
	L1 = []
	d = 2
	while d*d <= n:
		while (n % d) == 0:
		    L1.append(d)  # supposing you want multiple factors repeated
		    n = n/d
		d = d + 1
	if n > 1:
	       L1.append(n)
	return L1

def lowest_terms(a,b): #puts a fraction into lowest terms
    while gcd(a,b) != 1:
        blah = gcd(a,b)
        a = a/blah
        b = b/blah
    return([a,b])

def miller_rabin(x): #miller rabin primality testing returns true or false depending on if the number is prime
    if x == 1 or x == 2 or x % 2 == 0:
        if x == 1:
            return False
        if x == 2:
            return True
        return False
    elif x < 2047:
        L1 = [2]
    elif x < 1373653:
        L1 = [2,3]
    elif x < 9080191:
        L1 = [31,73]
    elif x < 25326001:
        L1 = [2,3,5]
    elif x < 4759123141:
        L1 = [2,7,61]
    elif x < 1122004669633:
        L1 = [2,13,23,1662803]
    elif x < 2152302898747:
        L1 = [2,3,5,7,11]
    elif x < 3474749660383:
        L1 = [2,3,5,7,11,13]
    elif x < 341550071728321:
        L1 = [2,3,5,7,11,13,17]
    elif x < 3825123056546413051:
        L1 = [2,3,5,7,11,13,17,19,23]
    d = x-1
    s = 0
    while d % 2 != 1:
        d = d/2
        s = s + 1
    for a in L1:
        L2 = []
        for z in range(s):
            y = pow(a,int(2**z*d),x)
            L2.append(y)
            if y == x - 1 or L2[0] == 1:
                break
        if L2[0] != 1 and x-1 not in L2:
            return False
    return True

def fraction_count(a,b):
    #returns number of fractions > 1 whose numerator is a and denominator is <= b
    L1 = list(set(prime_factors(a)))
    L2 = [n for n in range(a+1,b+1)]
    for x in range(len(L1)):
        L2[int(L1[x])-1:len(L2):int(L1[x])] = [0] * len(range(int(L1[x])-1,len(L2),int(L1[x])))
    return(len(L2)-L2.count(0))
