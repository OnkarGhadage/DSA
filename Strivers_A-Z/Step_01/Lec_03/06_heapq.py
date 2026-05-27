import heapq    # Equivalent to priority queue

# Min heap - smallest ele on top (By default)
# Max heap - largest ele on top

List = [] # Normal list is heap. Just perform heapq operations on it

heapq.heappush(List,10)
heapq.heappush(List,20)
heapq.heappush(List,30)
heapq.heappush(List,40)
heapq.heappush(List,50)
heapq.heappush(List,5)
print(List)
print("Poped ele: ",heapq.heappop(List))
print(List)
print()

# Normal list to heap
Normal_List = [8,6,4,9,3,1,5,7]
heapq.heapify(Normal_List)
print(Normal_List)
print()

print(heapq.nsmallest(2,List))  # 2 smallest elements
print(heapq.nlargest(2,List))  # 2 largest elements
print()

# Make number of lists sorted
List1 = [1,8,4]
List2 = [2,7,5]
List3 = [3,9,6]
merged = heapq.merge(List1,List2,List3)
print(list(merged))
print()

# Priority queue example
task = [(2,"Task 2"),(4,"Task 4"),(3,"Task 3"),(1,"zTask 1"),(5,"Task 5")]
heapq.heapify(task)
print(task)
print(task[0])