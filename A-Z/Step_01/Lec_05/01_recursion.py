# print no

def display(n,x):
    if n == x:   # Base condition
        return
    print(n)
    n += 1
    display(n,x)  # Recursion - Calling itself

display(0,int(input()))