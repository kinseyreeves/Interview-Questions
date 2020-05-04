out = []
nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

for i in range(1, 200):
    for j in range(1, 200):
        prod = i * j
        all_digs = str(i) + str(j) + str(prod)

        if len(all_digs) == 9 and set(all_digs) == nums:
            out.append([i, j, prod])

print(out)
print(len(out))
