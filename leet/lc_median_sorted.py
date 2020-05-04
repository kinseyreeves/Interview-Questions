"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

"""


def arr_merge(a, b):
    out = []

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if (a[i] < b[j]):
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    if i < len(a):
        out += a[i:]
    elif j < len(b):
        out += b[j:]
    return out


def get_med(arr):
    if (len(arr) % 2 == 0):
        val = (arr[int(len(arr) / 2) - 1] + arr[int(len(arr) / 2)]) / 2
    else:
        val = arr[int(len(arr) / 2)]

    return val


print(get_med([1, 2, 3, 4, 5]))
print(arr_merge([1], [1, 5, 9, 10, 11]))
