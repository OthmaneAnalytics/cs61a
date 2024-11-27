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
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return i**2 + j**2 + k**2 - max(i,j,k)**2 

def main():
    print(two_of_three(1, 2, 3))
    print(two_of_three(5, 3, 1))
    print(two_of_three(10, 2, 8))
    print(two_of_three(5, 5, 5))

main()
