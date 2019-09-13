print("Fibonacci numbers calculator")


def users_range_input():
    # asking user for defining of Fibonacci numbers range
    converted = False

    while not converted:
        try:
            fib_length = int(input("Type a number\n"))
            converted = True
            return fib_length
        except ValueError:
            print("It's not a number")
            continue


def calculation(n):
    # Fibonacci numbers calculation
    a = 0
    b = 1
    list_of_fibonacci = []

    if n == 1:
        list_of_fibonacci.append(a)
    else:
        list_of_fibonacci.append(a)
        list_of_fibonacci.append(b)

        for x in range(2,n):
            c = a + b
            a = b
            b = c
            list_of_fibonacci.append(c)

    return list_of_fibonacci


def results_print(res):
    # Fibonacci numbers print
    print(res)


def main():
    results = calculation(users_range_input())
    results_print(results)


if __name__ == "__main__":
    main()
