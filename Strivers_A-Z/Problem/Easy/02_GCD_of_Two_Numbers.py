N, M = map(int, input().split())
gcd = 1
for i in range(1,min(N,M)+1):
    if N%i==0 and M%i==0:
        gcd = i

print(gcd)