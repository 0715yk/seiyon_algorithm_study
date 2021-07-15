# 2021.07.07. 2021 Stack/Queue(Programmers High score kit) 
# 다리를 지나는 트럭

'''
<문제>
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	            []	                []	            [7,4,5,6]
1~2	            []	                [7]	            [4,5,6]
3	            [7]	                [4]	            [5,6]
4	            [7]	                [4,5]	        [6]
5	            [7,4]	            [5]	            [6]
6~7	            [7,4,5]	            [6]	            []
8	            [7,4,5,6]	        []	            []
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 
다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
'''

'''
<풀이>
다리길이만큼 0으로 채우고
매 초마다
최대 하중을 넘어가지 않는 경우 트럭의 무게를 큐에 푸쉬,
넘어가는 경우에는 0을 푸쉬하여
'''

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)       # 다리 길이만큼의 데크를 선언, 초기값 0으로 채워줌
    trucks = deque(truck_weights)                  # 트럭들의 무게도 데크로 선언(popleft의 성능 때문에)   
    time = 0    #현재 소요 시간
    csum = 0    #다리 위에 있는 트럭 무게의 합
    while trucks:   #트럭이 모두 출발할때까지 반복
        time += 1   
        passed = bridge.popleft()       #다리를 통과한 트럭의 무게(0일 수도 있음)
        csum -= passed                  #통과한 무게만큼 csum을 빼줌
        if csum + trucks[0] > weight:       # 다리위의 트럭 무게 합과 다음에 들어올 트럭의 무게의 합이 최대 하중보다 큰 경우
            bridge.append(0)                # 0만 푸쉬해줌으로써 시간을 소요함
        else:                           #최대 하중보다 작거나 같은 경우
            bridge.append(trucks[0])    #트럭을 다리위에 올리고
            csum += trucks.popleft()    #csum을 그 트럭의 무게만큼 더해줌
    
    answer = time + bridge_length       #마지막 트럭이 출발 후 종료되었으므로 마지막 트럭이 통과할때까지의 시간인 bridge_length를 더해줌
    return answer