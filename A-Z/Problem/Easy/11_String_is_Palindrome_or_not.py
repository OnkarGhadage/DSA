def ispal(s: str)-> bool:
    return True if s == s[::-1] else False

print(ispal("hannah"))