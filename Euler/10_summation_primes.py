def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if (n % i == 0):
            return False

    return True


total = 0

for i in range(0, 2000000):
    if (is_prime(i)):
        total += i

print(total)
