n_rows = int(input("Enter the number of rows:"))


for i in range(0, n_rows + 1, -1):
    for j in range(i, 0, -1):
        print("The Output:\n", j)
