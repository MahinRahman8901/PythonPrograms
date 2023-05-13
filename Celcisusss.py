with open("temp_in_F.txt","r") as temp:
    lines = [line.rstrip() for line in temp]

with open("temp.txt", "w") as new:
    for i in range(0, len(lines)):
        x = (int(lines[i]) - 32) * (5/9)
        new.write(str(x)+"\n")
