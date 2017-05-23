A1 = 0
A2 = 1
n = 15

def f(n, A1, A2):
    if n == 0:
        return A1
    else:
        return f(n-1,A2, A1+A2)

print f(n-1,A2, A1+A2)