reader = open("test.txt", "r")
count = 0
for row in reader:
    count += 1
print("There are ", count, "lines in the text file")