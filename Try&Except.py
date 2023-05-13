try:
    writer = open("test.txt","w")
finally:
    print("Time to close the file")
    writer.close()

print("Not reached if exception occurs")
