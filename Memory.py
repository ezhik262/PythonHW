def memorize(f):
    memo = {}

    def helper(*args, **kargs):
        k = tuple(args)
        if k not in memo:
            memo[k] = f(*args, **kargs)
        return memo[k]

    return helper


@memorize
def ladder(n, m=3):
    if n == 0:
        return 1
    elif n == 1 or n == -1:
        return 0
    else:
        return ladder(n - 2, 1) + ladder(n - 3, 1)


print(ladder(10, m=1))