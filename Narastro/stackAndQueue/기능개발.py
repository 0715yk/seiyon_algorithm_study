# 2021.07.06. 2021 - Stack/Queue(Programmers High score kit) 
# 기능 개발

import math
def solution(progresses, speeds):
    answer = []
    queue =[]
    
    for i in range(len(progresses)):
        # 완료까지 걸리는 시간
        take_time=math.ceil((100 - progresses[i])/speeds[i])
        # 첫 배포일
        if i==0:
            queue = [take_time]
            continue
        
        if queue[0] < take_time:
            answer.append(len(queue))
            queue=[take_time]
        else:
            queue.append(take_time)
    
    answer.append(len(queue))
    return answer