def min_find(numbers):
    num_min = numbers[0]
    for num in numbers[1:]:
        if isinstance(num, list):
            for nest_num in num:
                if nest_num < num_min:
                    num_min = nest_num
        if isinstance(num, int):
            if num < num_min:
                num_min = num
    return num_min


def max_find(numbers):
    num_max = numbers[0]
    for num in numbers[1:]:
        if isinstance(num, list):
            for nest_num in num:
                if nest_num > num_max:
                    num_max = nest_num
        if isinstance(num, int):
            if num > num_max:
                num_max = num
    return num_max


def avg_find(numbers):
    avg = 0
    for num in numbers:
        if isinstance(num, list):
            for nest_num in num:
                avg += nest_num
        if isinstance(num, int):
            avg += num
    return avg / len(numbers)


def main():
    numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
    numbers_opt = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]
    print(min_find(numbers_opt))
    print(max_find(numbers_opt))
    print(avg_find(numbers_opt))


if __name__ == "__main__":
    main()
