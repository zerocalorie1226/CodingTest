def solution (n, k):
    answer=[]
    sumK=k
    listN=[]
    value=0
    for num in range(0,n):
        listN.append(num + 1)
        
    while listN:
        if(sumK>len(listN)):
            sumK -= len(listN)
        else:              
            value=listN[sumK-1]
            answer.append(value)
            listN.pop(sumK-1)
            sumK=sumK+k-1


    return answer

n, k = map(int, input().split())
print("<" + ", ".join(map(str,solution(n, k))) + ">")

