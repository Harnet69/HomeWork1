def main():
    a = int(input("Type the a"))
    b = int(input("Type the b"))

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    print(a)


if __name__ == "__main__":
    main()