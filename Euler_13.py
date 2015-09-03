# Work out the first ten digits of the sum of the one-hundred 50-digit numbers (in Euler_13.txt).

sum = 0
fin = open("Euler_13.txt")
for i in range(100):
    sum += int(fin.readline())
sum = str(sum)

print("First 10 digits of the sum of the numbers = %s" %sum[:10])