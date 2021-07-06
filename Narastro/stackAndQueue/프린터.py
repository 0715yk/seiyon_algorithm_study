# 2021.07.06. 2021 Stack/Queue(Programmers High score kit) 
# 프린터

import collections
def solution(priorities, location):
    answer = 1
    prior_deq = collections.deque(priorities)
    max_prior = max(prior_deq)
    find = False

    while not find:
        for i in  range(location+1):
            v = prior_deq.popleft()
            # 1. 인쇄
            if max_prior == v:
                # 정답을 찾은 경우
                if i == location:
                    find = True
                    break
                answer += 1
                max_prior = max(prior_deq)
            # 2. 대기
            else:
                prior_deq.append(v)
        # 위치 초기화
        location = len(prior_deq)-1
    return answer


