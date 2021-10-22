def average():
    t = 0
    tot = 0
    while True:
        x = (input("Enter a number (q to stop)"))
        if x == "q":
            return float(tot) / t
        else:
            t = 1 + t
            tot = int(x) + tot




def main():
    print(average())

if __name__ == '__main__':
    main()
