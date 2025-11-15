import math

N = int(input())
if N == 0:
    print(1)
else:
    print(int(math.log10(N)+1))

# ------- Another way -------- #

count = 0
if N == 0:
    print(1)
else:
    while N > 0:
        count += 1
        N //= 10
    print(count)