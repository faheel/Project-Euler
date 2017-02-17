'''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
    the 6th prime is 13.

    What is the 10001st prime number?
'''

from math import sqrt

def is_prime(num):
    i = 2
    while i <= sqrt(num):
        if num%i == 0 and num != i:
            return False
        i += 1
    return True


n = 0
i = 1
while n < 10001:
    i += 1
    if is_prime(i):
        n += 1

print("10001st prime = %d" %i)
