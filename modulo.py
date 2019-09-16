# generate and find numbers divisible by 7 or 9 
def calculation():
    divisible_list = []
    for i in range(100, 1000):
        if i%7 == 0:
            divisible_list.append(i)
        elif i%9 == 0:
            divisible_list.append(i)
        if len(divisible_list) >= 25:
            return divisible_list


# display numbers divisible by 7 or 9
def display(divisible_list):
    for i in divisible_list:
        print(i)


def main():
    display(calculation())


if __name__ == "__main__":
    main()