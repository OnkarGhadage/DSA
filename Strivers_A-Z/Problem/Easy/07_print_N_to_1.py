def display(x):
    if x == 0:
        return
    print(x)
    # x -= 1
    display(x-1)

display(10)
display(int(input()))