import csv

filename = "goldmedals.csv"
with open(filename, newline="") as file:
    read = csv.reader(file, delimiter=",")
    line = read.__next__()
    #print(line)
    new = []
    for row in file:
        #print(row)
        x = row.split(",")
        #print(x)
        new.append(x[0]+" , "+x[15].strip("\n"))
    print(new[59])
