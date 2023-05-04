
# run length encoding
def printRLE(st):

	n = len(st)
	i = 0
	while i < n- 1:

		# Count occurrences of
		# current character
		count = 1
		while (i < n - 1 and
			st[i] == st[i + 1]):
			count += 1
			i += 1
		i += 1

		# Print character and its count
		print(str(count) +
			st[i - 1],
			end = "")

# Driver code
if __name__ == "__main__":

	st = input("Enter the string to compute RLE: ")
	printRLE(st)
	print("")

