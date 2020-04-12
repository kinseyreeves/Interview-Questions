import math

def is_triplet(a,b,c):
    if(a+b+c==1000):
        return True
    return False

for a in range(0,500):
    for b in range(0,500):
        c = math.sqrt(a**2 + b**2)
        if(is_triplet(a,b,c)):
            print("found a, b, c")
            print(str(a) + " " + str(b) + " " + str(c))

