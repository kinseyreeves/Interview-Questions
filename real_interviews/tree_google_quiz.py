
"""
Find the amount of equal subtrees in a list/tree structure.
Leaf nodes considered equal subtrees
"""

t_in = [[1], [1,2],[1,2,3,4]]

subtree = []
def get_subtree(tree, idx, depth, t):

    if(depth == len(tree)-1):
        return [tree[depth][idx]]
    else:
        t = t + [tree[depth][idx]] + get_subtree(tree, idx*2, depth+1, t) + get_subtree(tree, idx*2+1, depth+1, t)
    return t

def all_same(lst):
    return all(x==lst[0] for x in lst)

count = 0
for d in range(0,len(t_in)):
    for t in range(0,len(t_in[d])):

        subtree = get_subtree(t_in, t, d, [])
        if(all_same(subtree)):
            count+=1

print(count)

