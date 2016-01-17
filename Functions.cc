#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool myfunction(int i, int j){
    return (i < j);
}

/*def prime_factors(n):
 *      L1 = []
 *      d = 2
 *      while d*d <= n:
 *              while (n % d) == 0:
 *                  L1.append(d)  # supposing you want multiple factors repeated
 *                  n = n/d
 *              d = d + 1
 *      if n > 1:
 *             L1.append(n)
 *      return L1*/

vector<int> primeFactors(int n){
    vector<int> primes;
    int d = 2;
    while (d * d <= n) {
        while (n % d == 0) {
            primes.push_back(d); // if you want multiples
            n /= d;
        }
        d++;
    }
    if (n > 1) {
        primes.push_back(n);
    }
    sort(primes.begin(), primes.end(), myfunction);
    return primes;
}

/*def factors(n):
 *  L1 = []
 *  for i in range(1, int(n ** 0.5 + 1)):
 *      if n % i == 0:
 *          if (i != n/i):
 *              L1.append(i)
 *              L1.append(n/i)
 *          else:
 *              L1.append(i)
 *  L1.sort()
 *  return L1*/

vector<int> numFactors(int n){
    vector<int> factors;
    int limit = pow(n, 0.5) + 1;
    for (int i = 1; i < limit; i++) {
        if (n % i == 0) {
            if (i != n / i) {
                factors.push_back(i);
                factors.push_back(n / i);
            } else {
                factors.push_back(i);
            }
        }
    }
    sort(factors.begin(), factors.end(), myfunction);
    return factors;
}

/*def sieve(n):
    L1 = list(range(n+1))
    L1[1] = 0
    limit = int(round(n**0.5))
    for i in range(2, limit + 1):
        if L1[i]:
            L1[i*i: n+1: i] = [0] * len(range(i*i, n+1, i))
    return list(filter(None,L1))*/

vector<int> sieve(int n){
    vector<int> primes;
    vector<int> zeroesFiltered;
    for(int i = 0; i < n+1; i++){
        primes.push_back(i);
    }
    primes.at(1) = 0;
    int limit = pow(n,0.5)+1;
    for(int i = 2; i < limit+1; i++){
        if(primes.at(i) != 0){
            for(int p = i*i; p < n+1; p += i){
                 primes.at(p) = 0;
            }
        }
    }
    for(int i = 0; i < n+1; i++){
        if(primes.at(i) != 0){
            zeroesFiltered.push_back(primes.at(i));
        }
    }
    return zeroesFiltered;
}

int main(int argc, char * argv[]){
    vector<int> primes = sieve(10);
    for (unsigned int i = 0; i < primes.size(); i++) {
        cout << primes.at(i) << " ";
    }
    cout << primes.size();
    return 0;
}
