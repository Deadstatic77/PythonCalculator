O = int(input("Enter first number: "))
T = int(input("Enter second number: "))
W = input("\nAddition = add\nSubtraction = sub\nMultiplication = mult\nDivision = div\n")


def subtraction():
    print(O - T)


def addition():
    print(O + T)


def multiplication():
    print(O * T)


def division():
    print(O / T)


if W == "sub":
    subtraction()
elif W == "add":
    addition()
elif W == "mult":
    multiplication()
elif W == "div":
    division()
