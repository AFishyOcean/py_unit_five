def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
    t = 1
    while number != 1:
        y = number % 2
        if y == 1:
            x = number * 3 + 1
            number = x
            t = 1 + t
        else:
            x = number / 2
            number = x
            t = 1 + t
    return t

def get_number():
    x = int(input("Please enter an integer:"))
    return x
def main():
    number = get_number()
    print(sequence(number))


if __name__ == '__main__':
    main()
