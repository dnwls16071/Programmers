from collections import deque

def solution(queue1, queue2):
    # 연산 횟수 : 300,000 × 300,000 = 9,000,000,000(90억)의 횟수를 돌리면 시간초과가 발생함
    # 모든 경우를 다 확인하지않고 만약 제한 길이를 넘어서게 된다면 -1을 리턴하는 방법을 생각해내야함
    limit = len(queue1) * 3                     # 큐의 길이 제한
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)                    # 큐1의 합계
    sum_queue2 = sum(queue2)                    # 큐2의 합계
    
    while sum_queue1 != sum_queue2:
        # 하나의 큐라도 비어있는 경우가 발생하면? → 두 큐의 합을 같게 만들 수 없음
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        # 큐의 합을 기준으로 만약 첫 번째 큐가 값이 더 크다면?
        if sum_queue1 > sum_queue2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum_queue1 -= temp
            sum_queue2 += temp
            answer += 1
        # 큐의 합을 기준으로 만약 두 번째 큐가 값이 더 크다면?
        elif sum_queue1 < sum_queue2:
            temp = queue2.popleft()
            queue1.append(temp)
            sum_queue2 -= temp
            sum_queue1 += temp
            answer += 1
        # 계속되는 무한루프를 방지하고자 연산 횟수의 제한을 둠
        if answer == limit:
            return -1
    return answer