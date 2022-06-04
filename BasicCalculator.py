def main():
    O = int(input("Enter first number: "))
    T = int(input("Enter second number: "))
    W = input("\nAddition = add\nSubtraction = sub\nMultiplication = mult\nDivision = div\n")

    def subtraction():
        print(O - T, "\n")

    def addition():
        print(O + T, "\n")

    def multiplication():
        print(O * T, "\n")

    def division():
        print(O / T, "\n")

    if W == "sub":
        subtraction()
        main()
    elif W == "add":
        addition()
        main()
    elif W == "mult":
        multiplication()
        main()
    elif W == "div":
        division()
        main()


main()
