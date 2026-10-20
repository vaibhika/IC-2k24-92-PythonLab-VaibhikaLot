
matrix = []

# Input the matrix
print("Enter 9 elements:")
for i in range(3):
    row = []
    for j in range(3):
        num = int(input())
        row.append(num)
    matrix.append(row)

# Display the matrix
print("\nMatrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# Sum of all elements
total = 0
for i in range(3):
    for j in range(3):
        total = total + matrix[i][j]
print("Sum of all elements:", total)

# Sum of main diagonal elements
diagonal = 0
for i in range(3):
    diagonal = diagonal + matrix[i][i]
print("Sum of main diagonal elements:", diagonal)

# Find largest and smallest elements
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)

# Display the transpose
print("Transpose of the matrix:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
