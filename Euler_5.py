'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10
    without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20?
'''

def HCF(a, b):
    if b == 0:
        return a
    return HCF(b, a%b)


def LCM(a, b):
    return (a*b) // HCF(a, b)


lcm = 1
for n in range(1, 20):
    lcm = LCM(lcm, n+1)

print("Smallest number divisible by first 20 natural numbers = %d" %lcm)
