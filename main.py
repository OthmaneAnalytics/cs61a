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

def main():
    print(largest_factor(15))
    print(largest_factor(80))
    print(largest_factor(13))
    print(two_of_three(5, 5, 5))

main()
