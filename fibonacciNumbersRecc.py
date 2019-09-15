# calculate a number of Fibonacci
def fib_num(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib_num(n-1) + fib_num(n-2)


# create and fill sequance with number of Fibonacci
def fib_seq(n):
    seq = []

    for i in range(1, n+1):
        seq.append(fib_num(i))
    
    return seq


# display in apropriate format f.sequance
def display(fib_seq):
    print("Fibonacci sequance:\n")

    for index, f_num in enumerate(fib_seq):
        print(f"{index+1}. {f_num}")


def main():
    display(fib_seq(10))


if __name__ == "__main__":
    main()
