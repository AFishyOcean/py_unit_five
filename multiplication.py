def multiplication_table(number):
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the multiplication table of the parameter number.
    """
    tot = ""
    for x in range(12):
        tot +=str(6 * x + 6)+" "
    return tot
def main():
    number = int(input("What number would you like multiples of?"))
    print(multiplication_table(number))

main()