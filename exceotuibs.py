def square(value):
    try:
        x = int(value)
        return x*x
    except TypeError:
        print("Please only enter integers please")



print(square("abc"))
