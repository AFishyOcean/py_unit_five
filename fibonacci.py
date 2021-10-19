def fibonacci(x):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    c = ""
    a = 0
    b = 1
    for x in range(x):
        c +=str (a + b)+ ""
        a = b
        b = c
    return c
def main():
    x = int(input("How many terms would you like?"))
    fibonacci(x)
    print(fibonaci(x))

main()