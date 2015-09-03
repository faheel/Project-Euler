# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

n1 = 999
n2 = 999
largest = 10000
while n1 > 100:
	n = n1 * n2
	if n > largest and str(n) == str(n)[::-1]:
		largest = n
	n2 -= 1
	if n2 == 100:
		n2 = 999
		n1 -= 1

print("Largest palindrome number, which is the product of two 3-digit numbers = %d" %largest)