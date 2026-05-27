def addition(n):
    if n == 1:
        return 1
    return n + addition(n-1)
print(addition(int(input())))