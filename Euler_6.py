'''
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
'''

sum_of_squares = 0
square_of_sums = 0
for n in range(1, 101):
    sum_of_squares += n**2
    square_of_sums += n
square_of_sums **= 2

diff = abs(square_of_sums - sum_of_squares)
print("Difference between the sum of squares and square of sums of first 100 natural numbers = %d" %diff)
