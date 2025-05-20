n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for i in range(b):
        input()  # 입력은 버려도 됨
    print(a - 1)
