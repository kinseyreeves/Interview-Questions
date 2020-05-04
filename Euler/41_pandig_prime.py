def is_prime(k):
    n = k + 1
    all_vals = [x for x in range(1, n)]

    for i in range(1, len(all_vals) - 1):
        if all_vals[i] != -1:
            for j in range(i + all_vals[i], n - 1, all_vals[i]):
                all_vals[j] = -1
            # print(all_vals)

    primes = set([x for x in all_vals if x > 0])
    print(primes)
    if k in primes:
        return True
    return False


def is_pan(n, num):
    digs_set = set([int(x) for x in list(str(num))])
    all_digs = list(str(num))
    if (len(digs_set) > n) or (max(digs_set) != n) or len(digs_set) != len(all_digs):
        return False
    return True


def is_pan_prime()


print(is_pan(4, 12345))
