# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def is_prime(num):
	i = 2
	while i <= sqrt(num):
		if num != i and num % i == 0:
			return False
		i += 1
	return True


n = 600851475143
LPF = 1
for i in range(2, n+1):
	if is_prime(i) and n % i == 0:
		LPF = i
		n = n / LPF
		if n < i:
			break
			
print("Largest prime factor of 600851475143 = %d" %LPF)