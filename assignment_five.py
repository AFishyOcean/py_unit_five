# David Jones
# 10/22/2021
# Is a guessing game where the computer generates a number between 1 and 100 then the user has to guess it.
import random
def get_number():
    """
    Generates a random number between 0 and 101, then returns it.
    :return:
    """
    x = random.randint(1, 100)
    return x

def game_input(x):
    """
    Has a counter for the number of attempts
    asks for a guess on the number then responds accordingly
    :param x:
    :return:
    """
    t = 1
    while True:
        y = int(input("Guess a number between 1 and 100 that the computer selected. (Anything that is not a number between 1-100 to quit)"))
        if y == x:
            print("That is the number, good job. It took you", t, "times to guess the right number")
            break
        elif y > x:
            print("Try again, the number is smaller than", y)
        elif y < x:
            print("Try again, the number is larger than", y)
        else:
            print("That's not in the range or isn't a number. I'll stop here.")
            break
        t = 1 + t


def main():
    """
    calls all of the functions and assigns them values
    :return:
    """
    x = get_number()
    game_input(x)


if __name__ == '__main__':
    main()
