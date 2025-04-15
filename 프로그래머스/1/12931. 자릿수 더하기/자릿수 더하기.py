def solution(n):
    listN=list(str(n))
    answer=0
    for i in range(0,len(listN)):
                   answer+=int(listN[i])
    return answer