import math

def solution(n):
    num = math.sqrt(n)
    print(num)
    if (num.is_integer()):
        return (num+1)**2
    else:
        return -1
