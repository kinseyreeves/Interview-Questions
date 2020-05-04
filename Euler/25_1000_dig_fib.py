count = 0
curr = 0
next1 = 1
total = 0

while True:
    count += 1
    next2 = next1 + curr
    curr = next1
    next1 = next2

    if (len(str(curr)) == 1000):
        print(curr)
        exit(0)
