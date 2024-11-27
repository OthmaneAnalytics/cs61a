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

def main():
    a = hailstone(10)
    print(a)
    print(hailstone(1))

main()
