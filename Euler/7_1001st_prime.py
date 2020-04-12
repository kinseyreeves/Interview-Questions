def is_prime(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return False
    
    return True

print(is_prime(7930))

i = 2
primes = []
while True:
    if(is_prime(i)):
        primes.append(i)

    if(len(primes)%1000==0):
        print(i)

    if(len(primes)==10001):
        print(i)
        break
    i+=1


