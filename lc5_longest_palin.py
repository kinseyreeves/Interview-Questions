def is_palin(stra, strb):
    if(stra[::-1]==strb):
        return True
    return False

def longest_palin_substr(stra):
    
    for i in range(0,len(stra)):
        for j in range(i+1, len(stra)):
            substr = stra[i:j]
            