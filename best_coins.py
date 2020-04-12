denoms = [0.05,0.1,0.2,0.5,1,2]
value = 100



def get_sols(denoms, arr_size, val):
    

    if val == 0:
        return 1

    if val < 0:
        return 0

    if arr_size <=0 and val >=1:
        return 0
    
    return get_sols(denoms, arr_size-1, val) \
        + get_sols(denoms, arr_size, val-denoms[arr_size-1])


print(get_sols(denoms, len(denoms), value))