n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, 2 * n + 1):
        if j <= i or j > 2 * n - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n + 1):
        if j <= i or j > 2 * n - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
