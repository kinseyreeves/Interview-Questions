l_tris = []
l_pents = []
l_hexs = []

for n in range(0,100000):
    l_tris.append(int((n*(n+1))/2))
    l_pents.append(int((n*(3*n-1))/2))
    l_hexs.append(int(n*(2*n-1)))

s_tris = set(l_tris)
s_pents = set(l_pents)
s_hexs = set(l_hexs)


out = []
for i in range(0,len(l_tris)):
    if l_tris[i] in s_hexs and l_tris[i] in s_pents:
        out.append((i,l_tris[i]))

print(out)
