def display(x):
    if x == 0:  # Base condition
        return
    x -= 1
    print("Name")
    display(x)  # Recursion - Calling itself

display(5)