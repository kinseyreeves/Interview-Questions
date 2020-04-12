def facs(num):
    out=[]
    for i in range(int(num/2),0,-1):
        if(num%i==0):
            out.append(i)
    return out+[num]


def prime_facs(num):
    factors = facs(num)
    prime_factors = []
    for i in factors:
        if(len(facs(i))==2):
            prime_factors.append(i)


    return prime_factors

print(prime_facs(13195))

