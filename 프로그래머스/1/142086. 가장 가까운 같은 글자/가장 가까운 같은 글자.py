def solution(s):
    answer = [-1]  # 첫 번째 문자는 비교 대상 없음

    for i in range(1, len(s)):  # 두 번째 문자부터 탐색
        found = False  # 같은 문자 찾았는지 여부 체크
        for j in range(1, i + 1):  # i-1, i-2, ... 순서로 왼쪽 문자 탐색
            if s[i] == s[i - j]:
                answer.append(j)  # 가장 가까운 문자 거리 저장
                found = True
                break  # 가장 가까운 문자 찾았으면 반복 종료
        if not found:
            answer.append(-1)  # 같은 문자 없으면 -1 추가

    return answer
