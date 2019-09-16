def calculation():
    divisible_list = []
    for i in range(100, 1000):
        if i%7 == 0:
            divisible_list.append(i)
        elif i%9 == 0:
            divisible_list.append(i)
        if len(divisible_list) >= 25:
            return divisible_list
