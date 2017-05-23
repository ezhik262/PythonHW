A1 = 1
A2 = 1

n = input("")

i = 2
while i < n:
    A_sum = A2 + A1
    A1 = A2
    A2 = A_sum
    i += 1

print (A_sum)