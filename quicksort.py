"""
Quicksort implementation
"""

a = [12, 3, 2, 4, 4, 22, 34]


def quicksort(lst):
    if (len(lst) == 0):
        return []
    if (len(lst) == 1):
        return lst
    # print(lst)
    piv = lst[0]
    rest = lst[1:]
    lst1 = [x for x in rest if x > piv]
    lst2 = [x for x in rest if x <= piv]
    return quicksort(lst1) + [piv] + quicksort(lst2)


print(quicksort(a))
