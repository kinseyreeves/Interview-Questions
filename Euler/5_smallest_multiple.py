def divis_by(n, max):
    for i in range(1, max + 1):
        if (n % i != 0):
            return False

    return True


for i in range(1, 1000000000):
    if (divis_by(i, 20)):
        print(i)
        break
