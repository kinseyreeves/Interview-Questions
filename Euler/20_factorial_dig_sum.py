def fac(n):
    sum = 1
    for i in range(n, 0, -1):
        sum *= i
    return sum


total = fac(100)

s = 0
for i in str(total):
    s += (int(i))

print(s)
