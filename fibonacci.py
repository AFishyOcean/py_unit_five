def fibonacci(x):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    fib = ""
    c = 0
    a = 0
    b = 1
    for x in range(x):
        c = a + b
        a = b
        b = c
        fib +=str(c)+ " "
    return fib
def main():
    x = int(input("How many terms would you like?"))
    fibonacci(x)
    print(fibonacci(x))

main()