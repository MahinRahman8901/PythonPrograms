import Calculator
print("\n##############################")
print("THIS IS A VIRTUAL CALCULATOR")
print("CHOOSE ONE OF THE FOLLOWING")
print("##############################\n")

print(" - Addition")
print(" - Subtraction")
print(" - Division")
print(" - Multiplication")
print(" - Cubed")
print(" - CubeRoot\n")


userinput = input("Please select an option")
answer = userinput.lower()

if answer == "addition":
    num1 = int(input("Enter First digit"))
    num2 = int(input("Enter Second digit"))
    Calculator.addition(num1, num2)

elif answer == "subtraction":
    num1 = int(input("Enter First digit"))
    num2 = int(input("Enter Second digit"))
    Calculator.subtraction(num1, num2)

