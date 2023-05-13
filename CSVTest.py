import csv

filename = "goldmedals.csv"
with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #line = csvreader.__next__()
    #print(line)
    rows = list(csvreader)
    print(rows[58])

