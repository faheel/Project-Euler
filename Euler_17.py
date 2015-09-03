# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

wordDict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
			10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen", 20: "twen", 30: "thir", 40: "for", 50: "fif",
			60: "six", 70: "seven", 80: "eigh", 90: "nine"}

def num_to_words(num):
	org = num
	power = 0
	while num // 10 ** power:
		power += 1
	group = 1000
	hundreds = 0
	tens = 0
	in_words = ""

	for i in range(power, 0, -1):
		digit = num // 10 ** (i - 1)

		if i % 3 == 0:
			hundreds = digit
			group = num // 10 ** (i - 3)
			prefix = ""
			if hundreds != 0:
				word = wordDict[digit]
				suffix = " hundred "
			else:
				prefix = ""
				word = ""
				suffix = ""

		elif (i + 1) % 3 == 0:
			tens = digit
			if hundreds == 0:
				prefix = ""
			elif tens == 0:
				prefix = ""
			else:
				prefix = "and "
			if tens == 0:
				word = ""
				suffix = ""
			elif tens == 1:
				couple = num // 10 ** (i - 2)
				if 10 <= couple <= 13 or couple == 15 or couple == 18:
					word = wordDict[couple]
					suffix = ""
				else:
					word = wordDict[couple % 10]
					suffix = "teen"
			else:
				word = wordDict[tens * 10]
				suffix = "ty"

		else:
			ones = digit
			if ones == 0:
				prefix = ""
				word = ""
				suffix = ""
			elif hundreds == 0 and tens == 0:
				prefix = ""
				if digit == 0:
					word = "zero"
				else:
					word = wordDict[ones]
				suffix = ""
			elif group == ones and org != ones:
				prefix = "and "
				if digit == 0:
					word = ""
				else:
					word = wordDict[ones]
				suffix = ""
			elif tens == 0 and hundreds != 0:
				prefix = "and "
				if digit == 0:
					word = ""
				else:
					word = wordDict[ones]
				suffix = ""
			elif tens != 1:
				prefix = "-"
				if digit == 0:
					prefix = ""
					word = ""
				else:
					word = wordDict[ones]
				suffix = ""
			else:
				prefix = ""
				word = ""
				suffix = ""

			if group != 0:
				if i + 2 == 3:
					suffix = ""
				elif i + 2 == 6:
					suffix = " thousand "

		in_words += prefix + word + suffix
		num %= 10 ** (i-1)

	return in_words


letters = 0
for num in range(1, 1001):
	word = num_to_words(num)
	for char in word:
		if char not in " -":
			letters += 1

print("Letters = %d" %letters)