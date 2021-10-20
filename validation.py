def get_input():
    """
    This function ensures that a user correctly enters in a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        x = int(input("Give a number between 1 and 10"))
        if x > 0 and x < 10:
            return x

def main():
    print(get_input())


if __name__ == '__main__':
    main()
