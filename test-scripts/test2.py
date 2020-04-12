def max_printable_documents(documents, is_malfunctioning, x):
    total = 0
    sim_total = 0
    temp_total = 0
    for i in range(0,len(documents)):
        if(not is_malfunctioning[i]):
            total+=documents[i]
    print(total)
    
    for i in range(0,len(is_malfunctioning)-x):

        temp_total=total+get_sim_addons(i,x,documents,is_malfunctioning)
        if(temp_total > sim_total):
            sim_total = temp_total

    return sim_total

def get_sim_addons(i,x, documents, is_mal):
    print("here")
    print(documents[i:i+x])
    total = 0
    for j in range(i, i+x):
        if(is_mal[j]):
            total+=documents[j]
    print(total)
    return total
            


print(max_printable_documents([5,0,1,3,1,6,2], [0, 1, 1, 0, 0,1,0], 2))