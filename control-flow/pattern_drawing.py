
size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for column in range(size):
        print(column, end="")
    print()  
    row += 1
