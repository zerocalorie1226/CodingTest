def solution(n, numbers):
    up = 1
    down = 1
    answer = 1  # 최소 1개는 항상 있음
    
    for i in range(1, n):
        if numbers[i] > numbers[i - 1]:
            up += 1
            down = 1  # 내림차순 리셋
        elif numbers[i] < numbers[i - 1]:
            down += 1
            up = 1  # 오름차순 리셋
        else:
            up += 1
            down += 1  # 같은 수는 두 경우 모두 연장 가능

        answer = max(answer, up, down)

    return answer

n = int(input())
numbers = list(map(int, input().split()))
print(solution(n, numbers))