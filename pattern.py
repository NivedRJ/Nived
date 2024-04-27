rows = int(input("Enter number of rows:"))
if rows > 26:
    print("rows shoould be below 26")
else:
    for i in range(rows):
        for j in range(i + 1):
            print(1 +j,end=" ")
        print()




