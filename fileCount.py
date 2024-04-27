count = 0
inputFile = open("myfile.txt",'r')
for line in inputFile:
    words = line.split()
    for word in words:
        if len(word) == 4:
            count+=1
print("Count is:",count)
  