def sum_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2

    return sum


def square_sum(n):
    return sum(range(1, n + 1)) ** 2


print(square_sum(100) - sum_squares(100))
