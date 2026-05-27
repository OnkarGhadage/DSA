def fibonacci(n: int)-> None:
    first, second = 0, 1
    for i in range(n+1):
        print(first, end=" ")
        first, second = second, first+second
    return

def fibonacci_no(n: int)-> int:
    first, second = 0, 1
    for i in range(n):
        first, second = second, first+second
    return first


fibonacci(5)
print()
print(fibonacci_no(5))