from collections import deque

dq = deque([1,2,3,4,5,6,7,8,9])

# print(dq)
# print(*dq)
# print(list(dq))

dq.append(10)
print(list(dq))

dq.appendleft(0)
print(list(dq))

print(dq.pop())
print(dq.popleft())

print(list(dq))