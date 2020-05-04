'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
TERMINAL = 4000000
curr = 0
next1 = 1
total = 0
while True:
    next2 = next1 + curr
    curr = next1
    next1 = next2
    if (curr % 2 == 0):
        total += curr
    if (curr > TERMINAL):
        print(curr)
        break

print(total)
