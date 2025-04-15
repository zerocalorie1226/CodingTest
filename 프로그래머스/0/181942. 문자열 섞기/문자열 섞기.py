def solution(str1, str2):
    a=list(str1)
    b=list(str2)
    n=0
    answer=''
    while(n<len(a)):
        answer=answer+a[n]+b[n]
        n+=1
    return answer