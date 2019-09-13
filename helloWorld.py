import sys


def main():
    # print a welcomming message in a terminal, according to existance argument
    if len(sys.argv) == 1:
        print("Hello World!")
    elif len(sys.argv) == 2:
        print(f"Hello, dear {sys.argv[1]}!")
    else:
        print("Given too many arguments!")


if __name__ == "__main__":
    main()
