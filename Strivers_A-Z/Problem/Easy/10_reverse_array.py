def rev_arr_0(n: list) -> list:
    for i in range(len(n)//2):
        n[i], n[-(i+1)] = n[-(i+1)], n[i]
    return n

def rev_arr_1(n: list, s: int, e: int) -> list:
    if s < e:
        n[s], n[e] = n[e], n[s]
        return rev_arr_1(n, s+1, e-1)

def rev_arr_2(n: list) -> list:
    n.reverse()
    return n


array0 = [1,2,3,4,5,6]
print(rev_arr_0(array0))

array1 = [1,2,3,4,5,6]
rev_arr_1(array1,0,len(array1)-1)
print(array1)

array2 = [1,2,3,4,5,6]
print(rev_arr_2(array2))

