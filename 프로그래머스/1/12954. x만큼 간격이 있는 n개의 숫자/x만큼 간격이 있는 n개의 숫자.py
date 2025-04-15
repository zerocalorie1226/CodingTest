def solution(x, n):
    answer = []
    num=0
    for i in range(1,n+1):
        num+=x
        answer.append(num)
    return answer