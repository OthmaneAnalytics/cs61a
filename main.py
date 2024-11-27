"""
Homework 1:
"""
from operator import add, sub

def a_plus_abs_b(a,b):
    if b<0:
        f = sub
    else: 
        f = add
    return f(a,b)

def two_of_three(i, j, k):
   return i**2 + j**2 + k**2 - max(i,j,k)**2 


def largest_factor(n):
    for i in range(1,n):
        if n % i == 0:
            x = i
    return x

def hailstone(n):
    i = 1
    print(n)
    while n > 1:
        i += 1
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        print(n)
    return i

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    p = 1
    for i in range(1,n+1):
        p *= term(i)
    return p


def main():
    identity = lambda x : x
    square = lambda x : x**2
    triple = lambda x : x**3
    print(product(5, identity))
    print(product(3, square))
    print(product(3, triple))
main()
