def display(n, x):
    if n == x+1:
        return
    print(n)
    # n += 1
    display(n+1,x) # Directly writtenparameter of updated n so "n += 1" is not needed

display(1,10)
# display(1,int(input()))