n = int(input("enter an odd no.:"))

for i in range(n): 
	for j in range(2 * n - 1):
		if (j == n - 1 - i or j == n -1 + i ) and i < n // 2 + 1 :
			print("*", end="")
		elif(j == n - 1 - (n - 1 - i) or j == n - 1 + (n - 1 - i)) and i  > n // 2:
			print("*", end="")
		else:
		 	print(" ", end="")
	print()