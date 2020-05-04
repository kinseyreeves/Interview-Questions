def convert(string, numrows):
    arr = [[0 for x in range(0, len(string))] for y in range(0, numrows)]

    finished = False
    x = 0
    y = 0
    i = 0
    down = True
    while i < len(string):
        print(f"{x} {y}")
        arr[y][x] = string[i]
        if (y == numrows - 1):
            down = False
        if (y == 0):
            down = True

        if (down):
            y += 1
        else:
            x += 1
            y -= 1
        i += 1
    out = ''
    for row in arr:
        for item in row:
            if (item != 0):
                out += item
    return out


print(convert("paypalishiring", 3))
