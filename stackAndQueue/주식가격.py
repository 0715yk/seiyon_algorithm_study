# 2021.07.07. 2021 Stack/Queue(Programmers High score kit) 
# 주식 가격

'''
<문제>
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''

'''
<풀이>
스택을 이용했다. 
주식 가격들을 앞에서부터 하나씩 꺼내어
스택의 맨 마지막 요소(인덱스)에 해당하는 값과 비교하여,
주식 가격이 오른 경우에는 스택에 해당 주식 가격의 인덱스를 저장하고
주식 가격이 떨어진 경우에는 스택에 있는 인덱스를 꺼내어 현재 인덱스와 비교하여 차이만큼을 계산해 답을 내었다.
'''


def solution(prices):
    stack=[]    #인덱스를 저장할 스택
    answer = [0] * len(prices)      #prices의 길이만큼의 리스트 선언, 0으로 채워줌
    for i,v in enumerate(prices):   
        if i == len(prices)-1:                  #끝까지 가격이 떨어지지 않은 주식들의 경우
            while stack:                        #스택이 빌 때까지 그 기간을 계산해서 answer에 추가함
                last = stack.pop()
                answer[last] = i - last
                
        while stack and v < prices[stack[-1]]:  #스택이 존재하고(에러 방지를 위한 조건) 주식 가격이 떨어진 경우
            last = stack.pop()                  #last : 가격이 떨어진 값이 위치한 인덱스
            answer[last] = i - last             #현재 인덱스 i와 비교하여 차이만큼이 답

        stack.append(i) #스택에 현재 인덱스 값을 넣어줌
    return answer