#!/usr/bin/env python
import math

"""
Some useful facts:
1. 1 is not a prime.
2. All primes except 2 are odd.
3. All primes greater than 3 can be written in the form 6k+/-1.
4. Any number n can have only one primefactor greater than sqrt(n).
5. The consequence for primality testing of a number n is: 
       if we cannot find a number f less than or equal sqrt(n) that divides n 
       then n is prime: the only primefactor of n is n itself.
"""
def isPrime(n):
    if n <= 1:
        return False
    elif n < 4: # 2 and 3
        return True
    elif n % 2 == 0:
        return False
    elif n < 9: # 5 and 7 
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True

def g(a, b, n):
    return n*n + a*n + b

def f(a, b):
    n = 0
    while isPrime(g(a, b, n)):
        n += 1
    return n

def main():
    maxLen = 0
    for a in range(-999, 1000):
        for b in range(2, 1000):
            length = f(a, b)
            if length > maxLen:
                maxLen = length
                c, d = a, b
    print c * d
    
if __name__ == '__main__':
    main()
