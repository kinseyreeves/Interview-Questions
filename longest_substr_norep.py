#longest substring without repeating characters

def get_substr(stri):
    all_subs = []
    for i in range(0,len(stri)):
        for j in range(i+1, len(stri)):
            all_subs.append(stri[i:j])
    
    largest = ''
    largest_len = 0
    for substr in all_subs:
        if(no_rep(substr) and len(substr) > largest_len):
            largest_len = len(substr)
            largest = substr

    return largest

def no_rep(stri):
    a = list(stri)
    if(len(set(a)) == len(stri)):
        return True
    return False

print(get_substr("hellomyname"))