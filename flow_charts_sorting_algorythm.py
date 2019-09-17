def main():
    numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    print(numbers)
    iteration = 1
    n = len(numbers)

    while iteration < n:
        j = 0
        while j <= n - 2:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
                j = j + 1
            else:
                j = j + 1

        iteration = iteration + 1
    print(numbers)


if __name__ == "__main__":
    main()
