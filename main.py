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

def main():
    print(a_plus_abs_b(2, 3))
    print(a_plus_abs_b(2, -3))
    print(a_plus_abs_b(-1, 4))
    print(a_plus_abs_b(-1, -4))

main()
