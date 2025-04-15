def solution(a, b):
    result1=str(a)+str(b)
    result2=str(b)+str(a)
    result1Int=int(result1)
    result2Int=int(result2)
    answer=''
    if(result1Int>result2Int):
        answer=result1
    else:
        answer=result2
    return int(answer)