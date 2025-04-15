def solution(n):
    listN = list(str(n))  # n을 문자열로 변환한 후 리스트로 변환
    listN.reverse()  # 리스트를 역순으로 변경

    # 각 문자를 정수로 변환하여 새로운 리스트로 반환
    return [int(x) for x in listN]


