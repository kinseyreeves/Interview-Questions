maxnum = 0
for i in range(100, 1000):

    for j in range(100, 1000):
        num = i * j
        if num > maxnum and str(num) == str(num)[::-1]:
            maxnum = num

print(maxnum)
