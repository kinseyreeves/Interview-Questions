coins = [0.01, 0.02, 0.05, 0.2, 0.5, 1, 2]

rev = reversed(coins)

print(coins)
print(rev)
all = []
def get_perms(idx, c_sum):
    if(idx < 0 or idx > len(coins)):
        return
    c_sum = c_sum + [] + [coins[idx]]
    #print(c_sum)
    #a = input()
    if(sum(c_sum) == 2.0):
        all.append(c_sum)
        return
    if(sum(c_sum) > 2):
        return
    

    get_perms(idx, c_sum)
    get_perms(idx+1, c_sum)
    get_perms(idx-1, c_sum)



get_perms(0, [])

print(len(all))


    
