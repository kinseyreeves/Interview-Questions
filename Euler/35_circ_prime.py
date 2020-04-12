import copy
import collections

n = 20
all_vals = [x for x in range(1,n)]

for i in range(1,len(all_vals)-1):
    if all_vals[i] != -1:
        for j in range(i+all_vals[i], n-1, all_vals[i]):
            all_vals[j] = -1
        #print(all_vals)

primes = set([x for x in all_vals if x > 0])

def rotations(num):
    out = []
    a = collections.deque(list(str(num)))
    for i in range(len(a)):
        out.append([int(''.join(x)) for x in list(copy.copy(a))])
        a.rotate()
    return out

    

print(rotations(1234))
    