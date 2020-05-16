#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        # print(f'Current x-range: {x}')
        if n % x == 0:
            return False
    else:
        return True

def list_primes(scale = 10):
    print('Primes:', end=" ")
    for x in range(scale):
        if isprime(x):
            print(f'{x},', end=" ")
    print() # \n

list_primes(120)

""" n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime') """

