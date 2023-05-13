writer = open("temp.txt", "w")
writer.write("Fruits: \n") #Write one line and create a new line
writer.writelines(["apples\n", "bananas\n", "mangoes\n", "Mahin"])
writer.close()